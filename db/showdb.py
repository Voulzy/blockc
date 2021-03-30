import sqlite3

conn = sqlite3.connect("car.db")
c = conn.cursor()

for row in c.execute("SELECT * FROM car"):
	print(row)
