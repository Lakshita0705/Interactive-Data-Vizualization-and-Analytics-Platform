import pandas as pd

def load_data():
    df = pd.read_csv("data/sample_health_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    print("Data Ingested Successfully")
    print(df.head())
    return df

if __name__ == "__main__":
    load_data()
