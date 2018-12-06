import pandas as pd
import numpy as np
from pandas import Series, DataFrame

cars = Series(['BMW', 'Jaguar', 'Porsche', 'Mercedes'], index = ['a', 'b', 'c', 'd'])
print(cars)

cars = cars.drop('d')
print(cars)

#dataframes
cars_df = DataFrame(np.arange(9).reshape(3, 3), index = ['BMW', 'Jaguar', 'Porsche'], columns = ['torque', 'HP', 'color'])
print(cars_df)

cars_df = cars_df.drop('BMW', axis = 0)
print(cars_df)

cars_df = cars_df.drop('color', axis = 1)
print(cars_df)