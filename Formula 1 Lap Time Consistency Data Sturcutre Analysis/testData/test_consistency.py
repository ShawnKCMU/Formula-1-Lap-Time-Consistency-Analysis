import unittest
import pandas as pd
from src.preprocessing import load_and_preprocess_data
from src.feature_engineering import calculate_average_lap_times, calculate_std_dev_lap_times
from src.consistency_analysis import perform_consistency_analysis

class TestConsistencyAnalysis(unittest.TestCase):

    def setUp(self):
        self.lap_times, _ = load_and_preprocess_data()
        self.lap_times = calculate_average_lap_times(self.lap_times)
        self.lap_times = calculate_std_dev_lap_times(self.lap_times)

    def test_pearson_correlation(self):
        correlation = perform_consistency_analysis(self.lap_times)
        self.assertIsNotNone(correlation)
        self.assertTrue(-1 <= correlation <= 1)

    def test_correlation_significance(self):
        correlation = perform_consistency_analysis(self.lap_times)
        self.assertTrue(abs(correlation) > 0.05)  # Example significance level

if __name__ == '__main__':
    unittest.main()