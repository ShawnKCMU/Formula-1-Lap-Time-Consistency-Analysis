import pandas as pd

def load_and_preprocess_data():

    lap_times = pd.read_csv('../data/lapTimes.csv')
    qualifying_times = pd.read_csv('../data/qualifying.csv')

    return lap_times, qualifying_times
