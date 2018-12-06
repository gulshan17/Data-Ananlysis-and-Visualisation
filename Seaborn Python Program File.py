import pandas as pd
import seaborn as sns

dataset = pd.read_csv('f2m_ratios.csv', skiprows = 8)
#print(dataset)

pivot_table = pd.pivot_table(dataset, 'Ratio', 'Age', 'Year')
print(pivot_table)

figure = sns.heatmap(pivot_table).get_figure()

figure.savefig('Image file created by Seaborn.png')