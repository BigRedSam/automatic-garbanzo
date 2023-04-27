import openpyxl

workbook = openpyxl.load_workbook('ITEC_Courses.xlsx')

sheet_names = workbook.sheetnames
print(sheet_names)