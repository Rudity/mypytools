from PyQt4 import QtGui, QtCore

__author__ = 'mfacer'


class DropButton(QtGui.QPushButton):
    """
    Custom button that will accept drag and drop events.
    """
    dropped = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super(DropButton, self).__init__(parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.dropped.emit(links)

        else:
            event.ignore()
