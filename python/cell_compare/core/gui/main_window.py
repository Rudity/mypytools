import os
import inspect
from PyQt4 import QtGui, QtCore

from cell_compare.core.gui.ui.main_window import Ui_compare_cell
from cell_compare.core.gui.cell_control import CellControl


class MainWindow(QtGui.QMainWindow, Ui_compare_cell):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Set the QDir to the location of the compiled UI file so the icon paths are valid.
        for parent_class in self.__class__.mro():
            if parent_class.__name__.startswith('Ui_'):  # The compiled class always starts with Ui_
                gui_dir = os.path.dirname(inspect.getfile(parent_class))
                QtCore.QDir.setCurrent(gui_dir)

        self.setStyleSheet(open('../themes/dark/dark.css').read())
        self.setupUi(self)

        self.cell_controls = []

        self.scroll_vertical_layout.setAlignment(QtCore.Qt.AlignTop)
        self.add_cell_control_button.clicked.connect(self.add_cell_control_pressed)

        self.scrollArea.customContextMenuRequested.connect(self._on_context_menu)
        self.popMenu = QtGui.QMenu(self)
        self.popMenu.addAction('add compare cell block', self.add_cell_control_pressed)

        #temp code remove
        for i in range(0, 6):
            self.add_cell_control_pressed()

    def _on_context_menu(self, point):
        self.popMenu.exec_(self.scrollArea.mapToGlobal(point))

    def add_cell_control_pressed(self):
        cc = CellControl()
        cc.remove_cell_control_signal.connect(self.remove_cell_control)
        self.scroll_vertical_layout.addWidget(cc)
        self.cell_controls.append(cc)

    def remove_cell_control(self, cell_control):
        """

        :param cell_control: cell control object
        :type cell_control: CellControl
        :return:
        :rtype:
        """
        self.cell_controls.remove(cell_control)
        cell_control.setParent(None)