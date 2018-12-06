import pandas as pd
from pandas import DataFrame, read_html

#beautifulsoup4
#html5lib
#lxml

url = "https://www.countrycode.org/"
dflist = pd.io.html.read_html(url)
df = dflist[0]
print(dflist[1].columns)

print(df)

print(df.columns.values)