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

@app.route('/show/<int:page>',methods=['GET'])
def showten(page):
	return jsonify(show_ten(page))

@app.route('/insert')
def insertion():
	truck_no = request.args.get('truck_no')
	lat = request.args.get('lat')
	log = request.args.get('log')
	return truck_no + " "+ lat + " " + log + "inserted"