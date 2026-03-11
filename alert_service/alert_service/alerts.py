def generate_alerts(df, baseline):
    alerts = []

    latest = df.iloc[-1]

    # Heart rate alert
    if latest["heart_rate"] > baseline["heart_rate"] * 1.15:
        alerts.append("⚠ Heart rate significantly above baseline")

    # Sleep alert
    if latest["sleep_hours"] < baseline["sleep_hours"] * 0.85:
        alerts.append("⚠ Sleep hours significantly below baseline")

    # Activity alert
    if latest["steps"] < baseline["steps"] * 0.7:
        alerts.append("⚠ Physical activity dropped significantly")

    return alerts
