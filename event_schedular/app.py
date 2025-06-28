from flask import Flask, request, jsonify
import uuid
from utils import load_events, save_events, get_upcoming_reminders
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

EVENTS_FILE = 'events.json'
events = load_events(EVENTS_FILE)

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = {
        "id": str(uuid.uuid4()),
        "title": data["title"],
        "description": data["description"],
        "start_time": data["start_time"],
        "end_time": data["end_time"]
    }
    events.append(event)
    save_events(events, EVENTS_FILE)
    return jsonify({"message": "Event created", "event": event}), 201

@app.route('/events', methods=['GET'])
def get_events():
    sorted_events = sorted(events, key=lambda e: e['start_time'])
    return jsonify(sorted_events)

@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    for event in events:
        if event["id"] == event_id:
            event.update(data)
            save_events(events, EVENTS_FILE)
            return jsonify({"message": "Event updated", "event": event})
    return jsonify({"error": "Event not found"}), 404

@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    global events
    events = [e for e in events if e["id"] != event_id]
    save_events(events, EVENTS_FILE)
    return jsonify({"message": "Event deleted"}), 200

@app.route('/reminders', methods=['GET'])
def reminders():
    upcoming = get_upcoming_reminders(events)
    return jsonify(upcoming)

if __name__ == '__main__':
    app.run(debug=True)
