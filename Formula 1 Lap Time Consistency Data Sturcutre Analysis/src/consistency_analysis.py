import pandas as pd
from scipy.stats import pearsonr

def perform_consistency_analysis(lap_times):
    correlation, _ = pearsonr(lap_times['milliseconds'], lap_times['position'])
    print(f"Pearson Correlation between lap time and position: {correlation}")

