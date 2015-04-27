# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Work\GitHub\mypytools\python\cell_compare\core\gui\ui\workbook_control.ui'
#
# Created: Sun Apr 26 17:40:49 2015
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

class Ui_workbook(object):
    def setupUi(self, workbook):
        workbook.setObjectName(_fromUtf8("workbook"))
        workbook.resize(439, 52)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(workbook.sizePolicy().hasHeightForWidth())
        workbook.setSizePolicy(sizePolicy)
        workbook.setMaximumSize(QtCore.QSize(16777215, 52))
        self.horizontalLayout = QtGui.QHBoxLayout(workbook)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.a_horizontalLayout = QtGui.QHBoxLayout()
        self.a_horizontalLayout.setSpacing(2)
        self.a_horizontalLayout.setObjectName(_fromUtf8("a_horizontalLayout"))
        self.load_workbook = DropButton(workbook)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_workbook.sizePolicy().hasHeightForWidth())
        self.load_workbook.setSizePolicy(sizePolicy)
        self.load_workbook.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/excel_imports.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.load_workbook.setIcon(icon)
        self.load_workbook.setObjectName(_fromUtf8("load_workbook"))
        self.a_horizontalLayout.addWidget(self.load_workbook)
        self.sheet_combobox = QtGui.QComboBox(workbook)
        self.sheet_combobox.setEnabled(False)
        self.sheet_combobox.setObjectName(_fromUtf8("sheet_combobox"))
        self.a_horizontalLayout.addWidget(self.sheet_combobox)
        self.verticalLayout.addLayout(self.a_horizontalLayout)
        self.b_horizontalLayout = QtGui.QHBoxLayout()
        self.b_horizontalLayout.setSpacing(2)
        self.b_horizontalLayout.setObjectName(_fromUtf8("b_horizontalLayout"))
        self.row_label = QtGui.QLabel(workbook)
        self.row_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.row_label.setObjectName(_fromUtf8("row_label"))
        self.b_horizontalLayout.addWidget(self.row_label)
        self.row_spinBox = QtGui.QSpinBox(workbook)
        self.row_spinBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row_spinBox.sizePolicy().hasHeightForWidth())
        self.row_spinBox.setSizePolicy(sizePolicy)
        self.row_spinBox.setWrapping(False)
        self.row_spinBox.setMinimum(1)
        self.row_spinBox.setMaximum(150)
        self.row_spinBox.setObjectName(_fromUtf8("row_spinBox"))
        self.b_horizontalLayout.addWidget(self.row_spinBox)
        self.column_label = QtGui.QLabel(workbook)
        self.column_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.column_label.setObjectName(_fromUtf8("column_label"))
        self.b_horizontalLayout.addWidget(self.column_label)
        self.column_spinBox = QSpinBoxExcelColumnTitle(workbook)
        self.column_spinBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.column_spinBox.sizePolicy().hasHeightForWidth())
        self.column_spinBox.setSizePolicy(sizePolicy)
        self.column_spinBox.setWrapping(True)
        self.column_spinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.column_spinBox.setMinimum(1)
        self.column_spinBox.setMaximum(75)
        self.column_spinBox.setObjectName(_fromUtf8("column_spinBox"))
        self.b_horizontalLayout.addWidget(self.column_spinBox)
        self.cell_value = QtGui.QLabel(workbook)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cell_value.setFont(font)
        self.cell_value.setObjectName(_fromUtf8("cell_value"))
        self.b_horizontalLayout.addWidget(self.cell_value)
        self.notes_lineedit = QtGui.QLineEdit(workbook)
        self.notes_lineedit.setEnabled(True)
        self.notes_lineedit.setObjectName(_fromUtf8("notes_lineedit"))
        self.b_horizontalLayout.addWidget(self.notes_lineedit)
        self.verticalLayout.addLayout(self.b_horizontalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.add_workbook_control = QtGui.QPushButton(workbook)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_workbook_control.sizePolicy().hasHeightForWidth())
        self.add_workbook_control.setSizePolicy(sizePolicy)
        self.add_workbook_control.setMinimumSize(QtCore.QSize(22, 0))
        self.add_workbook_control.setMaximumSize(QtCore.QSize(16777215, 22))
        self.add_workbook_control.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/report_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_workbook_control.setIcon(icon1)
        self.add_workbook_control.setObjectName(_fromUtf8("add_workbook_control"))
        self.verticalLayout_2.addWidget(self.add_workbook_control)
        self.remove_workbook_control = QtGui.QPushButton(workbook)
        self.remove_workbook_control.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_workbook_control.sizePolicy().hasHeightForWidth())
        self.remove_workbook_control.setSizePolicy(sizePolicy)
        self.remove_workbook_control.setMinimumSize(QtCore.QSize(22, 0))
        self.remove_workbook_control.setMaximumSize(QtCore.QSize(16777215, 22))
        self.remove_workbook_control.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/report_delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_workbook_control.setIcon(icon2)
        self.remove_workbook_control.setIconSize(QtCore.QSize(16, 16))
        self.remove_workbook_control.setObjectName(_fromUtf8("remove_workbook_control"))
        self.verticalLayout_2.addWidget(self.remove_workbook_control)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(workbook)
        QtCore.QMetaObject.connectSlotsByName(workbook)

    def retranslateUi(self, workbook):
        workbook.setWindowTitle(_translate("workbook", "Form", None))
        self.load_workbook.setText(_translate("workbook", "load workbook", None))
        self.row_label.setText(_translate("workbook", "Row", None))
        self.column_label.setText(_translate("workbook", "Column", None))
        self.cell_value.setText(_translate("workbook", "<Load Workbook>", None))

from cell_compare.core.gui.widgets.dropbutton import DropButton
from cell_compare.core.gui.widgets.spinbox_excel_column_title import QSpinBoxExcelColumnTitle
