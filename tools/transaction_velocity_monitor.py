"""
transaction_velocity_monitor.py - Calculates transaction volume velocity spikes against historical 90-day moving average
"""
import sys
import json


def monitor_velocity(daily_volume: float, moving_average_90d: float = 10000.0):
    ratio = daily_volume / max(moving_average_90d, 1.0)
    is_spike = ratio >= 3.0
    return {
        "daily_volume": daily_volume,
        "moving_average": moving_average_90d,
        "velocity_ratio": round(ratio, 2),
        "anomaly": is_spike,
        "status": "VELOCITY_SPIKE_ALERT" if is_spike else "NORMAL_VELOCITY"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "transaction-velocity-monitor"}))
