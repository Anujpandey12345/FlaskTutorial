from flask import Flask, render_template, request, session, url_for, redirect, flash
from forms import RegistrationForm
app = Flask(__name__)
app.secret_key = "my-secret-key"

# @app.route("/", methods=["GET", "POST"])
# def form():
#     if request.method == "POST":
#         name = request.form.get("name")
#         if not name:
#             flash("Name cannot be empty")
#             return redirect(url_for("form"))
#         flash(f"ThankYou {name} , Your feedback is saved!")
#         return redirect(url_for("thankyou"))
#     return render_template("form.html")

"""We have multiple way to use Redirect """
# 1. return redirect(url_for("route_name")) ->> Good Way
# 2. return redirect("/route_name") ->> Bad way


# @app.route("/thankyou")
# def thankyou():
#     return render_template("thankyou.html")





"""How Forms Works"""

@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Welcome, {name}! You are register successfully")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)


@app.route("/success")
def success():
    return render_template("success.html")