# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Work\GitHub\mypytools\python\cell_compare\core\gui\ui\main_window.ui'
#
# Created: Thu Apr 23 23:57:39 2015
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

class Ui_compare_cell(object):
    def setupUi(self, compare_cell):
        compare_cell.setObjectName(_fromUtf8("compare_cell"))
        compare_cell.resize(642, 674)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/wishlist_add.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        compare_cell.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(compare_cell)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setMargin(4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.add_cell_control_button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_cell_control_button.sizePolicy().hasHeightForWidth())
        self.add_cell_control_button.setSizePolicy(sizePolicy)
        self.add_cell_control_button.setMinimumSize(QtCore.QSize(32, 32))
        self.add_cell_control_button.setMaximumSize(QtCore.QSize(32, 32))
        self.add_cell_control_button.setBaseSize(QtCore.QSize(10, 10))
        self.add_cell_control_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_cell_control_button.setIcon(icon1)
        self.add_cell_control_button.setIconSize(QtCore.QSize(24, 24))
        self.add_cell_control_button.setObjectName(_fromUtf8("add_cell_control_button"))
        self.horizontalLayout.addWidget(self.add_cell_control_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.scrollArea.setFrameShape(QtGui.QFrame.Box)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 615, 529))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scroll_vertical_layout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scroll_vertical_layout.setSpacing(10)
        self.scroll_vertical_layout.setMargin(8)
        self.scroll_vertical_layout.setObjectName(_fromUtf8("scroll_vertical_layout"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.compare = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compare.sizePolicy().hasHeightForWidth())
        self.compare.setSizePolicy(sizePolicy)
        self.compare.setMinimumSize(QtCore.QSize(50, 50))
        self.compare.setMaximumSize(QtCore.QSize(100, 50))
        self.compare.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/after_update.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.compare.setIcon(icon2)
        self.compare.setIconSize(QtCore.QSize(32, 32))
        self.compare.setObjectName(_fromUtf8("compare"))
        self.horizontalLayout_2.addWidget(self.compare)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        compare_cell.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(compare_cell)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        compare_cell.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(compare_cell)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 642, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        compare_cell.setMenuBar(self.menuBar)
        self.actionA = QtGui.QAction(compare_cell)
        self.actionA.setObjectName(_fromUtf8("actionA"))
        self.actionB = QtGui.QAction(compare_cell)
        self.actionB.setObjectName(_fromUtf8("actionB"))
        self.menuFile.addAction(self.actionA)
        self.menuFile.addAction(self.actionB)
        self.menuFile.addSeparator()
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(compare_cell)
        QtCore.QMetaObject.connectSlotsByName(compare_cell)

    def retranslateUi(self, compare_cell):
        compare_cell.setWindowTitle(_translate("compare_cell", "Compare Cell", None))
        self.add_cell_control_button.setToolTip(_translate("compare_cell", "add cell control", None))
        self.scrollArea.setToolTip(_translate("compare_cell", "add cell controls to compare workbooks here", None))
        self.menuFile.setTitle(_translate("compare_cell", "File", None))
        self.actionA.setText(_translate("compare_cell", "Export Cell Data", None))
        self.actionB.setText(_translate("compare_cell", "Import Cell Data", None))

