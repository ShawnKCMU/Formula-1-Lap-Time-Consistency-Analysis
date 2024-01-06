import pandas as pd

def calculate_average_lap_times(lap_times):
    avg_lap_times = lap_times.groupby(['raceId', 'driverId'])['milliseconds'].mean().reset_index()
    avg_lap_times.rename(columns={'milliseconds': 'avg_lap_time'}, inplace=True)
    
    return pd.merge(lap_times, avg_lap_times, on=['raceId', 'driverId'])

def calculate_std_dev_lap_times(lap_times):
    std_dev_lap_times = lap_times.groupby(['raceId', 'driverId'])['milliseconds'].std().reset_index()
    std_dev_lap_times.rename(columns={'milliseconds': 'std_dev_lap_time'}, inplace=True)
    
    return pd.merge(lap_times, std_dev_lap_times, on=['raceId', 'driverId'])