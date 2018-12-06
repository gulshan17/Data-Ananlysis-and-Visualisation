import pandas as pd

#apart from pandas library, also install xlrd, openpyxl

excelfile = pd.ExcelFile('Input File.xlsx')

for i in range(1, 11, 1) :
    df = excelfile.parse('Sheet' + str(i))
    df.to_csv('Sheet' + str(i) + '.csv')