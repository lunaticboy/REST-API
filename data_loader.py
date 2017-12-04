import csv,sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor();

with open('Truck.csv','rb') as fin:
	dr = csv.DictReader(fin)
	to_db = [(i['truck_no'], i['lat'], i['log']) for i in dr]

con.executemany("INSERT INTO truck (truck_no,lat,log) VALUES (?,?,?);", to_db)
con.commit();
con.close();