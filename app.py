from flask import Flask, render_template,request,json
from flask.ext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

#MySQL configurations
app.config['MYSQL_DATABASE_USER'] = '' #add username
app.config['MYSQL_DATABASE_PASSWORD'] = '' #add password
app.config['MYSQL_DATABASE_DB'] = '' #add dbname
app.config['MYSQL_DATABASE_HOST'] = 'localhost' 
mysql.init_app(app)


@app.route('/')
def main():
	return render_template('index.html') #Render homepage template index.html

@app.route('/showBooking/')
def showBooking():
	return render_template(
	'booking.html',
	date=[{'date':'1'},{'date':'2'},{'date':'3'},{'date':'4'},{'date':'5'},{'date':'6'},{'date':'7'},{'date':'8'},{'date':'9'},{'date':'10'},{'date':'11'},{'date':'12'},{'date':'13'},{'date':'14'},{'date':'15'},{'date':'16'},{'date':'17'},{'date':'18'},{'date':'19'},{'date':'20'},{'date':'21'},{'date':'22'},{'date':'23'},{'date':'24'},{'date':'25'},{'date':'26'},{'date':'27'},{'date':'28'},{'date':'29'},{'date':'30'},{'date':'31'}],
	month=[{'mon':'Jan'},{'mon':'Feb'},{'mon':'Mar'},{'mon':'Apr'},{'mon':'May'},{'mon':'Jun'},{'mon':'Jul'},{'mon':'Aug'},{'mon':'Sep'},{'mon':'Oct'},{'mon':'Nov'},{'mon':'Dec'}],
	year=[{'yr':'1996'},{'yr':'1997'},{'yr':'1998'},{'yr':'1999'},{'yr':'2000'}]) #Render booking page

@app.route('/flights/')
def flight():
	return render_template('flight.html') #Render flight details page

#TODO : Debug POST data from UI
@app.route('/booking/',methods=['POST'])
def booking():
	_firstName = request.form['firstName']
	_lastName = request.form['lastName']
	_email = request.form['email']
	_gender = request.form['gender']
	#Get dob data from UI
	_date = request.form.get('date')
	_month = request.form.get('month')
	_year = request.form.get('year')

	_phoneNo = request.form['phone']
	_firstLineAddress = request.form['firstLine']
	_secondLineAddress = request.form['secondLine']
	_state = request.form['state']

	#checking for validations
	if _firstName and _lastName and _email and _gender and _date and _month and _year and _phoneNo and _firstLineAddress and _secondLineAddress and _state:
		return json.dumps({'html':'<span>All good!</span>'})
	else:
		return json.dumps({'html':'<span>Error</span>'})

if __name__=="__main__":
	app.run(debug=True)
