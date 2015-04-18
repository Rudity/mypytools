import sys
import os
from PyQt4 import QtGui

import cell_compare.core.gui.main_window


def main():
    app = QtGui.QApplication(sys.argv)
    # css_file = open('../themes/dark_pink.css').read()
    cc = cell_compare.core.gui.main_window.MainWindow()
    # cc.setStyleSheet(css_file)
    cc.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()