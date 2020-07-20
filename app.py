import os
import json
import requests
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
from datetime import datetime
from db import User, Tasks, Add_Entry, Delete, Check, JSONEncoder, session

db = session

# Path references for templates (HTML) and static (CSS) folders
TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')

app = Flask('Task Master', template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.json_encoder = JSONEncoder
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

# Stored in config file and noted by .gitignore
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

# ----------------------------------------------------------------------
# Google oauth and Flask-Login

# Login Manager setup
login_manager = LoginManager()
login_manager.init_app(app)

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for('homepage', user=current_user))
    else:
        return '<a class="button" href="/login">Google Login</a>'

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

@app.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@app.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that we have tokens (yay) let's find and hit URL
    # from Google that gives you user's profile information,
    # including their Google Profile Image and Email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # We want to make sure their email is verified.
    # The user authenticated with Google, authorized our
    # app, and now we've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in our db with the information provided
    # by Google
    unique_id = int(unique_id) / 1000
    user = User(unique_id, name=users_name, email=users_email)

    # Doesn't exist? Add to database
    if Check(user.id) == False:
        print("------------")
        print("good")
        print()
        Add_Entry(user)

    # Begin user session by logging the user in
    login_user(user)

    # Send user back to homepage
    return redirect(url_for("index"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

# ----------------------------------------------------------------------
# Actual service

@app.route('/homepage', methods=['POST', 'GET'])
@app.route('/homepage/<tasks>', methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Tasks(content = task_content, user = current_user.id)
        
        try:
            Add_Entry(new_task)
            return return_to_home()
        except:
            return "There was an issue adding your task."
    else:
        return return_to_home()

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = db.query(Tasks).get(id)
    
    try:
        Delete(task_to_delete)
        return return_to_home()
    except:
        return "There was a problem deleting that task"

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    task = db.query(Tasks).get(id)

    if request.method == 'POST':
        task.content = request.form['content']
        db.commit()
        return return_to_home()
    else:
        return render_template('update.html', task=task)

# Just so I don't have to query the database within each function EVERY time I wanna return to the homepage
def return_to_home():
    tasks = db.query(Tasks).filter(Tasks.user_id == current_user.id).order_by(Tasks.date_created).all()
    return render_template('homepage.html', tasks=tasks)

if __name__ == "__main__":
    app.run(ssl_context = "adhoc", debug=False) 