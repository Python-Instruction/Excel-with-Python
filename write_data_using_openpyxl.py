from openpyxl import Workbook    
wb = Workbook()  
sheet = wb.active  

sheet['A1'] ="Roll"   
sheet['A2'] = 1  
sheet['A3'] = 2  
sheet['A4'] = 3

sheet['B1'] ="Name"   
sheet['B2'] = "Mickel"  
sheet['B3'] = "Ronit"  
sheet['B4'] = "Rohit"

sheet['C1'] ="Marks"   
sheet['C2'] = 80 
sheet['C3'] = 68  
sheet['C4'] = 39
 
wb.save("Student_Record1.xlsx")