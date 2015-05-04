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

        list_model = QtGui.QStandardItemModel(self.listView)
        self.letters = ['A', 'B', 'C', 'D', 'E']
        for letter in self.letters:
            item = QtGui.QStandardItem(letter)
            item.setCheckable(True)
            list_model.appendRow(item)

        self.listView.setModel(list_model)
        self.listView_2.setModel(list_model)
        self.treeView.setModel(list_model)

        table_model = MyTableModel(self, DATA_LIST, HEADER)
        self.tableView.setModel(table_model)


class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        super(MyTableModel, self).__init__(parent)
        self.mylist = mylist
        self.header = header

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.mylist[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

# the solvent data ...
HEADER = ['Name', 'Height', 'Weight', 'Reach']
# use numbers for numeric data to sort properly
DATA_LIST = [('Dude', 180, 66, 68),
             ('Guy', 170, 64, 69),
             ('Friend', 172, 68, 74),
             ('Buddy', 187, 62, 70)]


def main():
    app = QtGui.QApplication(sys.argv)
    tt = MainWindow()
    tt.move(2040, 40)
    tt.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()