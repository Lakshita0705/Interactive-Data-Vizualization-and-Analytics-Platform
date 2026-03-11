from ingestion_service.ingest import load_health_data
from analytics_service.trend_analysis import calculate_baseline, calculate_trends
from alert_service.alert_generator import generate_alerts

def main():

    file_path = "data/health_data.csv"

    # Load data
    df = load_health_data(file_path)

    if df is None:
        return

    # Baseline calculation
    baseline = calculate_baseline(df)

    print("\nBaseline Metrics")
    print(baseline)

    # Trend analysis
    trends = calculate_trends(df)

    print("\nHealth Trends")
    print(trends)

    # Generate alerts
    alerts = generate_alerts(df, baseline)

    print("\nAlerts")
    if alerts:
        for alert in alerts:
            print(alert)
    else:
        print("No alerts detected")


if __name__ == "__main__":
    main()
