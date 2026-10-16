
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
            new_task = {
                "id": len(tasks) + 1,
                "title": title,
                "completed": False,
            }
            tasks.append(new_task)

        return redirect(url_for("home"))

    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)
