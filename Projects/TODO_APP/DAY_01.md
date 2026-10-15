# Day 1 — Flask Todo App

## Objective
Build the foundation of a Todo application using Python and Flask.

## Concepts learned
- Flask is a Python web framework.
- A route maps a URL to a view function.
- A view function processes a request and returns a response.
- `render_template()` renders an HTML template.
- Flask uses the `templates` directory by default.
- Jinja supports loops, conditions, and variable interpolation.
- Python lists and dictionaries can represent sample application data.
- A virtual environment isolates project dependencies.

## Implementation
- Created a Flask application.
- Added a home route (`/`).
- Created sample todo tasks.
- Passed tasks from Python to an HTML template.
- Displayed task titles and completion status.

## Current limitations
- Tasks are hardcoded.
- There is no form to add a task.
- There is no way to mark a task complete or delete it.
- Data is not stored in a database.

## Next steps
- Add a form to create tasks.
- Handle POST requests.
- Understand GET vs POST.
- Add task completion and deletion.
- Introduce DB in later stages.