# Day 2 — Add Tasks Using Flask Forms

## Objective
Allow users to add new todo tasks using an HTML form.

## Concepts learned
- GET requests are commonly used to retrieve resources.
- POST requests are commonly used to submit data.
- `request.method` identifies the HTTP method.
- `request.form` accesses submitted form data.
- `.get()` retrieves a dictionary-like value with a default.
- `.strip()` removes leading and trailing whitespace.
- `redirect()` redirects the browser to another URL.
- `url_for()` generates a URL using a Flask view function name.
- Post/Redirect/Get helps prevent duplicate submissions on refresh.
- Backend validation is necessary even when HTML validation exists.

## Implementation
- Updated the home route to support GET and POST.
- Added an HTML form for task creation.
- Read the task title from the form.
- Prevented empty and whitespace-only tasks.
- Added valid tasks to the in-memory list.
- Redirected to the home page after submission.
- Displayed the updated task list.

## Current limitations
- Task data is not persisted in a database.
- Task IDs are generated using the current list length.
- Users cannot yet edit, complete, or delete tasks.

## Next steps
- Learn Flask route parameters.
- Implement task completion and deletion.
- Learn how to use HTTP methods appropriately.
- Add persistent storage in a future stage.