from app import app
from models import *
from flask import jsonify,render_template

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
	if 'truck_no' in request.args and 'lat' in request.args and 'log' in request.args:
		truck_no = request.args.get('truck_no')
		lat = request.args.get('lat')
		log = request.args.get('log')
		insert_truck(truck_no,lat,log)
		return truck_no + " "+ lat + " " + log + " inserted"
	else:
		return "Error: All fields are mandatory"