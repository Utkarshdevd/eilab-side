import sqlite3
conn = sqlite3.connect('program.db')
curs = conn.cursor()
ro = curs.execute('select * from customers')
customers = ro.fetchall()