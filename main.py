"""Ticket volume by contact channel.

Usage: python3 main.py tickets.csv
CSV columns: ticket,channel (phone/email/portal/chat/other).
Per channel: count and share of all tickets, largest first.
"""
import argparse, csv, sys
from collections import Counter

def report(rows):
    counts = Counter(r["channel"].strip().lower() for r in rows)
    total = sum(counts.values())
    out = []
    for channel, count in counts.items():
        out.append((channel, count, count / total if total else 0))
    return sorted(out, key=lambda r: -r[1])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for channel, count, share in report(list(csv.DictReader(f))):
            print(f"{channel}: {count} tickets ({share:.0%})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
