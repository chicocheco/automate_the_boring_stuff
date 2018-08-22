
import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
print(wb.sheetnames)        # before 'wb.get_sheet_names()'

sheet = wb['Sheet3']        # before wb.get_sheet_by_name('Sheet1')
print(sheet.title)
