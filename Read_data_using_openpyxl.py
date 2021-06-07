
import openpyxl
path = "Student_Record1.xlsx"
wb = openpyxl.load_workbook(path)
sheet = wb.active
for row in sheet:
    print([data.value for data in row])


    