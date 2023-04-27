import openpyxl

workbook = openpyxl.load_workbook('ITEC_Courses.xlsx')

# sheet_names = workbook.sheetnames
# print(sheet_names)

names_sheet = workbook.active

# b2_data = names_sheet['B2'].value
# print(f'Cell B2 contains {b2_data}')

# c5_data = names_sheet['C5'].value
# print(f"Cell C5 contains {c5_data}")

# rows = names_sheet.rows
# for row in rows:
#     for cell in row:
#         print(cell.value)

# columns = names_sheet.columns

# for col in columns:
#     for cell in col:
#         print(cell.value)

# columns_list = list(names_sheet.columns)

# class_code_column = columns_list[1]

# for code_cell in class_code_column:
#     print(code_cell.value)

rooms_sheet = workbook['rooms']
rooms_columns = rooms_sheet.columns

for column in rooms_columns:
    for cell in column:
        print(cell.value)