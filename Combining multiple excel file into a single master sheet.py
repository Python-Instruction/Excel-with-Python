import pandas
  
df1 = pandas.read_excel("Student_details.xlsx")
df2 = pandas.read_excel("Marks.xlsx")
  
# merging the files
df3 = df1[["Roll No","Name",
"Email id"]].merge(df2[["Roll No","English", 
"Science", "History"]], on = "Roll No", how = "left")
  
# combining into single excel spreadsheet
df3.to_excel("Student_details_with_marks.xlsx", index = False)

