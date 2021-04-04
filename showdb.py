import sqlite3

def get_uid(VIN):
	conn = sqlite3.connect("car2.db")
	c = conn.cursor()
	uid = c.execute(("SELECT uid FROM car WHERE vin = '{}'").format(VIN))
	uid = c.fetchone()
	if not uid:
		return "error"
	if uid:
		print(uid[0])
		return uid[0]

if __name__ == '__main__':
	conn = sqlite3.connect("car2.db")
	c = conn.cursor()

	for row in c.execute("SELECT * FROM car"):
		print(row)

