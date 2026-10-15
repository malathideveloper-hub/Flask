from flask import Flask, render_template

app=Flask(__name__)

tasks=[
    {"id":1, "title":"Learn flask basics", "completed":False},
    {"id": 2, "title": "Build my first backend project", "completed": False},
    {"id": 3, "title": "Commit code to GitHub", "completed": True},
]

@app.route("/")
def home():
    return render_template("index.html",tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)