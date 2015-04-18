from PyQt4 import QtGui, QtCore

from cell_compare.core.gui.ui.workbook_control import Ui_workbook
from cell_compare.core.workbook import WorkBook


class WorkbookControl(QtGui.QWidget, Ui_workbook):

    add_workbook_signal = QtCore.pyqtSignal(object)
    remove_workbook_signal = QtCore.pyqtSignal(object)
    compare_cell_values_signal = QtCore.pyqtSignal()

    excel_files = ['.xls', '.xlsx', '.csv']

    def __init__(self, parent=None):
        super(WorkbookControl, self).__init__()
        self.setupUi(self)

        self._parent = parent
        self.workbook = None

        self.load_workbook.clicked.connect(self.load_workbook_pressed)
        self.load_workbook.dropped.connect(self.load_workbook_dropped)
        self.remove_workbook_control.clicked.connect(self.remove_workbook_control_pressed)
        self.add_workbook_control.clicked.connect(self.add_workbook_control_pressed)
        self.row_spinBox.valueChanged.connect(self.set_cell_value)
        self.column_spinBox.valueChanged.connect(self.set_cell_value)

    def remove_workbook_control_pressed(self):
        self.remove_workbook_signal.emit(self)
        self.compare_cell_values_signal.emit()

    def add_workbook_control_pressed(self):
        self.add_workbook_signal.emit(self)
        self.compare_cell_values_signal.emit()

    def open_excel_dialog(self):
        filter_ = 'Excel files ({})'.format(' '.join(self.excel_files).replace('.', '*.'))
        return QtGui.QFileDialog.getOpenFileName(None, caption="Open Excel File...",
                                                 filter=filter_)

    def load_workbook_pressed(self):
        file_diag = self.open_excel_dialog()
        if file_diag:
            self.populate_workbook_control(file_=file_diag)

    def load_workbook_dropped(self, files_):
        if len(files_) == 1:
            self.populate_workbook_control(file_=files_[0])

    def populate_workbook_control(self, file_):

        self.workbook = WorkBook(file_=str(file_))

        # setting combo box stuff. Have to discconnect before clear and add so it doesn't trigger
        try:
            self.sheet_combobox.currentIndexChanged.disconnect(self.set_cell_value)
        except Exception:
            pass

        self.sheet_combobox.setEnabled(True)
        self.sheet_combobox.clear()
        self.sheet_combobox.addItems(self.workbook.sheets)
        self.sheet_combobox.currentIndexChanged.connect(self.set_cell_value)

        self.load_workbook.setText(self.workbook.name)
        self.row_spinBox.setEnabled(True)
        self.column_spinBox.setEnabled(True)

        self.set_cell_value()

    def set_cell_value(self):
        self.cell_value.setText(self.get_cell_value())
        self.compare_cell_values_signal.emit()

    def get_cell_value(self):
        return self.workbook.get_value(sheet_name=str(self.sheet_combobox.currentText()),
                                       row=self.row_spinBox.value(),
                                       column=self.column_spinBox.value())
