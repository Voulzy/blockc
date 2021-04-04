import sqlite3

conn = sqlite3.connect("car2.db")
c = conn.cursor()


vin = input("Entrer VIN   ")
uid = input("Entrer UID   ")

data=(vin,uid)

c.execute("INSERT INTO car VALUES(?,?)",data)
conn.commit()

for row in c.execute("SELECT * FROM car"):
	print(row)

conn.close()