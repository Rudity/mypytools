import functools
from PyQt4 import QtGui, QtCore

from cell_compare.core.gui.ui.cell_control import Ui_cell_control
from cell_compare.core.gui.workbook_control import WorkbookControl


class CellControl(QtGui.QWidget, Ui_cell_control):

    remove_cell_control_signal = QtCore.pyqtSignal(object)

    def __init__(self, n_workbooks=2):
        super(CellControl, self).__init__()
        self.setupUi(self)

        self._n_workbooks = n_workbooks
        self._workbook_controls = []
        self._add_starting_workbook_controls()

        self._create_conext_menu()

    def _create_conext_menu(self):
        self.custom_name_frame.customContextMenuRequested.connect(self._on_context_menu)
        self.popMenu = QtGui.QMenu(self)
        self.popMenu.addAction('delete compare block', self.remove_cell_control_pressed)

    def _on_context_menu(self, point):
        self.popMenu.exec_(self.custom_name_frame.mapToGlobal(point))

    def _add_starting_workbook_controls(self):
        for i in range(0, self._n_workbooks):
            self.add_workbook_control(WorkbookControl)

    def _add_ordered_workbook_controls(self):
        for wbc in self._workbook_controls or []:
            self.contols_verticalLayout.addWidget(wbc)

    def remove_cell_control_pressed(self):
        self.remove_cell_control_signal.emit(self)

    def _get_wbc_index(self, wbc):
        """
        gets index our workbook control object is at in the vertical layout

        :param wbc: pass a workbook control object
        :type wbc: WorkbookControl
        :return: index
        :rtype: int
        """
        index = 0
        for i, control in enumerate(self._workbook_controls):
            if control == wbc:
                index = i
        return index

    def add_workbook_control(self, workbook_control):
        """
        :param workbook_control: pass a workbook control object
        :type workbook_control: WorkbookControl
        :return:
        :rtype: None
        """
        wbc = WorkbookControl()
        wbc.add_workbook_signal.connect(self.add_workbook_control)
        wbc.remove_workbook_signal.connect(self.remove_workbook_control)
        wbc.compare_cell_values_signal.connect(self.compare_cell_values)
        wbc_index = self._get_wbc_index(workbook_control)
        self._workbook_controls.insert(wbc_index + 1, wbc)  # +1 to insert after index
        self._add_ordered_workbook_controls()
        self.disable_remove_workbook_button()

    def remove_workbook_control(self, workbook_control):
        """
        :param workbook_control: pass a workbook control object
        :type workbook_control: WorkbookControl
        :return:
        :rtype: None
        """
        self._workbook_controls.remove(workbook_control)
        workbook_control.setParent(None)
        self.disable_remove_workbook_button()

    def get_workbook_controls(self):
        return [self.contols_verticalLayout.itemAt(i) for i in range(self.contols_verticalLayout.count())]

    def disable_remove_workbook_button(self):
        disable = False
        if len(self._workbook_controls) > 2:
            disable = True

        for control in self._workbook_controls:
            control.remove_workbook_control.setEnabled(disable)

    def compare_cell_values(self):
        """
        Compare cell values from our QLabel and sets icons accordingly for our cell control
        :rtype: None
        """
        comparable_values = []
        for workbook in self._workbook_controls:
            if workbook.workbook:  # check if workbook control has workbook loaded
                comparable_values.append(str(workbook.cell_value.text()))

        if len(comparable_values) >= 2:
            self.cell_match_icon.setPixmap(QtGui.QPixmap("../icons/cancel.png"))
            if comparable_values[1:] == comparable_values[:-1]:  # compare items in list
                self.cell_match_icon.setPixmap(QtGui.QPixmap("../icons/accept_button.png"))
        else:
            self.cell_match_icon.setPixmap(QtGui.QPixmap("../icons/ask_and_answer.png"))