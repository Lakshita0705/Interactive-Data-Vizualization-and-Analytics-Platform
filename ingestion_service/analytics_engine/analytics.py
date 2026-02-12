import pandas as pd
import numpy as np

def analyze_trends():
    df = pd.read_csv("data/sample_health_data.csv")

    baseline_hr = df['resting_hr'].mean()
    baseline_sleep = df['sleep_hours'].mean()

    df['hr_deviation'] = df['resting_hr'] - baseline_hr
    df['sleep_deviation'] = df['sleep_hours'] - baseline_sleep

    df['risk_score'] = (
        0.5 * (df['hr_deviation']) -
        0.3 * (df['sleep_deviation'])
    )

    print("Trend Analysis Complete")
    print(df[['date', 'risk_score']])

    df.to_csv("data/processed_health_data.csv", index=False)

if __name__ == "__main__":
    analyze_trends()
