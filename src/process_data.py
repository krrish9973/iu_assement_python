import numpy as np
from sklearn.metrics import mean_squared_error
class DataOperations:
    def __init__(self, training_data, ideal_function, test_data):
        self.training_data = training_data
        self.ideal_function = ideal_function
        self.test_data = test_data
        self.best_fit_functions = self.find_best_fit_functions()
        self.max_deviation = self.find_max_deviations(self.best_fit_functions)

    def find_best_fit_functions(self):
        best_fit_functions = {}
        for y_column in self.training_data.columns[1:]:
            best_fit = None
            min_error = float('inf')
            for ideal_column in self.ideal_function.columns[1:]:
                mse = mean_squared_error(self.training_data[y_column], self.ideal_function[ideal_column])
                if mse < min_error:
                    min_error = mse
                    best_fit = ideal_column
            best_fit_functions[y_column] = best_fit
        return best_fit_functions

    def find_max_deviations(self, best_fit_functions):
        max_deviation = {}
        for y_column, ideal_column in best_fit_functions.items():
            max_deviation[y_column] = np.max(np.abs(self.training_data[y_column] -
                                                    self.ideal_function[ideal_column]))
        return max_deviation

    def map_test_data_with_ideal_function(self):
        mapped_test_data = []
        for _, row in self.test_data.iterrows():
            x_test = row['x']
            y_test = row['y']
            best_fit = None
            min_deviation = None
            for y_column, ideal_column in self.best_fit_functions.items():
                ideal_value = self.ideal_function[ideal_column].loc[self.ideal_function['x'] == x_test].values
                if len(ideal_value) == 0:
                    continue
                deviation = np.abs(y_test - ideal_value[0])
                if deviation <= self.max_deviation[y_column] * np.sqrt(2):
                    min_deviation = deviation
                    best_fit = ideal_column
            mapped_test_data.append({
                'x': x_test,
                'y': y_test,
                'ideal_function_id': best_fit,
                'deviation': min_deviation
            })
        return mapped_test_data