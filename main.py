from flask import *
from modules import checklogin, add_user, checkusername, checkmob, checkemail, getname, mail_engine_authentication
import random
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        if request.method =='POST':
            if request.form['ok'] == 'Log Out':
                session.clear()
                return redirect(url_for("login"))

        return render_template('remindabout.html', name=username_session,name1 = getname(username_session))
    return redirect(url_for('login'))

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
                            generatedid = random.randint(1000,9999)
                            add_user(request.form['FirstName'],request.form['LastName'],request.form['username'],int(request.form['mobile']),request.form['email'],request.form['password'],str(generatedid),str(0))
                            mail_engine_authentication(request.form['FirstName'],request.form['email'], str(generatedid))
                            return redirect(url_for('login'))
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
	app.run(host='0.0.0.0',debug=True)
