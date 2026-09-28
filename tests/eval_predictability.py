"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitAMLWatch.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.structuring_smurfing_detector import *
from tools.transaction_velocity_monitor import *
from tools.sanctions_entity_screener import *

class TestGitAMLWatchPredictability(unittest.TestCase):

    def test_structuring_smurfing_detector(self):
        res = detect_structuring("[9500, 9700]")
        self.assertTrue(res["structuring_detected"])
        self.assertEqual(res["status"], "FLAG_SUSPICIOUS_STRUCTURING")

    def test_transaction_velocity_monitor(self):
        res = monitor_velocity(35000.0, 10000.0)
        self.assertTrue(res["anomaly"])
        self.assertEqual(res["status"], "VELOCITY_SPIKE_ALERT")

    def test_sanctions_entity_screener(self):
        res = screen_sanctions("Valid Corp International")
        self.assertFalse(res["sanction_match"])
        self.assertEqual(res["status"], "CLEAR")


if __name__ == "__main__":
    unittest.main()
