import sqlite3

conn = sqlite3.connect("car.db")
c = conn.cursor()

sql = 'DELETE FROM car'
cur = conn.cursor()
cur.execute(sql)
conn.commit()

for row in c.execute("SELECT * FROM car"):
	print(row)

conn.close()