"""
structuring_smurfing_detector.py - Identifies sequential cash deposits structured just below the $10,000 CTR reporting threshold
"""
import sys
import json


def detect_structuring(deposits_json: str):
    import json
    amounts = json.loads(deposits_json) if isinstance(deposits_json, str) else deposits_json
    near_threshold = [a for a in amounts if 8500 <= a < 10000]
    total_amount = sum(amounts)
    is_smurfing = len(near_threshold) >= 2 or (len(near_threshold) >= 1 and total_amount >= 10000)
    return {
        "near_threshold_count": len(near_threshold),
        "total_amount": total_amount,
        "structuring_detected": is_smurfing,
        "status": "FLAG_SUSPICIOUS_STRUCTURING" if is_smurfing else "NORMAL"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "structuring-smurfing-detector"}))
