import sqlite3

data = [('VIN1','AA'),
		('VIN2','BB'),
		('VIN3','CC'),
		('VIN4','DD')]

conn = sqlite3.connect("car2.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS car (vin TEXT PRIMARY KEY, uid TEXT)")
c.executemany("INSERT INTO car VALUES(?,?)",data)
conn.commit()

for row in c.execute("SELECT * FROM car"):
	print(row)

conn.close()