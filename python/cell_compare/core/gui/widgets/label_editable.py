import sys
from PyQt4 import QtGui, QtCore


class QLabelEditable(QtGui.QLabel):

    def __init__(self, parent=None):
        super(QLabelEditable, self).__init__(parent)

        # self.mouseDoubleClickEvent.clicked.connect()

    def mouseDoubleClickEvent(self, ev):
        print 'double licked'
        self.emit(QtCore.SIGNAL('clicked()'))

    def double_clicked(self):
        print 'double clicked'

def main():

    app = QtGui.QApplication([])
    ex = QLabelEditable()
    ex.show()
    ex.setText('< dclick to change me >')
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()