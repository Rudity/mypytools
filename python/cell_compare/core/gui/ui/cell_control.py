# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Work\GitHub\mypytools\python\cell_compare\core\gui\ui\cell_control.ui'
#
# Created: Tue May 05 22:25:12 2015
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

class Ui_cell_control(object):
    def setupUi(self, cell_control):
        cell_control.setObjectName(_fromUtf8("cell_control"))
        cell_control.resize(497, 154)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(cell_control.sizePolicy().hasHeightForWidth())
        cell_control.setSizePolicy(sizePolicy)
        cell_control.setMaximumSize(QtCore.QSize(16777215, 16777215))
        cell_control.setFocusPolicy(QtCore.Qt.NoFocus)
        cell_control.setAutoFillBackground(False)
        self.verticalLayout_2 = QtGui.QVBoxLayout(cell_control)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.custom_name_frame = QtGui.QFrame(cell_control)
        self.custom_name_frame.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.custom_name_frame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.custom_name_frame.setFrameShape(QtGui.QFrame.Box)
        self.custom_name_frame.setObjectName(_fromUtf8("custom_name_frame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.custom_name_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.custom_title_label = QtGui.QLabel(self.custom_name_frame)
        self.custom_title_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.custom_title_label.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.custom_title_label.setScaledContents(False)
        self.custom_title_label.setWordWrap(True)
        self.custom_title_label.setMargin(4)
        self.custom_title_label.setIndent(4)
        self.custom_title_label.setOpenExternalLinks(False)
        self.custom_title_label.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.custom_title_label.setObjectName(_fromUtf8("custom_title_label"))
        self.horizontalLayout.addWidget(self.custom_title_label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.controls_horizontalLayout = QtGui.QHBoxLayout()
        self.controls_horizontalLayout.setObjectName(_fromUtf8("controls_horizontalLayout"))
        self.cell_match_icon = QtGui.QLabel(self.custom_name_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cell_match_icon.sizePolicy().hasHeightForWidth())
        self.cell_match_icon.setSizePolicy(sizePolicy)
        self.cell_match_icon.setMinimumSize(QtCore.QSize(60, 60))
        self.cell_match_icon.setMaximumSize(QtCore.QSize(60, 60))
        self.cell_match_icon.setText(_fromUtf8(""))
        self.cell_match_icon.setPixmap(QtGui.QPixmap(_fromUtf8("../icons/ask_and_answer.png")))
        self.cell_match_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.cell_match_icon.setObjectName(_fromUtf8("cell_match_icon"))
        self.controls_horizontalLayout.addWidget(self.cell_match_icon)
        self.contols_verticalLayout = QtGui.QVBoxLayout()
        self.contols_verticalLayout.setSpacing(4)
        self.contols_verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.contols_verticalLayout.setObjectName(_fromUtf8("contols_verticalLayout"))
        self.controls_horizontalLayout.addLayout(self.contols_verticalLayout)
        self.verticalLayout_3.addLayout(self.controls_horizontalLayout)
        self.label = QtGui.QLabel(self.custom_name_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.notesTextEdit = QtGui.QTextEdit(self.custom_name_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notesTextEdit.sizePolicy().hasHeightForWidth())
        self.notesTextEdit.setSizePolicy(sizePolicy)
        self.notesTextEdit.setMaximumSize(QtCore.QSize(16777215, 75))
        self.notesTextEdit.setFrameShape(QtGui.QFrame.Box)
        self.notesTextEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.notesTextEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.notesTextEdit.setTabStopWidth(12)
        self.notesTextEdit.setObjectName(_fromUtf8("notesTextEdit"))
        self.verticalLayout_3.addWidget(self.notesTextEdit)
        self.verticalLayout_2.addWidget(self.custom_name_frame)

        self.retranslateUi(cell_control)
        QtCore.QMetaObject.connectSlotsByName(cell_control)

    def retranslateUi(self, cell_control):
        cell_control.setWindowTitle(_translate("cell_control", "Cell Control", None))
        self.custom_title_label.setText(_translate("cell_control", "unnamed", None))
        self.label.setText(_translate("cell_control", "Notes:", None))
        self.notesTextEdit.setToolTip(_translate("cell_control", "notes go here", None))
        self.notesTextEdit.setDocumentTitle(_translate("cell_control", "compare notes", None))

