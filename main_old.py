import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from database import engine, Base, session
from iu_assement_python.src.models.training_data import TrainingData
from iu_assement_python.src.models.ideal_function import IdealFunction
from iu_assement_python.src.models.test_data import TestData

"""
A study of the relationship between the number of ideal functions considered and the accuracy of 
regression models generated using training data.
"""


training_data = pd.read_csv('train.csv')
ideal_function = pd.read_csv('ideal.csv')
test_data = pd.read_csv('test.csv')


#Use of Training Data for Choosing Best Fit Ideal Function
def find_best_fit_functions(training_data, ideal_function):
    best_fit_functions = {}
    for y_column in training_data.columns[1:]:
        best_fit = None
        min_error = float('inf')
        for ideal_column in ideal_function.columns[1:]:
            mse = mean_squared_error(training_data[y_column], ideal_function[ideal_column])
            if mse < min_error:
                min_error = mse
                best_fit = ideal_column
        best_fit_functions[y_column] = best_fit
    return best_fit_functions

def find_max_deviations(best_fit_functions):
    max_deviation = {}
    for y_column, ideal_column in best_fit_functions.items():
        max_deviation[y_column] = np.max(np.abs(training_data[y_column] - ideal_function[ideal_column]))
    return max_deviation

def map_test_data_with_ideal_function(training_data,ideal_function, test_data):
    mapped_test_data = []
    best_fit_functions = find_best_fit_functions(training_data, ideal_function)
    max_deviation = find_max_deviations(best_fit_functions)
    for _, row in test_data.iterrows():
        x_test = row['x']
        y_test = row['y']
        best_fit = None
        min_deviation = float('inf')
        for y_column, ideal_column in best_fit_functions.items():
            ideal_value = ideal_function[ideal_column].loc[ideal_function['x'] == x_test].values
            if len(ideal_value) == 0:
                continue
            deviation = np.abs(y_test - ideal_value[0])
            if deviation <= max_deviation[y_column] * np.sqrt(2):
                min_deviation = deviation
                best_fit = ideal_column
        mapped_test_data.append({
            'x': x_test,
            'y': y_test,
            'ideal_function_id': best_fit,
            'deviation': min_deviation
        })
    return mapped_test_data

# Save Data to Database
Base.metadata.create_all(engine)
for index, row in training_data.iterrows():
    session.merge(TrainingData(x=row['x'], y1=row['y1'], y2=row['y2'], y3=row['y3'], y4=row['y4']))

for index,row in ideal_function.iterrows():
    session.merge(IdealFunction(x=row['x'], y1=row['y1'], y2=row['y2'],y3=row['y3'],y4=row['y4'],y5=row['y5'],
                              y6=row['y6'], y7=row['y7'],y8=row['y8'],y9=row['y9'],y10=row['y10'],
                              y11=row['y11'],
                              y12=row['y12'],
                              y13=row['y13'],
                              y14=row['y14'],
                              y15=row['y15'],
                              y16=row['y16'],
                              y17=row['y17'],
                              y18=row['y18'],
                              y19=row['y19'],
                              y20=row['y20'],
                              y21=row['y21'],
                              y22=row['y22'],
                              y23=row['y23'],
                              y24=row['y24'],
                              y25=row['y25'],
                              y26=row['y26'],
                              y27=row['y27'],
                              y28=row['y28'],
                              y29=row['y29'],
                              y30=row['y30'],
                              y31=row['y31'],
                              y32=row['y32'],
                              y33=row['y33'],
                              y34=row['y34'],
                              y35=row['y35'],
                              y36=row['y36'],
                              y37=row['y37'],
                              y38=row['y38'],
                              y39=row['y39'],
                              y40=row['y40'],
                              y41=row['y41'],
                              y42=row['y42'],
                              y43=row['y43'],
                              y44=row['y44'],
                              y45=row['y45'],
                              y46=row['y46'],
                              y47=row['y47'],
                              y48=row['y48'],
                              y49=row['y49'],
                              y50=row['y50']
                              ))

mapped_test_data = map_test_data_with_ideal_function(training_data, ideal_function, test_data)
for row in mapped_test_data:
    session.merge(TestData(x=row['x'], y=row['y'], ideal_function_id=row['ideal_function_id'],
                         deviation=row['deviation']))
session.commit()