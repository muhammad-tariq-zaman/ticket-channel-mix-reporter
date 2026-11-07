import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import report

def row(t, c):
    return {"ticket": t, "channel": c}

class TestChannelMix(unittest.TestCase):
    def test_counts(self):
        r = report([row("T1", "email"), row("T2", "email"), row("T3", "phone")])
        self.assertEqual(dict((c, n) for c, n, _ in r)["email"], 2)
    def test_share(self):
        r = report([row("T1", "email"), row("T2", "phone")])
        self.assertAlmostEqual(dict((c, s) for c, _, s in r)["email"], 0.5)
    def test_largest_first(self):
        r = report([row("T1", "phone"), row("T2", "email"), row("T3", "email")])
        self.assertEqual(r[0][0], "email")
    def test_case_insensitive(self):
        r = report([row("T1", "Email"), row("T2", "EMAIL")])
        self.assertEqual(len(r), 1)
