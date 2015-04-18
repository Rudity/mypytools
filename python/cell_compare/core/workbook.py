import os

import xlrd


class WorkBook(object):

    def __init__(self, file_):

        self._file = file_
        self.name = os.path.basename(str(self._file))
        self.workbook = xlrd.open_workbook(self._file)
        self.sheets = [sheet.name for sheet in self.workbook.sheets()]

    def get_value(self, sheet_name, row, column):
        sheet = self.workbook.sheet_by_name(sheet_name)
        nrows = sheet.nrows
        ncols = sheet.ncols

        if nrows == 0 and ncols == 0:
            return '<Empty Sheet>'

        if nrows < row and ncols < column:
            return '<Max Rows and Columns Exceeded for {0}'.format(sheet.name)

        if nrows < row:
            return '<Max Rows Exceeded for {0}>'.format(sheet.name)

        if ncols < column:
            return '<Max Columns Exceeded for {0}>'.format(sheet.name)

        value = sheet.cell_value(rowx=row-1, colx=column-1)
        if isinstance(value, float):
            value = '{:,}'.format(value)  # adds a coma every 3rd zero if float
        return value