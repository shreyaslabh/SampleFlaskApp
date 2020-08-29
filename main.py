from flask import Flask,render_template,request,session,redirect,url_for,flash
import psycopg2
import datetime
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'

con = psycopg2.connect(user="datamaskuser",
                                  password="datamaskuser123",
                                  host="35.245.71.89",
                                  port="5432",
                                  dbname="sampleapp")


@app.route('/',methods=["GET","POST"])
@app.route('/home',methods=["GET","POST"])
def home():
	return render_template('home.html')

@app.route('/csubmit',methods=["GET","POST"])
def csubmit():
	if request.method == "POST":
		cname = request.form['cname']
		ssn = request.form['ssn']
		mob = request.form['mob']
		email = request.form['email']
		addr = request.form['addr']

		ts = time.time()

		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		#data = [session['name'],session['ssn'],session['email'],session['addr']]
		cur = con.cursor()  
		cur.execute("INSERT INTO users(uname,ssn,mob,email,address,ts) VALUES(%s,%s,%s,%s,%s,%s)",(cname,ssn,mob,email,addr,st))
		con.commit()
		cur.execute("SELECT * FROM users WHERE uname = %s AND ssn = %s AND mob = %s AND email = %s AND address = %s AND ts = %s",(cname,ssn,mob,email,addr,st))
		data = cur.fetchone()[0]
		uid = data

		return render_template('submitted.html',uid = uid)

@app.route('/edit',methods=["GET","POST"])
def edit():
	cur = con.cursor()      
	uid = request.form['uid']                     
	cur.execute("SELECT * FROM users WHERE uid = %s",(uid,))
	data = cur.fetchall()[0]
	return render_template('edit.html',data=data,uid=uid)


@app.route('/database',methods=["GET","POST"])
def database():
	cur = con.cursor()                           
	cur.execute("SELECT * FROM users ORDER BY ts DESC")
	try:
	 data = cur.fetchall()
	 print(data[0])
	 return render_template('database.html',data=data)
	except:
		flash("No Users Found")
		return render_template('database.html')


@app.route('/cedit',methods=["GET","POST"])
def cedit():
	if request.method == "POST":
		uname = request.form['cname']
		ssn = request.form['ssn']
		mob = request.form['mob']
		email = request.form['email']
		addr = request.form['addr']
		uid = request.form['uid']
		#data = [session['name'],session['ssn'],session['email'],session['addr']]
		#uid = session['uid']

		ts = time.time()

		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

		cur = con.cursor()  
		cur.execute("UPDATE users SET uname = %s, ssn = %s, mob = %s, email = %s, address = %s, ts = %s WHERE uid = %s",(uname,ssn,mob,email,addr,st,uid))
		con.commit()
		
		return render_template('submitted.html',uid = uid)
	else:
		return render_template('submitted.html')

if __name__ == "__main__":
        #app.run(host='0.0.0.0',port=5000,debug=True)
        app.run(debug=True)

