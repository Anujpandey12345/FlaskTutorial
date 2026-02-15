from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def student_profile():
    return render_template(
        "profile.html",
        name="Anuj",
        is_topper=True,
        subjects=["Maths", "Science", "history"]
    )