import pandas as pd

class DataHandler:
    """Class for handling data loading and processing."""
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        """Loads data from a CSV file."""
        try:
            data = pd.read_csv(self.file_path)
        except FileNotFoundError as e:
            raise CustomFileNotFoundError(f"File not found: {self.file_path}") from e
        return data

class TrainDataHandler(DataHandler):
    """Class for handling training data."""
    def __init__(self, file_path):
        super().__init__(file_path)


class TestDataHandler(DataHandler):
    """Class for handling test data."""
    def __init__(self, file_path):
        super().__init__(file_path)

class IdealDataHandler(DataHandler):
    """Class for handling ideal data."""
    def __init__(self, file_path):
        super().__init__(file_path)

class CustomFileNotFoundError(Exception):
    """Exception raised when a file is not found."""
    pass

'''
from bokeh.plotting import figure, show
from bokeh.io import output_file

class Visualizer:
    """Class for visualizing data."""

    @staticmethod
    def plot_data(train_data, test_data):
        """Plots the training and test data using Bokeh."""
        p = figure(title="Data Visualization", x_axis_label='X', y_axis_label='Y')
        p.line(train_data['x'], train_data['y'], legend_label="Train Data", line_width=2)
        p.circle(test_data['x'], test_data['y'], legend_label="Test Data", fill_color="red", size=6)
        output_file("data_visualization.html")
        show(p)
File: src/database.py
python
Copy code
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class DataPoint(Base):
    """Class for a data point in the database."""
    __tablename__ = 'data_points'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)
    dataset_type = Column(String)

class DatabaseHandler:
    """Class for handling database operations."""

    def __init__(self, db_url='sqlite:///data.db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_data_point(self, x, y, dataset_type):
        """Adds a data point to the database."""
        session = self.Session()
        data_point = DataPoint(x=x, y=y, dataset_type=dataset_type)
        session.add(data_point)
        session.commit()
        session.close()

    def get_all_data_points(self):
        """Retrieves all data points from the database."""
        session = self.Session()
        data_points = session.query(DataPoint).all()
        session.close()
        return data_points
'''