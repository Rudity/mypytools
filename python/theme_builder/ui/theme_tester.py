# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Work\GitHub\mypytools\python\theme_builder\ui\theme_tester.ui'
#
# Created: Sun May 03 20:59:23 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(790, 1003)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(240, 0))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(self.tab)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 222, 753))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_4.addWidget(self.label_7)
        self.textEdit_3 = Qsci.QsciScintilla(self.scrollAreaWidgetContents)
        self.textEdit_3.setToolTip(_fromUtf8(""))
        self.textEdit_3.setWhatsThis(_fromUtf8(""))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.verticalLayout_4.addWidget(self.textEdit_3)
        self.textEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_4.addWidget(self.textEdit)
        self.textEdit_2 = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.verticalLayout_4.addWidget(self.textEdit_2)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_4.addWidget(self.plainTextEdit)
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.verticalLayout_4.addWidget(self.plainTextEdit_2)
        self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_4.addWidget(self.label_9)
        self.declarativeView = QtDeclarative.QDeclarativeView(self.scrollAreaWidgetContents)
        self.declarativeView.setObjectName(_fromUtf8("declarativeView"))
        self.verticalLayout_4.addWidget(self.declarativeView)
        self.spinBox = QtGui.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.verticalLayout_4.addWidget(self.spinBox)
        self.spinBox_2 = QtGui.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_2.setEnabled(False)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.verticalLayout_4.addWidget(self.spinBox_2)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.verticalLayout_4.addWidget(self.doubleSpinBox)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_2.setEnabled(False)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.verticalLayout_4.addWidget(self.doubleSpinBox_2)
        self.lineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.comboBox_3 = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.verticalLayout_4.addWidget(self.comboBox_3)
        self.comboBox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setEnabled(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout_4.addWidget(self.comboBox)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)
        self.line_2 = QtGui.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(0, 20))
        self.line_2.setBaseSize(QtCore.QSize(0, 30))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_4.addWidget(self.line_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_8.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout_6.addWidget(self.checkBox_2)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_6.addWidget(self.checkBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.radioButton_3 = QtGui.QRadioButton(self.frame)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_9.addWidget(self.radioButton_3)
        self.radioButton_2 = QtGui.QRadioButton(self.frame)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_9.addWidget(self.radioButton_2)
        self.radioButton = QtGui.QRadioButton(self.frame)
        self.radioButton.setEnabled(False)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_9.addWidget(self.radioButton)
        self.verticalLayout_3.addWidget(self.frame)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.toolButton_2 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout_5.addWidget(self.toolButton_2)
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.toolButton.setEnabled(False)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout_5.addWidget(self.toolButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setFrameShape(QtGui.QFrame.WinPanel)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.page_3)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_2 = QtGui.QLabel(self.page_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_11.addWidget(self.label_2)
        self.pushButton_3 = QtGui.QPushButton(self.page_3)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_11.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.page_3)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_11.addWidget(self.pushButton_4)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.page_4)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.pushButton_5 = QtGui.QPushButton(self.page_4)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_6.addWidget(self.pushButton_5)
        self.pushButton_6 = QtGui.QPushButton(self.page_4)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout_6.addWidget(self.pushButton_6)
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalSlider_2 = QtGui.QSlider(self.centralwidget)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName(_fromUtf8("verticalSlider_2"))
        self.horizontalLayout_7.addWidget(self.verticalSlider_2)
        self.verticalSlider = QtGui.QSlider(self.centralwidget)
        self.verticalSlider.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider.sizePolicy().hasHeightForWidth())
        self.verticalSlider.setSizePolicy(sizePolicy)
        self.verticalSlider.setBaseSize(QtCore.QSize(0, 40))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.horizontalLayout_7.addWidget(self.verticalSlider)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_3.addWidget(self.label_8)
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 268, 89))
        self.page.setObjectName(_fromUtf8("page"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label = QtGui.QLabel(self.page)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_10.addWidget(self.label)
        self.columnView = QtGui.QColumnView(self.page)
        self.columnView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.columnView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.columnView.setObjectName(_fromUtf8("columnView"))
        self.horizontalLayout_10.addWidget(self.columnView)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 278, 68))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.toolBox)
        self.buttonBox_2 = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox_2.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName(_fromUtf8("buttonBox_2"))
        self.verticalLayout_3.addWidget(self.buttonBox_2)
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setEnabled(False)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.verticalLayout_3.addWidget(self.horizontalSlider)
        self.horizontalSlider_2 = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_2.setEnabled(False)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.verticalLayout_3.addWidget(self.horizontalSlider_2)
        self.fontComboBox = QtGui.QFontComboBox(self.centralwidget)
        self.fontComboBox.setObjectName(_fromUtf8("fontComboBox"))
        self.verticalLayout_3.addWidget(self.fontComboBox)
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.verticalLayout_3.addWidget(self.commandLinkButton)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.verticalLayout_3.addWidget(self.dateTimeEdit)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.verticalLayout_3.addWidget(self.dateEdit)
        self.timeEdit = QtGui.QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.verticalLayout_3.addWidget(self.timeEdit)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.dial = QtGui.QDial(self.centralwidget)
        self.dial.setObjectName(_fromUtf8("dial"))
        self.verticalLayout_5.addWidget(self.dial)
        self.dial_2 = QtGui.QDial(self.centralwidget)
        self.dial_2.setEnabled(False)
        self.dial_2.setObjectName(_fromUtf8("dial_2"))
        self.verticalLayout_5.addWidget(self.dial_2)
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_5.addWidget(self.textBrowser)
        self.textBrowser_2 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setEnabled(False)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.verticalLayout_5.addWidget(self.textBrowser_2)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_5.addWidget(self.listWidget)
        self.listWidget_2 = QtGui.QListWidget(self.centralwidget)
        self.listWidget_2.setEnabled(False)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        item = QtGui.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.verticalLayout_5.addWidget(self.listWidget_2)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_5.addWidget(self.label_6)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout_5.addWidget(self.treeWidget)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.verticalLayout_5.addWidget(self.treeView)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_5.addWidget(self.progressBar)
        self.progressBar_2 = QtGui.QProgressBar(self.centralwidget)
        self.progressBar_2.setEnabled(False)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.verticalLayout_5.addWidget(self.progressBar_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMainWindow = QtGui.QMenu(self.menubar)
        self.menuMainWindow.setObjectName(_fromUtf8("menuMainWindow"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_10 = QtGui.QLabel(self.dockWidgetContents)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_12.addWidget(self.label_10)
        self.listView = QtGui.QListView(self.dockWidgetContents)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.horizontalLayout_12.addWidget(self.listView)
        self.listView_2 = QtGui.QListView(self.dockWidgetContents)
        self.listView_2.setEnabled(False)
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.horizontalLayout_12.addWidget(self.listView_2)
        self.label_5 = QtGui.QLabel(self.dockWidgetContents)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_12.addWidget(self.label_5)
        self.tableView = QtGui.QTableView(self.dockWidgetContents)
        self.tableView.setMinimumSize(QtCore.QSize(450, 0))
        self.tableView.setBaseSize(QtCore.QSize(600, 0))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.horizontalLayout_12.addWidget(self.tableView)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget)
        self.actionA = QtGui.QAction(MainWindow)
        self.actionA.setObjectName(_fromUtf8("actionA"))
        self.actionB = QtGui.QAction(MainWindow)
        self.actionB.setObjectName(_fromUtf8("actionB"))
        self.actionC = QtGui.QAction(MainWindow)
        self.actionC.setObjectName(_fromUtf8("actionC"))
        self.actionD = QtGui.QAction(MainWindow)
        self.actionD.setObjectName(_fromUtf8("actionD"))
        self.menuMainWindow.addAction(self.actionA)
        self.menuMainWindow.addSeparator()
        self.menuMainWindow.addAction(self.actionB)
        self.menuMainWindow.addAction(self.actionC)
        self.menuMainWindow.addSeparator()
        self.menuMainWindow.addAction(self.actionD)
        self.menubar.addAction(self.menuMainWindow.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_7.setText(_translate("MainWindow", "QsciScintilla", None))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">test</span></p></body></html>", None))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "test", None))
        self.label_9.setText(_translate("MainWindow", "QDeclarativeView", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "A", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "B", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "C", None))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "D", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.pushButton.setToolTip(_translate("MainWindow", "This is the toolTip", None))
        self.pushButton.setStatusTip(_translate("MainWindow", "This is the statusTip", None))
        self.pushButton.setWhatsThis(_translate("MainWindow", "This is whatsThis", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox.setText(_translate("MainWindow", "CheckBox", None))
        self.radioButton_3.setWhatsThis(_translate("MainWindow", "This is whatsThis", None))
        self.radioButton_3.setText(_translate("MainWindow", "RadioButton", None))
        self.radioButton_2.setText(_translate("MainWindow", "RadioButton", None))
        self.radioButton.setText(_translate("MainWindow", "RadioButton", None))
        self.toolButton_2.setStatusTip(_translate("MainWindow", "This is a statusTip", None))
        self.toolButton_2.setText(_translate("MainWindow", "QToolButton", None))
        self.toolButton.setText(_translate("MainWindow", "QToolButton", None))
        self.label_2.setText(_translate("MainWindow", "StackedWidget", None))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton", None))
        self.label_8.setText(_translate("MainWindow", "QGraphicsView", None))
        self.label.setText(_translate("MainWindow", "ColumnView", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page 1 - toolBox", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Page 2 - toolBox", None))
        self.commandLinkButton.setText(_translate("MainWindow", "CommandLinkButton", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "A", None))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "B", None))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "C", None))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "D", None))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "E", None))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "F", None))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "G", None))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "H", None))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "I", None))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "J", None))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "K", None))
        item = self.listWidget.item(11)
        item.setText(_translate("MainWindow", "L", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "A", None))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "B", None))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "C", None))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "D", None))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("MainWindow", "TableWidget", None))
        self.label_3.setText(_translate("MainWindow", "TreeWidget", None))
        self.label_4.setText(_translate("MainWindow", "TreeView", None))
        self.menuMainWindow.setTitle(_translate("MainWindow", "MainWindow", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "dockWidget", None))
        self.label_10.setText(_translate("MainWindow", "ListView:", None))
        self.label_5.setText(_translate("MainWindow", "TableView", None))
        self.actionA.setText(_translate("MainWindow", "A", None))
        self.actionB.setText(_translate("MainWindow", "B", None))
        self.actionC.setText(_translate("MainWindow", "C", None))
        self.actionD.setText(_translate("MainWindow", "D", None))

from PyQt4 import Qsci
from PyQt4 import QtDeclarative
