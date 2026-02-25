import pandas as pd
import numpy as np
import pickle
import sys

# Load saved model, scaler, and features
with open("isolation_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("features.pkl", "rb") as f:
    features = pickle.load(f)

# Preprocessing + Feature Engineering Function
def preprocess(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    df = df.sort_values(['station_id', 'session_id', 'timestamp']).reset_index(drop=True)

    

    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)

    df['power_expected'] = df['voltage'] * df['current'] / 1000
    df['power_deviation'] = abs(df['power_kw'] - df['power_expected'])

    df['energy_expected'] = df['power_kw'] * df['duration_sec'] / 3600
    df['energy_deviation'] = abs(df['energy_kwh'] - df['energy_expected'])

    # Rolling features
    df['rolling_power_mean'] = df.groupby(
        ['station_id', 'session_id']
    )['power_kw'].transform(
        lambda x: x.rolling(window=5, min_periods=1).mean()
    )

    df['rolling_power_std'] = df.groupby(
        ['station_id', 'session_id']
    )['power_kw'].transform(
        lambda x: x.rolling(window=5, min_periods=1).std()
    ).fillna(0)

    df['rolling_temp_mean'] = df.groupby(
        ['station_id', 'session_id']
    )['temperature_c'].transform(
        lambda x: x.rolling(window=5, min_periods=1).mean()
    )

    df['rolling_temp_std'] = df.groupby(
        ['station_id', 'session_id']
    )['temperature_c'].transform(
        lambda x: x.rolling(window=5, min_periods=1).std()
    ).fillna(0)

    # Delta features

    df['power_delta'] = df.groupby(
        ['station_id', 'session_id']
    )['power_kw'].diff().fillna(0)

    df['temp_delta'] = df.groupby(
        ['station_id', 'session_id']
    )['temperature_c'].diff().fillna(0)

    df['voltage_delta'] = df.groupby(
        ['station_id', 'session_id']
    )['voltage'].diff().fillna(0)


    station_power_mean = df.groupby('station_id')['power_kw'].transform('mean')
    df['station_power_deviation'] = abs(df['power_kw'] - station_power_mean)

    station_temp_mean = df.groupby('station_id')['temperature_c'].transform('mean')
    df['station_temp_deviation'] = abs(df['temperature_c'] - station_temp_mean)

    df['session_total_energy'] = df.groupby('session_id')['energy_kwh'].transform('sum')

    df['session_total_duration'] = df.groupby('session_id')['duration_sec'].transform('sum')

    df = df.fillna(df.median(numeric_only=True))
    df = df.fillna(0)
    
    return df

def predict(input_csv, output_csv):

    # Load data
    df = pd.read_csv(input_csv)

    original_cols = df.columns.tolist()

    df = preprocess(df)
    X = df[features]

    X_scaled = scaler.transform(X)

    # Predict anomalies
    preds = model.predict(X_scaled)
    df['is_anomaly'] = np.where(preds == -1, 1, 0)

    # Hardware error
    if 'error_code' in df.columns:
        df.loc[df['error_code'] != 0, 'is_anomaly'] = 1

    # Physics violation override
    physics_violation = (
        (df['power_kw'] < 0) |
        (df['energy_kwh'] < 0) |
        (df['voltage'] <= 0) |
        (df['current'] < 0) |
        (df['duration_sec'] <= 0)
    )
    df.loc[physics_violation, 'is_anomaly'] = 1

    columns_to_keep = original_cols + ['is_anomaly']
    df_final = df[columns_to_keep]

    df_final.to_csv(output_csv, index=False)

    # Print summary
    print("Prediction complete.")
    print(f"Output saved to: {output_csv}")
    print(f"Total rows: {len(df_final)}")
    print(f"Total anomalies detected: {df_final['is_anomaly'].sum()}")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python predict.py input.csv")
        sys.exit(1)

    input_csv = sys.argv[1]

    output_csv = input_csv.replace(".csv", "_output.csv")

    predict(input_csv, output_csv)