from iu_assement_python.src.data_handler import DataHandler, TestDataHandler, TrainDataHandler, IdealDataHandler
from iu_assement_python.src.db_operation import AddTrainingDataToDB, AddIdealFunctionsToDB, AddMappedTestDataToDB
from src.process_data import DataOperations
def main():
    try:
        #Training Data
        training_data = TrainDataHandler('train.csv').data
        AddTrainingDataToDB().add_data(training_data)

        #Ideal Function Data
        ideal_function = IdealDataHandler('ideal.csv').data
        AddIdealFunctionsToDB().add_data(ideal_function)

        #Test data
        testing_data = TestDataHandler('test.csv').data
        mapped_data = DataOperations(training_data, ideal_function, testing_data).map_test_data_with_ideal_function()
        AddMappedTestDataToDB().add_data(mapped_data)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()