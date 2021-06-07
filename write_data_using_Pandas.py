import pandas as pd

Roll = [1, 2, 3]
Name = ['Mickel', 'Ronit', 'Rohit']
Marks = [80, 68, 39]

df = pd.DataFrame({'Name':Name, 'Roll':Roll, 'Marks': Marks})

writer = pd.ExcelWriter('Student_Record2.xlsx')

df.to_excel(writer, sheet_name='sheet',header=True, index=False)

writer.save()


