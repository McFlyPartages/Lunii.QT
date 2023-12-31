import os.path
from pathlib import WindowsPath
from uuid import UUID

import requests
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QItemSelectionModel
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QFileDialog, QMessageBox
from PySide6.QtGui import QFont, QShortcut, QKeySequence, QPixmap, Qt

from pkg.api.device import find_devices, LuniiDevice, is_device
from pkg.api.stories import story_name, story_desc, DESC_NOT_FOUND, story_load_db, story_load_pict
from pkg.api.constants import *
from pkg.ierWorker import ierWorker, ACTION_REMOVE, ACTION_IMPORT, ACTION_EXPORT

from pkg.ui.main_ui import Ui_MainWindow

"""
TODO : 
 * Add free space
 * drag n drop to reorder list
 * select move up/down reset screen display
DONE
 * add cache mgmt in home dir (or local)
 * download story icon
 * display picture
 * add icon to app
 * add icon to refresh button
 * add icon to context menu
 * supporting entry for lunii path
 * create a dedicated thread for import / export / delete
"""

COL_NAME = 0
COL_UUID = 1


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        # class instance vars init
        self.lunii_device: LuniiDevice = None
        self.worker: ierWorker = None
        self.thread: QtCore.QThread = None

        # UI init
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.modify_widgets()
        self.setup_connections()
        self.cb_dev_refresh()

    # update ui elements state (enable, disable, context enu)
    def modify_widgets(self):
        # self.btn_abort.setVisible(False)
        # self.pgb_total.setVisible(False)
        self.tree_stories.setColumnWidth(0, 300)
        self.lbl_picture.setVisible(False)
        self.te_story_details.setVisible(False)

        # clean progress bars
        self.lbl_total.setVisible(False)
        self.pbar_total.setVisible(False)
        self.lbl_story.setVisible(False)
        self.pbar_story.setVisible(False)

        # Connect the context menu
        self.tree_stories.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree_stories.customContextMenuRequested.connect(self.ts_context_menu)

    # connecting slots and signals
    def setup_connections(self):
        self.combo_device.currentIndexChanged.connect(self.cb_dev_select)
        self.le_filter.textChanged.connect(self.ts_update)
        self.btn_refresh.clicked.connect(self.cb_dev_refresh)
        self.tree_stories.itemSelectionChanged.connect(self.cb_tree_select)
        self.tree_stories.installEventFilter(self)

        # signals connections
        # LuniiDevice.signal_zip_progress.connect(self.slot_zip_progress)

        # story list shortcuts
        QShortcut(QKeySequence("Alt+Up"), self.tree_stories, self.ts_move_up)
        QShortcut(QKeySequence("Alt+Down"), self.tree_stories, self.ts_move_down)
        QShortcut(QKeySequence("Delete"), self.tree_stories, self.ts_remove)
        QShortcut(QKeySequence("Ctrl+S"), self.tree_stories, self.ts_export)
        QShortcut(QKeySequence("Ctrl+I"), self.tree_stories, self.ts_import)
        QShortcut(QKeySequence("F5"), self, self.cb_dev_refresh)

    def eventFilter(self, obj, event):
        if obj.objectName() == "tree_stories":
            if event.type() == QtCore.QEvent.DragEnter:
                self.ts_dragenter_action(event)
                return True
            elif event.type() == QtCore.QEvent.Drop:
                self.ts_drop_action(event)
                return True
        return False

    # TREE WIDGET MANAGEMENT
    def ts_context_menu(self, point):
        # about the selected node.
        index = self.tree_stories.indexAt(point)

        # We build the menu.
        menu = QtWidgets.QMenu()
        act_mv_up = menu.addAction("Move Up")
        act_mv_down = menu.addAction("Move Down")
        menu.addSeparator()
        act_import = menu.addAction("Import")
        act_export = menu.addAction("Export")
        act_remove = menu.addAction("Remove")

        # config Tooltips
        act_mv_up.setToolTip("Move item upper (ATL + UP)")
        act_mv_down.setToolTip("Move item upper (ATL + DOWN)")
        act_import.setToolTip("Export story to Archive")
        act_export.setToolTip("Import story from Archive")
        act_remove.setToolTip("Remove story")

        # Loading icons
        icon = QtGui.QIcon()

        icon.addPixmap(QtGui.QPixmap(":/icon/res/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        act_mv_up.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(":/icon/res/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        act_mv_down.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(":/icon/res/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        act_import.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(":/icon/res/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        act_export.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(":/icon/res/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        act_remove.setIcon(icon)

        # not pointing to an item
        if not index.isValid():
            act_mv_up.setEnabled(False)
            act_mv_down.setEnabled(False)
            act_export.setEnabled(False)
            act_remove.setEnabled(False)

        if not self.lunii_device or self.worker:
            # during download or no device selected, no action possible
            act_mv_up.setEnabled(False)
            act_mv_down.setEnabled(False)
            act_import.setEnabled(False)
            act_export.setEnabled(False)
            act_remove.setEnabled(False)

        if self.lunii_device.lunii_version == LUNII_V3 and not self.lunii_device.device_key:
            act_export.setEnabled(False)

        # Checking action
        picked_action = menu.exec_(self.tree_stories.mapToGlobal(point))
        if picked_action == act_mv_up:
            self.ts_move_up()
        elif picked_action == act_mv_down:
            self.ts_move_down()
        elif picked_action == act_import:
            self.ts_import()
        elif picked_action == act_export:
            self.ts_export()
        elif picked_action == act_remove:
            self.ts_remove()

    # WIDGETS UPDATES
    def cb_dev_refresh(self):
        dev_list = find_devices()
        self.combo_device.clear()

        dev: WindowsPath
        self.combo_device.setPlaceholderText("Select your Lunii")
        self.lbl_version.setText("")
        self.statusbar.showMessage("")

        for dev in dev_list:
            dev_name = str(dev)
            # print(dev_name)
            self.combo_device.addItem(dev_name)

        if os.path.isdir("C:/Work/dev/lunii-packs/test/"):
            self.combo_device.addItem("C:/Work/dev/lunii-packs/test/_v2/")
            self.combo_device.addItem("C:/Work/dev/lunii-packs/test/_v3/")

        if self.combo_device.count():
            self.combo_device.lineEdit().setText("Select your Lunii")

            # automatic select if only one device
            if self.combo_device.count() == 1:
                self.combo_device.setCurrentIndex(0)
        else:
            self.statusbar.showMessage("No Lunii detected 😥, try to copy paste a path")
            self.combo_device.lineEdit().setText("Enter a path here")

    def cb_dev_select(self):
        # getting current device
        dev_name = self.combo_device.currentText()

        if dev_name:

            if not is_device(dev_name):
                self.statusbar.showMessage(f"ERROR : {dev_name} is not a recognized Lunii.")

                # removing the new entry
                cur_index = self.combo_device.currentIndex()
                self.combo_device.removeItem(cur_index)

                # picking another existing entry
                if self.combo_device.count() > 0:
                    self.combo_device.setCurrentIndex(0)
                else:
                    self.combo_device.lineEdit().setText("Enter a path here")

                return

            self.lunii_device = LuniiDevice(dev_name, V3_KEYS)
            self.statusbar.showMessage(f"")

            # updating UI to indicate version
            if self.lunii_device.lunii_version == LUNII_V2:
                self.lbl_version.setText("v2")
            elif self.lunii_device.lunii_version == LUNII_V3:
                self.lbl_version.setText("v3")
            self.ts_update()

    def cb_tree_select(self):
        # getting selection
        selection = self.tree_stories.selectedItems()
        only_one = len(selection) == 1
        # self.lbl_picture.setVisible(only_one)
        self.te_story_details.setVisible(only_one)
        self.lbl_picture.setVisible(only_one)

        if only_one:
            item = selection[0]
            uuid = item.text(COL_UUID)

            one_story_desc = story_desc(uuid)
            one_story_image = story_load_pict(uuid)

            # nothing to display
            if (not one_story_desc or one_story_desc == DESC_NOT_FOUND) and not one_story_image:
                self.te_story_details.setVisible(False)
                self.lbl_picture.setVisible(False)
                return

            # Update story description
            self.te_story_details.setText(one_story_desc)

            # Display image from URL or cache
            if one_story_image:
                pixmap = QPixmap()
                pixmap.loadFromData(one_story_image)

                scaled_pixmap = pixmap.scaled(192, 192, aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)
                self.lbl_picture.setPixmap(scaled_pixmap)
            else:
                self.lbl_picture.setText("Failed to fetch BMP file.")

    def ts_update(self):
        # clear previous story list
        self.tree_stories.clear()
        self.ts_populate()
        # update status in status bar
        # self.sb_update_summary()

        # clean progress bars
        # self.lbl_total.setVisible(False)
        # self.pbar_total.setVisible(False)
        # self.lbl_story.setVisible(False)
        # self.pbar_story.setVisible(False)

    def ts_populate(self):
        # empty device
        if self.lunii_device.stories is None or len(self.lunii_device.stories) == 0:
            return

        # creating font
        console_font = QFont()
        console_font.setFamilies([u"Consolas"])

        # getting filter text
        le_filter = self.le_filter.text()

        # adding items
        for story in self.lunii_device.stories:
            # filtering 
            if le_filter is not None and le_filter.lower() not in story_name(story).lower():
                continue

            # create and add item to treeWidget
            item = QTreeWidgetItem()
            item.setText(COL_NAME, story_name(story))
            item.setText(COL_UUID, str(story).upper())
            item.setFont(COL_UUID, console_font)
            self.tree_stories.addTopLevelItem(item)

    def sb_update_summary(self):
        # displayed items
        count_items = self.tree_stories.topLevelItemCount()

        sb_message = f" {count_items}/{len(self.lunii_device.stories)}"
        self.statusbar.showMessage(sb_message)

    def ts_move_up(self):
        # print("ts_move_up")
        self.ts_move(-1)

    def ts_move_down(self):
        # print("ts_move_down")
        self.ts_move(1)

    def ts_move(self, offset):
        # # no moves under filters
        # if self.le_filter.text():
        #     self.statusbar.showMessage("Remove filters before moving...")
        #     return

        sb_pos = self.tree_stories.verticalScrollBar().value()

        # getting selection
        selected = self.tree_stories.selectionModel().selection()
        selected_items = self.tree_stories.selectedItems()
        if len(selected_items) == 0:
            return

        old_idx = set()
        # getting all indexes to move (sorted)
        for item in selected_items:
            old_idx.add(self.lunii_device.stories.index(UUID(item.text(COL_UUID))))

        old_idx = sorted(old_idx)

        # updating new indexes
        new_idx = list()
        for pos, idx in enumerate(old_idx):
            # top reached ?
            if offset < 0 and idx <= pos:
                new_idx.append(idx)
                continue

            # bottom reached ?
            if offset > 0 and idx >= len(self.lunii_device.stories) - 1 - (len(old_idx) - 1 - pos):
                new_idx.append(idx)
                continue

            new_idx.append(idx + offset)

        # moving items
        for i in range(len(new_idx)):
            # depending on offset (up / down), list must be updated in specific order
            if offset > 0:
                i = len(new_idx) - 1 - i

            # print(f"{old_idx[i]} -> {new_idx[i]}")
            if old_idx[i] != new_idx[i]:
                self.lunii_device.stories.insert(new_idx[i], self.lunii_device.stories.pop(old_idx[i]))

        # update Lunii device (.pi)
        # TODO: update Lunii device (.pi)

        # refresh stories
        self.ts_update()

        # update selection
        sel_model = self.tree_stories.selectionModel()
        # sel_model.select(selected, QItemSelectionModel.Select)
        for idx in new_idx:
            item: QTreeWidgetItem = self.tree_stories.topLevelItem(idx)
            sel_model.select(self.tree_stories.indexFromItem(item, COL_NAME), QItemSelectionModel.Select)
            sel_model.select(self.tree_stories.indexFromItem(item, COL_UUID), QItemSelectionModel.Select)

        self.tree_stories.verticalScrollBar().setValue(sb_pos)

    def ts_remove(self):
        # getting selection
        selection = self.tree_stories.selectedItems()
        if len(selection) == 0:
            return

        # preparing validation window
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Delete stories")
        message = "You are requesting to delete : \n"
        for item in selection:
            message += f"- {item.text(COL_NAME)}\n"

        if len(message) > 512:
            message = message[:768] + "..."
            message += "\n(and too many others)\n"

        message += "\nDo you want to proceed ?"
        dlg.setText(message)
        dlg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        dlg.setIcon(QMessageBox.Warning)
        button = dlg.exec_()

        if button != QMessageBox.Ok:
            return

        # processing selection
        to_remove = [item.text(COL_UUID) for item in selection]
        self.worker_launch(ACTION_REMOVE, to_remove)

    def ts_export(self):
        # getting selection
        selection = self.tree_stories.selectedItems()
        if len(selection) == 0:
            return

        out_dir = QFileDialog.getExistingDirectory(self, "Ouput Directory for Stories", "",
                                                   QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)

        # if ok pressed
        if out_dir:
            to_export = [item.text(COL_UUID) for item in selection]
            self.worker_launch(ACTION_EXPORT, to_export, out_dir)

    def ts_import(self):
        if not self.lunii_device:
            return

        file_filter = "PK files (*.plain.pk *.pk);;Archive files (*.7z *.zip);;All supported (*.pk *.7z *.zip);;All files (*)"
        files, _ = QFileDialog.getOpenFileNames(self, "Open Stories", "", file_filter)

        if not files:
            return

        self.worker_launch(ACTION_IMPORT, files)

    def ts_dragenter_action(self, event):
        # a Lunii must be selected
        if not self.lunii_device:
            event.ignore()
            return

        # must be files
        if event.mimeData().hasUrls():
            # getting path for dropped files
            file_paths = [url.toLocalFile() for url in event.mimeData().urls()]

            # checking if dropped files are ending with expected extensions
            if all(any(file.endswith(ext) for ext in SUPPORTED_EXT) for file in file_paths):
                event.acceptProposedAction()
            else:
                event.ignore()

    def ts_drop_action(self, event):
        # getting path for dropped files
        file_paths = [url.toLocalFile() for url in event.mimeData().urls()]

        self.worker_launch(ACTION_IMPORT, file_paths)

    def worker_launch(self, action, item_list, out_dir = None):
        if self.worker:
            return

        # setting up the thread
        self.worker = ierWorker(self.lunii_device, action, item_list, out_dir)
        self.thread = QtCore.QThread()
        self.worker.moveToThread(self.thread)

        # connecting slots
        self.thread.started.connect(self.worker.process)
        self.worker.signal_finished.connect(self.thread.quit)
        self.worker.signal_total_progress.connect(self.slot_total_progress)
        self.lunii_device.signal_story_progress.connect(self.slot_story_progress)
        self.worker.signal_finished.connect(self.slot_finished)
        self.worker.signal_refresh.connect(self.ts_update)
        self.worker.signal_message.connect(self.statusbar.showMessage)

        # running
        self.thread.start()

    def slot_total_progress(self, current, max_val):
        # updating UI
        self.tree_stories.setEnabled(False)
        self.lbl_total.setVisible(True)
        self.lbl_total.setText(f"Total {current+1}/{max_val}")
        self.pbar_total.setVisible(True)
        self.pbar_total.setRange(0, max_val)
        self.pbar_total.setValue(current+1)

    def slot_story_progress(self, uuid, current, max_val):
        # updating UI
        self.lbl_story.setVisible(True)
        self.lbl_story.setText(uuid)

        self.pbar_story.setVisible(True)
        self.pbar_story.setRange(0, max_val)
        self.pbar_story.setValue(current+1)

    def slot_finished(self):
        # print("SLOT FINISHED")
        # updating UI
        self.tree_stories.setEnabled(True)

        self.lbl_total.setVisible(False)
        self.pbar_total.setVisible(False)
        self.lbl_story.setVisible(False)
        self.pbar_story.setVisible(False)

        self.worker = None
        self.thread = None


    def slot_zip_progress(self, message, progress):
        # handling progress bar
        if not self.pbar_total.isVisible() and progress != 100:
            self.pbar_total.setVisible(True)

        if progress >= 100:
            self.pbar_total.setVisible(False)

        # putting message
        self.statusbar.showMessage(message)
