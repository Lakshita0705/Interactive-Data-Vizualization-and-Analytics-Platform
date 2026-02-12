import pandas as pd

def generate_alerts():
    df = pd.read_csv("data/processed_health_data.csv")

    threshold = 5

    df['alert'] = df['risk_score'].apply(
        lambda x: "⚠️ Elevated Risk" if x > threshold else "Normal"
    )

    print("Alerts Generated")
    print(df[['date', 'risk_score', 'alert']])

if __name__ == "__main__":
    generate_alerts()
