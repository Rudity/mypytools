"""
playing with stuffs

"""

import xlrd

# our whole workboox stored in the workbook variable
workbook = xlrd.open_workbook(r'E:\Kelsea\2014 Q4 Financial Statements (IGO) copy.xls')

# balance sheet information
balance_sheet = workbook.sheet_by_name('Balance Sheet')
bs_label = balance_sheet.cell_value(rowx=10, colx=1)
bs_value = balance_sheet.cell_value(rowx=10, colx=4)


row = 100
col = 100
statement_of_cash_flows = workbook.sheet_by_name('Statement of Cash Flows')
print statement_of_cash_flows.nrows
socf_label = statement_of_cash_flows.cell_value(rowx=row, colx=0)
socf_value = statement_of_cash_flows.cell_value(rowx=row, colx=3)


if bs_value == socf_value:
    print 'Y: {2}    {0} -> {1}'.format(balance_sheet.name, bs_label, bs_value)
    print '   {2}    {0} -> {1}'.format(balance_sheet.name, socf_label, socf_value)
else:
    print 'N: {2}    {0} -> {1}'.format(statement_of_cash_flows.name, bs_label, bs_value)
    print '   {2}    {0} -> {1}'.format(statement_of_cash_flows.name, socf_label, socf_value)