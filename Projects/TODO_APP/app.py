
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Flask basics", "completed": False},
    {"id": 2, "title": "Build my first backend project", "completed": False},
    {"id": 3, "title": "Commit code to GitHub", "completed": True},
]


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form.get("title", "").strip()

        if title:
            next_id = max((task["id"] for task in tasks), default=0) + 1

            new_task = {
                "id": next_id,
                "title": title,
                "completed": False,
            }

            tasks.append(new_task)

        return redirect(url_for("home"))

    return render_template("index.html", tasks=tasks)


@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    task = next(
        (task for task in tasks if task["id"] == task_id),
        None,
    )

    if task:
        task["completed"] = True

    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    task = next(
        (task for task in tasks if task["id"] == task_id),
        None,
    )

    if task:
        tasks.remove(task)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
