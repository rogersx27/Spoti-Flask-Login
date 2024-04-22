import os
from dotenv import load_dotenv

from flask import Flask

load_dotenv()

app = Flask(__name__)
app.config["SESSION_COOKIE_NAME"] = "spotify-login-session"
app.secret_key = os.getenv('SECRET_KEY')
app.debug = True
