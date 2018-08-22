
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active

for cell_obj in tuple(sheet.columns)[1]:  # difference - needed to change to tuple() from the 'generator' object
    print(cell_obj.value)
