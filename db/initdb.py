import sqlite3


vin="CAR1234567CAR1234"
address="ZLGVEQ9JUZZWCZXLWVNTHBDX9G9KZTJP9PREEIIFHY9SIQKYBVAHIMLHXPQVE9IXFDDXNHQINXJDRPFDX"
values=(vin,address)

conn = sqlite3.connect("car.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS car (id INTEGER PRIMARY KEY, vin TEXT, address TEXT)")
c.execute("INSERT INTO car VALUES(1,?,?)",values)
conn.commit()

for row in c.execute("SELECT * FROM car"):
	print(row)

conn.close()