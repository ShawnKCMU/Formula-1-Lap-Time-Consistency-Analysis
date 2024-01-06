from preprocessing import load_and_preprocess_data
from feature_engineering import calculate_features
from consistency_analysis import perform_consistency_analysis

def main():
    lap_times, qualifying_times = load_and_preprocess_data()

    lap_times = calculate_features(lap_times)

    perform_consistency_analysis(lap_times)

if __name__ == "__main__":
    main()

