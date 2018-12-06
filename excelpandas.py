import pandas as pd

#xlrd
#openpyxl

excelfile = pd.ExcelFile('D:\\Downloads\\demo2.xlsx')
df = excelfile.parse('demo2')
print(df)
