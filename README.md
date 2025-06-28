# 📅 Event Scheduler System (Flask REST API)

A simple Python + Flask backend application that allows users to schedule, update, delete, and view events. Events are stored in a local JSON file to persist across sessions.

---

## 🚀 Features

- Create new events with title, description, start time, and end time
- View all scheduled events (sorted by start time)
- Update existing events
- Delete events
- File-based persistence using `events.json`
- Testable via Postman (Collection included)

---

## 🔧 Requirements

- Python 3.7+
- pip (Python package manager)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ranganath099/eventschedular.git
cd eventschedular
2. (Optional but recommended) Create a virtual environment

python -m venv venv
venv\Scripts\activate        # On Windows
# OR
source venv/bin/activate     # On Linux/macOS
3. Install required dependencies

pip install -r requirements.txt
▶️ Running the Application

python app.py
By default, it runs on http://localhost:5000/

🔁 API Endpoints (Test in Postman)
All endpoints are http://localhost:5000/...

➕ Create an Event (POST /events)
Request Body:

json

{
  "title": "Team Meeting",
  "description": "Weekly sync-up",
  "start_time": "2025-06-30T10:00:00",
  "end_time": "2025-06-30T11:00:00"
}
Response:


{
  "message": "Event created",
  "event": {
    "id": "a-uuid",
    "title": "Team Meeting",
    ...
  }
}
📋 View Events (GET /events)
Returns all events, sorted by start_time.

Example Response:


[
  {
    "id": "abc123",
    "title": "Team Meeting",
    "start_time": "2025-06-30T10:00:00"
  }
]
✏️ Update Event (PUT /events/<id>)
http
Copy
Edit
PUT /events/abc123
Request Body:

json
Copy
Edit
{
  "title": "Updated Meeting"
}
❌ Delete Event (DELETE /events/<id>)
http
Copy
Edit
DELETE /events/abc123
Response:

json
Copy
Edit
{
  "message": "Event deleted"
}
⏰ Get Reminders (GET /reminders)
Returns all events starting within the next 1 hour.

🧪 Testing with Postman
Open Postman

Import Event Scheduler.postman_collection.json file

Run the saved endpoints (Create, View, Update, Delete, Reminder)

📁 Project Structure

eventschedular/
│
├── app.py                  # Main Flask app
├── utils.py                # File read/write helpers
├── events.json             # Stores events (runtime data)
├── test_app.py             # (Optional) Pytest test cases
├── requirements.txt        # Python dependencies
├── README.md               # Project instructions
└── .gitignore
✅ Sample Requirements File (requirements.txt)

flask
flask-cors
🧾 License
This project is for educational purposes only.

🙋‍♂️ Author
Ranganath B



---

Would you like me to:
- Create a downloadable `README.md` file
- Include `test_app.py` example test cases
- Auto-generate a `.zip` of your full project structure

Just let me know!
