# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextBrowser, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(665, 600)
        MainWindow.setMinimumSize(QSize(500, 0))
        icon = QIcon()
        icon.addFile(u":/icon/res/lunii.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        icon1 = QIcon()
        icon1.addFile(u":/icon/res/import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionImport.setIcon(icon1)
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        icon2 = QIcon()
        icon2.addFile(u":/icon/res/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExport.setIcon(icon2)
        self.actionExport_All = QAction(MainWindow)
        self.actionExport_All.setObjectName(u"actionExport_All")
        self.actionExport_All.setIcon(icon2)
        self.actionMove_Up = QAction(MainWindow)
        self.actionMove_Up.setObjectName(u"actionMove_Up")
        icon3 = QIcon()
        icon3.addFile(u":/icon/res/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMove_Up.setIcon(icon3)
        self.actionMove_Down = QAction(MainWindow)
        self.actionMove_Down.setObjectName(u"actionMove_Down")
        icon4 = QIcon()
        icon4.addFile(u":/icon/res/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMove_Down.setIcon(icon4)
        self.actionRemove = QAction(MainWindow)
        self.actionRemove.setObjectName(u"actionRemove")
        icon5 = QIcon()
        icon5.addFile(u":/icon/res/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRemove.setIcon(icon5)
        self.actionShow_size = QAction(MainWindow)
        self.actionShow_size.setObjectName(u"actionShow_size")
        self.actionShow_size.setCheckable(True)
        self.actionShow_size.setChecked(True)
        self.actionShow_size.setEnabled(True)
        self.actionGet_firmware = QAction(MainWindow)
        self.actionGet_firmware.setObjectName(u"actionGet_firmware")
        self.actionGet_firmware.setEnabled(False)
        icon6 = QIcon()
        icon6.addFile(u":/icon/res/fw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionGet_firmware.setIcon(icon6)
        self.actionShow_story_details = QAction(MainWindow)
        self.actionShow_story_details.setObjectName(u"actionShow_story_details")
        self.actionShow_story_details.setCheckable(True)
        self.actionShow_story_details.setChecked(True)
        self.actionMove_Top = QAction(MainWindow)
        self.actionMove_Top.setObjectName(u"actionMove_Top")
        icon7 = QIcon()
        icon7.addFile(u":/icon/res/top.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMove_Top.setIcon(icon7)
        self.actionMove_Bottom = QAction(MainWindow)
        self.actionMove_Bottom.setObjectName(u"actionMove_Bottom")
        icon8 = QIcon()
        icon8.addFile(u":/icon/res/bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMove_Bottom.setIcon(icon8)
        self.actionOpen_Lunii = QAction(MainWindow)
        self.actionOpen_Lunii.setObjectName(u"actionOpen_Lunii")
        icon9 = QIcon()
        icon9.addFile(u":/icon/res/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_Lunii.setIcon(icon9)
        self.actionShow_Log = QAction(MainWindow)
        self.actionShow_Log.setObjectName(u"actionShow_Log")
        icon10 = QIcon()
        icon10.addFile(u":/icon/res/debug_log.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionShow_Log.setIcon(icon10)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon11 = QIcon()
        icon11.addFile(u":/icon/res/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon11)
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        self.actionUpdate.setIcon(icon6)
        self.actionTranscode = QAction(MainWindow)
        self.actionTranscode.setObjectName(u"actionTranscode")
        self.actionTranscode.setCheckable(True)
        self.actionTranscode.setChecked(True)
        self.actionTranscode.setEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_layout = QHBoxLayout()
        self.top_layout.setSpacing(6)
        self.top_layout.setObjectName(u"top_layout")
        self.btn_refresh = QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(9)
        self.btn_refresh.setFont(font)
        icon12 = QIcon()
        icon12.addFile(u":/icon/res/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh.setIcon(icon12)
        self.btn_refresh.setIconSize(QSize(22, 22))
        self.btn_refresh.setFlat(True)

        self.top_layout.addWidget(self.btn_refresh)

        self.combo_device = QComboBox(self.centralwidget)
        self.combo_device.addItem("")
        self.combo_device.addItem("")
        self.combo_device.setObjectName(u"combo_device")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_device.sizePolicy().hasHeightForWidth())
        self.combo_device.setSizePolicy(sizePolicy)
        self.combo_device.setMaximumSize(QSize(200, 16777215))
        self.combo_device.setEditable(False)

        self.top_layout.addWidget(self.combo_device)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.top_layout.addItem(self.horizontalSpacer)

        self.le_filter = QLineEdit(self.centralwidget)
        self.le_filter.setObjectName(u"le_filter")
        self.le_filter.setClearButtonEnabled(True)

        self.top_layout.addWidget(self.le_filter)

        self.btn_db = QPushButton(self.centralwidget)
        self.btn_db.setObjectName(u"btn_db")
        self.btn_db.setMaximumSize(QSize(25, 25))
        icon13 = QIcon()
        icon13.addFile(u":/icon/res/refresh_db.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_db.setIcon(icon13)
        self.btn_db.setIconSize(QSize(22, 22))
        self.btn_db.setFlat(True)

        self.top_layout.addWidget(self.btn_db)


        self.verticalLayout_2.addLayout(self.top_layout)

        self.tree_stories = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setText(2, u"UUID");
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        self.tree_stories.setHeaderItem(__qtreewidgetitem)
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        __qtreewidgetitem1 = QTreeWidgetItem(self.tree_stories)
        __qtreewidgetitem1.setFont(2, font1);
        __qtreewidgetitem2 = QTreeWidgetItem(self.tree_stories)
        __qtreewidgetitem2.setFont(2, font1);
        QTreeWidgetItem(self.tree_stories)
        QTreeWidgetItem(self.tree_stories)
        self.tree_stories.setObjectName(u"tree_stories")
        self.tree_stories.setMinimumSize(QSize(0, 150))
        self.tree_stories.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tree_stories.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tree_stories.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tree_stories.setDragEnabled(True)
        self.tree_stories.setDragDropMode(QAbstractItemView.DropOnly)
        self.tree_stories.setDefaultDropAction(Qt.MoveAction)
        self.tree_stories.setAlternatingRowColors(True)
        self.tree_stories.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree_stories.setIndentation(20)
        self.tree_stories.setRootIsDecorated(True)
        self.tree_stories.setItemsExpandable(True)
        self.tree_stories.setAllColumnsShowFocus(True)

        self.verticalLayout_2.addWidget(self.tree_stories)

        self.progressLayout = QVBoxLayout()
        self.progressLayout.setSpacing(0)
        self.progressLayout.setObjectName(u"progressLayout")
        self.totalLayout = QHBoxLayout()
        self.totalLayout.setSpacing(6)
        self.totalLayout.setObjectName(u"totalLayout")
        self.lbl_total = QLabel(self.centralwidget)
        self.lbl_total.setObjectName(u"lbl_total")
        self.lbl_total.setMinimumSize(QSize(80, 0))
        self.lbl_total.setFrameShape(QFrame.Panel)
        self.lbl_total.setFrameShadow(QFrame.Sunken)
        self.lbl_total.setAlignment(Qt.AlignCenter)

        self.totalLayout.addWidget(self.lbl_total)

        self.pbar_total = QProgressBar(self.centralwidget)
        self.pbar_total.setObjectName(u"pbar_total")
        self.pbar_total.setMaximumSize(QSize(16777215, 10))
        self.pbar_total.setValue(24)
        self.pbar_total.setTextVisible(False)

        self.totalLayout.addWidget(self.pbar_total)


        self.progressLayout.addLayout(self.totalLayout)

        self.storyLayout = QHBoxLayout()
        self.storyLayout.setSpacing(6)
        self.storyLayout.setObjectName(u"storyLayout")
        self.lbl_story = QLabel(self.centralwidget)
        self.lbl_story.setObjectName(u"lbl_story")
        self.lbl_story.setMinimumSize(QSize(80, 0))
        self.lbl_story.setFrameShape(QFrame.Panel)
        self.lbl_story.setFrameShadow(QFrame.Sunken)
        self.lbl_story.setAlignment(Qt.AlignCenter)

        self.storyLayout.addWidget(self.lbl_story)

        self.pbar_story = QProgressBar(self.centralwidget)
        self.pbar_story.setObjectName(u"pbar_story")
        self.pbar_story.setMaximumSize(QSize(16777215, 10))
        self.pbar_story.setValue(24)
        self.pbar_story.setTextVisible(False)

        self.storyLayout.addWidget(self.pbar_story)


        self.progressLayout.addLayout(self.storyLayout)


        self.verticalLayout_2.addLayout(self.progressLayout)

        self.details_layout = QHBoxLayout()
        self.details_layout.setObjectName(u"details_layout")
        self.details_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.lbl_picture = QLabel(self.centralwidget)
        self.lbl_picture.setObjectName(u"lbl_picture")
        self.lbl_picture.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_picture.sizePolicy().hasHeightForWidth())
        self.lbl_picture.setSizePolicy(sizePolicy1)
        self.lbl_picture.setMinimumSize(QSize(192, 0))
        font2 = QFont()
        font2.setPointSize(12)
        self.lbl_picture.setFont(font2)
        self.lbl_picture.setAlignment(Qt.AlignCenter)

        self.details_layout.addWidget(self.lbl_picture)

        self.te_story_details = QTextBrowser(self.centralwidget)
        self.te_story_details.setObjectName(u"te_story_details")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.te_story_details.sizePolicy().hasHeightForWidth())
        self.te_story_details.setSizePolicy(sizePolicy2)
        self.te_story_details.setMaximumSize(QSize(16777215, 192))
        self.te_story_details.setOpenExternalLinks(True)
        self.te_story_details.setOpenLinks(False)

        self.details_layout.addWidget(self.te_story_details)


        self.verticalLayout_2.addLayout(self.details_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QRect(0, 0, 665, 22))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTools = QMenu(self.menuBar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuStory = QMenu(self.menuBar)
        self.menuStory.setObjectName(u"menuStory")
        self.menuUpdate = QMenu(self.menuBar)
        self.menuUpdate.setObjectName(u"menuUpdate")
        self.menuUpdate.setEnabled(False)
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.combo_device, self.le_filter)
        QWidget.setTabOrder(self.le_filter, self.tree_stories)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuStory.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuBar.addAction(self.menuUpdate.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Lunii)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionShow_size)
        self.menuTools.addAction(self.actionShow_story_details)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionShow_Log)
        self.menuTools.addAction(self.actionGet_firmware)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionTranscode)
        self.menuStory.addAction(self.actionMove_Top)
        self.menuStory.addAction(self.actionMove_Up)
        self.menuStory.addAction(self.actionMove_Down)
        self.menuStory.addAction(self.actionMove_Bottom)
        self.menuStory.addSeparator()
        self.menuStory.addAction(self.actionImport)
        self.menuStory.addAction(self.actionExport)
        self.menuStory.addAction(self.actionExport_All)
        self.menuStory.addAction(self.actionRemove)
        self.menuHelp.addAction(self.actionUpdate)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.combo_device.currentIndexChanged.connect(self.tree_stories.clear)
        self.actionExit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lunii Qt-Manager", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
#if QT_CONFIG(shortcut)
        self.actionImport.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
#if QT_CONFIG(shortcut)
        self.actionExport.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExport_All.setText(QCoreApplication.translate("MainWindow", u"Export All", None))
#if QT_CONFIG(shortcut)
        self.actionExport_All.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionMove_Up.setText(QCoreApplication.translate("MainWindow", u"Move Up", None))
#if QT_CONFIG(shortcut)
        self.actionMove_Up.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionMove_Down.setText(QCoreApplication.translate("MainWindow", u"Move Down", None))
#if QT_CONFIG(shortcut)
        self.actionMove_Down.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Down", None))
#endif // QT_CONFIG(shortcut)
        self.actionRemove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
#if QT_CONFIG(shortcut)
        self.actionRemove.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.actionShow_size.setText(QCoreApplication.translate("MainWindow", u"Show size", None))
#if QT_CONFIG(tooltip)
        self.actionShow_size.setToolTip(QCoreApplication.translate("MainWindow", u"Show size for each stories", None))
#endif // QT_CONFIG(tooltip)
        self.actionGet_firmware.setText(QCoreApplication.translate("MainWindow", u"Get FW Update", None))
#if QT_CONFIG(tooltip)
        self.actionGet_firmware.setToolTip(QCoreApplication.translate("MainWindow", u"Get firmaware update for current Lunii", None))
#endif // QT_CONFIG(tooltip)
        self.actionShow_story_details.setText(QCoreApplication.translate("MainWindow", u"Show story details", None))
        self.actionMove_Top.setText(QCoreApplication.translate("MainWindow", u"Move Top", None))
#if QT_CONFIG(shortcut)
        self.actionMove_Top.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionMove_Bottom.setText(QCoreApplication.translate("MainWindow", u"Move Bottom", None))
#if QT_CONFIG(shortcut)
        self.actionMove_Bottom.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Down", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen_Lunii.setText(QCoreApplication.translate("MainWindow", u"Open Lunii", None))
#if QT_CONFIG(shortcut)
        self.actionOpen_Lunii.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionShow_Log.setText(QCoreApplication.translate("MainWindow", u"Show Log", None))
#if QT_CONFIG(shortcut)
        self.actionShow_Log.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", u"Update to v2.X.X", None))
        self.actionTranscode.setText(QCoreApplication.translate("MainWindow", u"FFMPEG detected", None))
#if QT_CONFIG(tooltip)
        self.btn_refresh.setToolTip(QCoreApplication.translate("MainWindow", u"Refresh connected devices", None))
#endif // QT_CONFIG(tooltip)
        self.btn_refresh.setText("")
        self.combo_device.setItemText(0, QCoreApplication.translate("MainWindow", u"D:\\", None))
        self.combo_device.setItemText(1, QCoreApplication.translate("MainWindow", u"F:\\", None))

#if QT_CONFIG(tooltip)
        self.combo_device.setToolTip(QCoreApplication.translate("MainWindow", u"Select your Lunii", None))
#endif // QT_CONFIG(tooltip)
        self.combo_device.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select your Lunii", None))
        self.le_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type to filter", None))
#if QT_CONFIG(tooltip)
        self.btn_db.setToolTip(QCoreApplication.translate("MainWindow", u"Force official Lunii DB to be refreshed", None))
#endif // QT_CONFIG(tooltip)
        self.btn_db.setText("")
        ___qtreewidgetitem = self.tree_stories.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"DB", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Story Name", None));

        __sortingEnabled = self.tree_stories.isSortingEnabled()
        self.tree_stories.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.tree_stories.topLevelItem(0)
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"75MB", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"C4139D59-872A-4D15-8CF1-76D34CDF38C6", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"O", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Suzanne et Gaston", None));
        ___qtreewidgetitem2 = self.tree_stories.topLevelItem(1)
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("MainWindow", u"65MB", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"03933BA4-4FBF-475F-9ECC-35EFB4D11DC9", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"O", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Panique aux 6 Royaumes", None));
        ___qtreewidgetitem3 = self.tree_stories.topLevelItem(2)
        ___qtreewidgetitem3.setText(3, QCoreApplication.translate("MainWindow", u"124MB", None));
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("MainWindow", u"22137B29-8646-4335-8069-4A4C9A2D7E89", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"O", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Au Pays des Loups", None));
        ___qtreewidgetitem4 = self.tree_stories.topLevelItem(3)
        ___qtreewidgetitem4.setText(3, QCoreApplication.translate("MainWindow", u"25MB", None));
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("MainWindow", u"29264ADF-5A9F-451A-B1EC-2AE21BBA473C", None));
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"C", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Sur les bancs de l'\u00e9cole", None));
        self.tree_stories.setSortingEnabled(__sortingEnabled)

        self.lbl_total.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.lbl_story.setText(QCoreApplication.translate("MainWindow", u"8B_UUID", None))
        self.lbl_picture.setText(QCoreApplication.translate("MainWindow", u"No Thumb", None))
        self.te_story_details.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Story description", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"&Tools", None))
        self.menuStory.setTitle(QCoreApplication.translate("MainWindow", u"&Stories", None))
        self.menuUpdate.setTitle(QCoreApplication.translate("MainWindow", u"Update 2.2.X is released", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

