from flask import Flask, redirect, url_for, session, request, jsonify,render_template
from flask_oauthlib.client import OAuth

app = Flask(__name__, template_folder='templates')

from flask_app import routes

if __name__ == "__main__":
    app.run()
