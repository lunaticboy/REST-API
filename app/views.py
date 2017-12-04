from app import app
from flask import render_template,redirect,request,flash,g,session,url_for
from models import *
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/showbyid/<int:id>',methods=['GET'])
def showbyid(id):
	return jsonify(show_by_id(id))

@app.route('/showbynum/<num>',methods=['GET'])
def showbynum(num):
	return jsonify(show_by_num(num))