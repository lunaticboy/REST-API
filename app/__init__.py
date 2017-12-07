from flask import Flask

app = Flask(__name__)
app.secret_key = 'default'

from app import views,models