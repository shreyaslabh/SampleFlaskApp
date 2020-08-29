"""CREATE TABLE users(
uname VARCHAR(100),
	ssn INT,
	mob VARCHAR(50),
	email VARCHAR(50),
	address VARCHAR(100)
	

)"""




'''import psycopg2

con = psycopg2.connect(user="datamaskuser",
                                  password="datamaskuser123",
                                  host="35.245.71.89",
                                  port="5432",
                                  dbname="sampleapp")

cur = con.cursor()                           
cur.execute("SELECT * FROM users")
data = cur.fetchall()

print(data)'''

import datetime,time

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(st)