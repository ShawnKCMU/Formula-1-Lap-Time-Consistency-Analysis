import unittest
import pandas as pd
from src.preprocessing import load_and_preprocess_data

class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        self.lap_times, self.qualifying_times = load_and_preprocess_data()

    def test_load_data_not_empty(self):
        self.assertFalse(self.lap_times.empty)
        self.assertFalse(self.qualifying_times.empty)

    def test_column_existence(self):
        required_columns = ['raceId', 'driverId', 'lap', 'position', 'time', 'milliseconds']
        for column in required_columns:
            self.assertIn(column, self.lap_times.columns)

    def test_no_null_values(self):
        self.assertFalse(self.lap_times.isnull().values.any())


if __name__ == '__main__':
    unittest.main()