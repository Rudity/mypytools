import time
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
        self._file = None

        self.file_watcher = QtCore.QFileSystemWatcher()
        self.file_watcher.fileChanged.connect(self._file_changed)

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
            self._file = file_diag

    def load_workbook_dropped(self, files_):
        if len(files_) == 1:
            self.populate_workbook_control(file_=files_[0])
            self._file = files_[0]

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

        if file_ not in self.file_watcher.files():
            self.file_watcher.addPath(file_)

    def set_cell_value(self):
        self.cell_value.setText(self.get_cell_value())
        self.compare_cell_values_signal.emit()

    def get_cell_value(self):
        return self.workbook.get_value(sheet_name=str(self.sheet_combobox.currentText()),
                                       row=self.row_spinBox.value(),
                                       column=self.column_spinBox.value())

    def _file_changed(self):
        for i in range(20):
            try:
                time.sleep(1.0)
                # print i
                self.workbook = WorkBook(file_=str(self._file))
                self.set_cell_value()
                # for f in self.file_watcher.files():
                #     print f
                break
            except:
                # TODO figure out how print how many times it tried to access file
                raise

    # def watch_file(self, file_):
    #     # paths = [os.path.dirname(os.path.realpath(file_)),
    #     #          os.path.realpath(file_)]
    #     # print paths
    #     self.file_watcher.addPath(file_)