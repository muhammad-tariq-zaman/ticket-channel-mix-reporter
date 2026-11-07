# ticket-channel-mix-reporter

Summarise where tickets come from — phone, email, portal or chat — with counts and shares, largest channel first, so staffing follows demand.

## How to run

```sh
python3 main.py tickets.csv
```

## Example output

```
email: 42 tickets (60%)
phone: 28 tickets (40%)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
