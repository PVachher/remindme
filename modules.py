def add_user(first_name, last_name, username, mobile, email, password):
    import pymysql
    db = pymysql.connect("52.66.46.128", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    sql = "INSERT INTO userdb (FirstName,LastName,Username,MobileNumber,Email,Password) " \
          "VALUES ('%s','%s','%s','%d','%s','%s')" % (first_name, last_name, username,mobile,email,password)
    try:
        cursor.execute(sql)
        db.commit()
        print "DONE"
    except:
        db.rollback()
    db.close()


def checkusername(username):
    import pymysql
    db = pymysql.connect("52.66.46.128", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    sql = "SELECT * FROM userdb \
           WHERE username = '%s'" % (username.lower())
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) == 0:
            return False
        else:
            return True
    except:
        print "ERROR CHECKING USERNAME"

def getname(username):
    import pymysql
    db = pymysql.connect("52.66.46.128", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    sql = "SELECT * FROM userdb \
           WHERE username = '%s'" % (username.lower())
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results[0][0]
    except:
        print "ERROR CHECKING Name"

def checkmob(mobile):
    import pymysql
    db = pymysql.connect("52.66.46.128", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    sql = "SELECT * FROM userdb \
           WHERE MobileNumber = '%s'" % str(mobile)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) == 0:
            return False
        else:
            return True
    except:
        print "ERROR CHECKING Mobile"

def checkemail(email):
    import pymysql
    db = pymysql.connect("52.66.46.128", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    sql = "SELECT * FROM userdb \
           WHERE Email = '%s'" % (email)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) == 0:
            return False
        else:
            return True
    except:
        print "ERROR CHECKING Email"

def checklogin(username,password):
    import pymysql
    db = pymysql.connect("52.66.46.128", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    sql = "SELECT * FROM userdb \
           WHERE username = '%s'" % (username.lower())
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if results[0][-1] == password:
            flag = 1
        else:
            flag = 0
    except:
        flag = 2

    if flag == 1:
        return "Granted"
    elif flag == 0:
        return "Incorrect"
    elif flag == 2:
        return "NoUser"
    db.close()

