import sqlite3 as sql

def insert_truck(truck_no,lat,log):
	with sql.connect('database.db') as con:
		cur = con.cursor()
		cur.execute('INSERT INTO truck (truck_no,lat,log) VALUES (?,?,?)',(truck_no,lat,log))
		con.commit()

def show_by_id(id):
	with sql.connect('database.db') as con:
		cur = con.cursor()
		result = cur.execute('SELECT * FROM truck WHERE id=?',(id,))
		return result.fetchall()

def show_by_num(truck_no):
	with sql.connect('database.db') as con:
		cur = con.cursor()
		result = cur.execute('SELECT * FROM truck WHERE truck_no=?',(truck_no,))
		return result.fetchall()

def show_all_trucks():
	with sql.connect('database.db') as con:
		cur = con.cursor()
		cur.execute('SELECT * FROM truck')
		con.commit()
