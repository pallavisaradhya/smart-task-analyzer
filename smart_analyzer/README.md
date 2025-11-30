 # Smart Task Analyzer

## Project Overview
Smart Task Analyzer is a mini web application that intelligently scores and prioritizes tasks based on multiple factors such as urgency, importance, effort, and dependencies. It helps users decide which tasks to focus on first, improving productivity and task management.

---

## Tech Stack
- *Backend:* Python 3.8+, Django 4.x, Django REST Framework  
- *Frontend:* HTML, CSS, JavaScript  
- *Database:* SQLite (default Django)  

---

## Setup Instructions

1. *Clone the repository:*
   ```bash
   git clone <your-github-repo-link>
   cd smart-task-analyzer

2. Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate   # Mac/Linux


3. Install dependencies:

pip install -r requirements.txt


4. Apply database migrations:

python manage.py makemigrations
python manage.py migrate


5. Run the development server:

python manage.py runserver


6. Open the frontend in a browser:

http://127.0.0.1:8000/


7. Run unit tests (optional but recommended):

python manage.py test




---

API Endpoints

POST /api/tasks/analyze/
Accepts a list of tasks in JSON and returns them sorted by priority with calculated scores.

GET /api/tasks/suggest/
Returns the top 3 tasks the user should work on today with explanations for why each was chosen.



---

Algorithm Explanation

The priority score for each task is calculated based on four main factors:

1. Urgency:
Tasks with due dates closer to today are given higher priority. Past-due tasks are weighted higher to ensure they are addressed immediately.


2. Importance:
Each task has a user-provided importance rating (1–10 scale). Higher importance increases the task’s priority score significantly.


3. Effort:
Tasks that require fewer hours are considered "quick wins" and receive a small bonus in the score.


4. Dependencies:
Tasks that are prerequisites for other tasks are prioritized higher so that dependent tasks can proceed without delay.



The final score is a sum of all these factors. Tasks are sorted in descending order of priority. This algorithm ensures a balance between urgent, important, low-effort, and dependent tasks.


---

Design Decisions

Django REST Framework is used for the backend API to allow easy integration with the frontend.

ManyToManyField is used for task dependencies, allowing multiple dependencies per task.

The priority scoring function is kept in utils.py for modularity and easier unit testing.

Unit tests cover scenarios for basic priority, past-due tasks, and tasks with dependencies.

Frontend is minimal but functional, with HTML/CSS/JS communicating directly with the API.



---

Time Breakdown

Task	Time Spent

Backend setup & models	45 minutes
Priority scoring algorithm	45 minutes
API views & serializers	30 minutes
Frontend HTML/CSS/JS	45 minutes
Unit tests	30 minutes
Debugging & final testing	30 minutes



---

Bonus Features Attempted

Handling task dependencies in priority scoring

Explanation for task scores in API responses

Unit tests to ensure correct scoring logic



---

Future Improvements

Allow users to adjust weights for urgency, importance, and effort

Visualize task dependencies as a graph

Add an Eisenhower Matrix view (Urgent vs Important)

Save user preferences for prioritization strategy

Implement task history and learning system to improve future suggestions



---

How to Use

1. Enter tasks manually in the input form or paste a JSON array of tasks.


2. Click Analyze Tasks to see tasks sorted by priority.


3. Use the Suggest Tasks API or frontend section to see the top 3 tasks to work on today.


4. Each task shows its priority score and reason for the score.




---

Example JSON Input

[
  {
    "title": "Fix login bug",
    "due_date": "2025-11-30",
    "estimated_hours": 3,
    "importance": 8,
    "dependencies": []
  },
  {
    "title": "Write report",
    "due_date": "2025-12-05",
    "estimated_hours": 5,
    "importance": 6,
    "dependencies": []
  }
]


---

Author

Your Name: Pallavi K S

Contact: [pallaviks135@gmail.com]