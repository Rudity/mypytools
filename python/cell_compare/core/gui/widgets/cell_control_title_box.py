import sys
from PyQt4 import QtGui, QtCore, Qt


class CellControlTitleBox(QtGui.QFrame):

    def __init__(self, parent=None):
        super(CellControlTitleBox, self).__init__(parent)

        self._parent = parent

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw_lines(qp)
        qp.end()

    def draw_lines(self, qp):
        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(0, 20, 200, 20)

def main():

    app = QtGui.QApplication([])
    ex = CellControlTitleBox()
    ex.setGeometry(1350, 300, 200, 200)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()