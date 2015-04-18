import sys
import string
from PyQt4 import QtGui, QtCore


class QSpinBoxExcelColumnTitle(QtGui.QSpinBox):

    def __init__(self, parent=None):
        super(QSpinBoxExcelColumnTitle, self).__init__(parent)

        self._parent = parent
        self.validator = QtGui.QRegExpValidator(QtCore.QRegExp('[A-Z]+'), self)
        self._excel_column_titles = []
        self._values = {}

        #  set to default min/max when instancing
        self.create_column_title_list(self.maximum())
        self._values = dict(zip(self._excel_column_titles, range(len(self._excel_column_titles))))

    def textFromValue(self, value):
        return self._excel_column_titles[value]

    def valueFromText(self, text):
        text = str(text)
        if text in self._values.keys():
            return self._values[text]
        return self.value()

    def validate(self, text, pos):
        return self.validator.validate(text, pos)

    def setRange(self, p_int, p_int_1):
        self.setMinimum(p_int)
        self.setMaximum(p_int_1)

    def setMaximum(self, p_int):
        super(QSpinBoxExcelColumnTitle, self).setMaximum(p_int)
        self.create_column_title_list(p_int)

    def create_column_title_list(self, _max):
        """
        creates a list of column titles that match excel convention
        ['', 'A', 'B', 'C', 'D']

        :param _max:
        :type _max: int
        :return: list of column titles you would expect from an excel spread sheet
        :rtype: list
        """

        def column_title(num):
            title = ''
            alphabet = string.uppercase
            while num:
                mod = (num-1) % 26
                num = int((num - mod) / 26)
                title += alphabet[mod]
            return title[::-1]

        excel_column_titles = []
        for i in range(0, _max+1):  # add to our max range to match title list len
            excel_column_titles.append(column_title(i))

        self._excel_column_titles = excel_column_titles


def main():

    app = QtGui.QApplication([])
    ex = QSpinBoxExcelColumnTitle()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
