from flask import *
from modules import checklogin, add_user, checkusername, checkmob, checkemail, getname, mail_engine_authentication, checkauth, getauthcode, updateauth, putreminder, getdate,gettime
import random
from smsengine import *
import time
app = Flask(__name__, static_url_path='/static')
database = {}
SITE_KEY = '6LeCQgoUAAAAAJTKVmw--WI9sZdMDJqnXLsDVMyU'
SECRET_KEY = '6LeCQgoUAAAAAG10j2-q3nBB59xwBpYiiOeEEY-J'
@app.route('/', methods=['GET','POST'])
def home():
    error = ""
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        if checkauth(username_session) == True:
            return redirect(url_for('remindabout'))
        else:
            if request.method == 'POST':
                string1 = ""
                string1 += request.form['val1']
                string1 += request.form['val2']
                string1 += request.form['val3']
                string1 += request.form['val4']
                print string1
                if string1 == getauthcode(username_session):
                    updateauth(username_session)
                    return redirect(url_for('home'))
                else:
                    error = "INVALID AUTH CODE"

            return render_template('authentication.html', name=username_session, name1= getname(username_session),error= error)

    return redirect(url_for('login'))


def checkRecaptcha(response, secretkey):
    import urllib2
    url = 'https://www.google.com/recaptcha/api/siteverify?'
    url = url + 'secret=' +secretkey
    url = url + '&response=' +response
    try:
        jsonobj = json.loads(urllib2.urlopen(url).read())
	print jsonobj
        if jsonobj['success']:
            return True
        else:
            return False
    except Exception as e:
        return False

@app.route('/remindabout', methods=['GET','POST'])
def remindabout():
    error = ""
    if 'username' in session:
        global database
        username_session = escape(session['username']).capitalize()
        (database)[username_session] = ""
        if checkauth(username_session) == True:
            if request.method =='POST':
                if 'ok' in request.form:
                    session.clear()
                    return redirect(url_for("login"))
                else:
                    database[username_session] = request.form['Reminder']
                    return redirect(url_for('remindwhen'))
        else:
            return redirect(url_for('home'))
    return render_template('remindabout.html', name=username_session,name1=getname(username_session))

@app.route('/registersuccessful')
def registersuccess():
    return render_template('registersuccess.html')

@app.route('/remindersuccessful',methods=['GET','POST'])
def remindersuccess():
    if 'username' in session:
        if request.method == 'POST':
            if 'ok' in request.form:
                session.clear()
                return redirect(url_for("login"))
        else:
            username_session = escape(session['username']).capitalize()
            return render_template('remindersuccess.html',name1=username_session)
    else:
        return redirect(url_for('home'))

@app.route('/remindwhen', methods=['GET','POST'])
def remindwhen():
    global database
    error = ""
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        if checkauth(username_session) == True:
            if request.method =='POST':
                if 'ok' in request.form:
                    session.clear()
                    return redirect(url_for("login"))
                else:
                    response = request.form.get('g-recaptcha-response')
                    if checkRecaptcha(response, SECRET_KEY):
                        if request.form['Date'][2] == '-' and request.form['Date'][5] == '-' and request.form['Time'][2]==':':
                            final = ""
                            date = request.form['Date']
                            time1 = request.form['Time']
                            z = date.split('-')
                            final += z[-3]
                            final += ":"
                            final += str(int(z[-2]))
                            final += ":"
                            final += z[-1]
                            time1 += ":00"
                            putreminder(username_session.lower(), database[username_session], date, time1)
                            return redirect(url_for('remindersuccess'))
                        else:
                            error = "Invalid Entered Date/Time Structure"
                    else:
                        error = 'Invalid Captcha'
        else:
            return redirect(url_for('home'))
    return render_template('remindwhen.html', name=username_session,name1=getname(username_session),error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))
    value = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        val = checklogin(username,password)
        print val
        if val == "Granted":
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        elif val == 'Incorrect':
            value = "Incorrect Password!"
        elif val == 'NoUser':
            value = "User doesn't exist!"
    return render_template('login.html',value = value)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



@app.route('/register', methods=['GET','POST'])
def register():
        v1 = v2 = v3 =v4 = v5 = ""
        error = ""
        if request.method =='POST':
            if checkusername(request.form['username']) == False:
                if checkmob(request.form['mobile']) == False:
                    if checkemail(request.form['email']) == False:
                        if request.form['password'] == request.form['repassword']:
                            response = request.form.get('g-recaptcha-response')
                            if checkRecaptcha(response,SECRET_KEY):
                                generatedid = random.randint(1000,9999)
                                add_user(request.form['FirstName'],request.form['LastName'],request.form['username'],int(request.form['mobile']),request.form['email'],request.form['password'],str(generatedid),str(0))
                                mail_engine_authentication(request.form['FirstName'],request.form['username'],request.form['email'], str(generatedid))
                                return redirect(url_for('registersuccess'))

                            else:
                                error = 'Invalid Captcha'
                                v1 = request.form['FirstName']
                                v2 = request.form['LastName']
                                v3 = request.form['username']
                                v4 = request.form['mobile']
                                v5 = request.form['email']
                        else:
                            error = "Passwords Don't Match"
                            v1 = request.form['FirstName']
                            v2 = request.form['LastName']
                            v3 = request.form['username']
                            v4 = request.form['mobile']
                            v5 = request.form['email']
                    else:
                        error = 'Email ID Already Registered'
                        v1 = request.form['FirstName']
                        v2 = request.form['LastName']
                        v3 = request.form['username']
                        v4 = request.form['mobile']
                        v5 = request.form['email']
                else:
                    error = 'Mobile Number Already Registered'
                    v1 = request.form['FirstName']
                    v2 = request.form['LastName']
                    v3 = request.form['username']
                    v4 = request.form['mobile']
                    v5 = request.form['email']
            else:
                error = "User ID Already Registered"
                v1 = request.form['FirstName']
                v2 = request.form['LastName']
                v3 = request.form['username']
                v4 = request.form['mobile']
                v5 = request.form['email']

        return render_template('register.html', error=error, v1=v1, v2=v2, v3=v3, v4=v4, v5=v5)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080,debug=True)
