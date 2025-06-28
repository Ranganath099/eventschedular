import json
from datetime import datetime, timedelta

def load_events(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_events(events, path):
    with open(path, 'w') as f:
        json.dump(events, f, indent=4)

def get_upcoming_reminders(events):
    now = datetime.now()
    upcoming = []
    for e in events:
        try:
            start = datetime.fromisoformat(e["start_time"])
            if now <= start <= now + timedelta(hours=1):
                upcoming.append(e)
        except:
            continue
    return upcoming
