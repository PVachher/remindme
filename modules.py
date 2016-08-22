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

def mail_engine_authentication(name,emailid,authenticationid):
    import smtplib
    import string
    import traceback
    import sys

    fromaddr = 'remindme@prateekvachher.in'
    password = 'Welcome123'
    toaddrs  = emailid
    server_smtp = 'host5.dnsinweb.com'
    port_smtp = 465

    msg = 'Test message ^^'
    BODY = string.join((
            "From: %s" % fromaddr,
            "To: %s" % toaddrs,
            "Subject: %s" % 'Email Verification for Remind Me Web App' ,
            "",
            'Email Verification for %s. This is to Inform you that your verification id is: %s'  % (name, authenticationid)
            ), "\r\n")

    try :


        server = smtplib.SMTP_SSL(host=server_smtp, port=port_smtp)
        server.set_debuglevel(True)
        server.esmtp_features['auth'] = 'LOGIN PLAIN'
        server.login('remindme@prateekvachher.in', password)
        server.sendmail(fromaddr, toaddrs, str(BODY))
        server.quit()

    except smtplib.SMTPServerDisconnected :
        print "smtplib.SMTPServerDisconnected"
    except smtplib.SMTPResponseException, e:
        print "smtplib.SMTPResponseException: " + str(e.smtp_code) + " " + str(e.smtp_error)
    except smtplib.SMTPSenderRefused:
        print "smtplib.SMTPSenderRefused"
    except smtplib.SMTPRecipientsRefused:
        print "smtplib.SMTPRecipientsRefused"
    except smtplib.SMTPDataError:
        print "smtplib.SMTPDataError"
    except smtplib.SMTPConnectError:
        print "smtplib.SMTPConnectError"
    except smtplib.SMTPHeloError:
        print "smtplib.SMTPHeloError"
    except smtplib.SMTPAuthenticationError:
        print "smtplib.SMTPAuthenticationError"
    except Exception, e :
        print "Exception", e
        print traceback.format_exc()
        print sys.exc_info()[0]

