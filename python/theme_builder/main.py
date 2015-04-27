import sys
import os
import inspect
from PyQt4 import QtGui, QtCore

from theme_builder.ui.theme_tester import Ui_MainWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Set the QDir to the location of the compiled UI file so the icon paths are valid.
        for parent_class in self.__class__.mro():
            if parent_class.__name__.startswith('Ui_'):  # The compiled class always starts with Ui_
                gui_dir = os.path.dirname(inspect.getfile(parent_class))
                QtCore.QDir.setCurrent(gui_dir)

        # pass a theme dir here
        self.setStyleSheet(open(r'E:\Work\GitHub\mypytools\python\cell_compare\core\gui\themes\dark\dark.css').read())

        self.setupUi(self)

        self.toolBar.addWidget(QtGui.QPushButton())
        self.toolBar.addWidget(QtGui.QPushButton())
        self.toolBar.addWidget(QtGui.QPushButton())


def main():
    app = QtGui.QApplication(sys.argv)
    tt = MainWindow()
    tt.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()