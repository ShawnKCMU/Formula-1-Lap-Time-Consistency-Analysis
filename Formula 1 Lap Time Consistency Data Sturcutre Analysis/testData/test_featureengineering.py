import unittest
import pandas as pd
from src.preprocessing import load_and_preprocess_data
from src.feature_engineering import calculate_average_lap_times, calculate_std_dev_lap_times

class TestFeatureEngineering(unittest.TestCase):

    def setUp(self):
        self.lap_times, _ = load_and_preprocess_data()

    def test_average_lap_times(self):
        lap_times_with_avg = calculate_average_lap_times(self.lap_times)
        self.assertIn('avg_lap_time', lap_times_with_avg.columns)
        # Check if average lap times are calculated correctly

    def test_std_dev_lap_times(self):
        lap_times_with_std = calculate_std_dev_lap_times(self.lap_times)
        self.assertIn('std_dev_lap_time', lap_times_with_std.columns)
        # Verify if standard deviations are calculated correctly


if __name__ == '__main__':
    unittest.main()