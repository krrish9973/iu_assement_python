import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error

training_data = pd.read_csv('train.csv')
ideal_function = pd.read_csv('ideal.csv')
test_data = pd.read_csv('test.csv')
print(test_data)

#Use of Training Data for Choosing Best Fit Ideal Function
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

max_deviation = {}
for y_column, ideal_column in best_fit_functions.items():
    max_deviation[y_column] = np.max(np.abs(training_data[y_column] - ideal_function[ideal_column]))

print(best_fit_functions)
print("Max Deviation")
print(max_deviation)

# Mapping the test data
mapped_test_data = []
count=0
for _, row in test_data.iterrows():
    print("Count = > ",count)
    x_test = row['x']
    print(x_test)
    y_test = row['y']
    best_fit = None
    min_deviation = float('inf')
    for y_column, ideal_column in best_fit_functions.items():
        print(y_column," ---> ",ideal_column)
        ideal_value = ideal_function[ideal_column].loc[ideal_function['x'] == x_test].values
        print(ideal_value)
        if len(ideal_value) == 0:
            continue
        deviation = np.abs(y_test - ideal_value[0])

        print("Before Comparing Deviation", deviation," Count ==> ",count)
        if deviation <= max_deviation[y_column] * np.sqrt(2):
            print("After Comparing Deviation", deviation," Count ==> ",count)
            min_deviation = deviation
            best_fit = ideal_column
            #mapped_test_data.append((x_test, y_test, best_fit, min_deviation))
    mapped_test_data.append({
        'x (test func)': x_test,
        'y (test func)': y_test,
        'Chosen Ideal Function': best_fit,
        'Deviation': min_deviation
        })
    count += 1

mapped_test_df = pd.DataFrame(mapped_test_data, columns=['x (test func)', 'y (test func)',
                                                         'Chosen Ideal Function', 'Deviation'])
print("Mapped Test DF\n",mapped_test_df.to_string())