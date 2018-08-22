from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference, Series

wb = Workbook()
sheet = wb.active
# Create some email_data in the column A.
for i in range(1, 11):
    sheet[f'A{str(i)}'] = i

# Create some email_data in the column B.
nums = []
for i in range(10, 0, -1):
    nums.append(i)
for i, j in list(enumerate(nums, start=1)):
    sheet[f'B{i}'] = j

# First rectangular selection for a first series.
ref_obj_1 = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
ref_obj_2 = Reference(sheet, min_col=2, min_row=1, max_col=2, max_row=10)

# First series of email_data from the selection and its name 'First series' (it will be displayed in the chart legend).
series_obj_1 = Series(ref_obj_1, title='First series')
series_obj_2 = Series(ref_obj_2, title='Second series')

# Create a chart
chart_obj = BarChart()
chart_obj.title = 'My Chart'  # Top of the chart.
chart_obj.append(series_obj_1)
chart_obj.append(series_obj_2)
sheet.add_chart(chart_obj, 'D5')  # 'C5' is the anchor of the chart (the from_top-from_left corner).
wb.save('sample_chart.xlsx')


"""
OpenPyXL supports creating bar, line, scatter, and pie charts using the email_data in a sheet’s cells. 
To make a chart, you need to do the following:

Create a Reference object from a rectangular selection of cells.
Create a Series object by passing in the Reference object.
Create a Chart object.
Append the Series object to the Chart object.
Add the Chart object to the Worksheet object, 
optionally specifying which cell the from_top from_left corner of the chart should be positioned.

"""