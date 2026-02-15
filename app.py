from flask import Flask, request, url_for, session, Response, redirect


"""app = Flask(__name__)                     # This is Object

@app.route("/")
def home():
    return 'Hello User! This is my first Flask App'

@app.route("/about")
def about():
    return 'This is About us page'

@app.route("/contact")
def contact():
    return "This is Contact page"



@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return "You send data !"
    else:
        return "You are only viewing"            """

app = Flask(__name__)
app.secret_key = "supersecret"

#Homepage for Login page
@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username  #Store in session

            return redirect(url_for("welcome"))
        else:
            return Response("In-valid credentials. Try Again !!!", mimetype="text/plain")


    return '''
            <h2>Login Page !</h2>
            <form method="POST">
                Username : <input type = "text" name = "username"><br>
                Password : <input type = "password" name = "password"><br>
                <input type="submit" value="Login">
            </form>
'''

#Welcome Page
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
                <h2> Welcome, {session["user"]}!</h2>
                <a href={url_for('logout')}>Logout</a>

        '''
    
    return redirect(url_for("login"))



#Logout page

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
