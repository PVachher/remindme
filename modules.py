def add_user(first_name, last_name, username, mobile, email, password,authcode,authlevel):
    import pymysql
    db = pymysql.connect("52.66.46.128", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    sql = "INSERT INTO userdb (FirstName,LastName,Username,MobileNumber,Email,Password,authcode,authlevel) " \
          "VALUES ('%s','%s','%s','%d','%s','%s','%s','%s')" % (first_name, last_name, username,mobile,email,password,authcode,authlevel)
    try:
        cursor.execute(sql)
        db.commit()
        print "DONE"
    except:
        db.rollback()
    db.close()

def dndchecker(number):
    import urllib2
    import json
    url = "http://dndchecker.railsroot.com/api?mobile_number="+str(number)
    req = urllib2.urlopen(url)
    final = json.load(req)
    return final

def getdate():
    import time
    localtime = time.localtime(time.time())
    year = localtime[0]
    month =localtime[1]
    date = localtime[2]
    return (str(date)+":"+str(month)+":"+str(year))

def gettime():
    import time
    localtime = time.localtime(time.time())
    hour = localtime[3]
    minute = localtime[4]
    seconds = localtime[5]
    return (str(hour)+":"+str(minute) + ":" + str(seconds))

def putreminder(username, data, date, time):
    import pymysql
    db = pymysql.connect("52.66.46.128", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    sql = "INSERT INTO reminder (username, reminder_data,reminder_date,reminder_time) " \
          "VALUES ('%s','%s','%s','%s')" % (username,data,date,time)
    try:
        cursor.execute(sql)
        db.commit()
        print "Reminder Added"
    except:
        db.rollback()
    db.close()


def updateauth(username):
    import pymysql
    db = pymysql.connect("52.66.46.128", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    sql = "UPDATE userdb SET authlevel= 1\
                   WHERE username = '%s'" % (username.lower())
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "ERROR Updating Auth"

def getauthcode(username):
    import pymysql
    db = pymysql.connect("52.66.46.128", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    sql = "SELECT * FROM userdb \
                   WHERE username = '%s'" % (username.lower())
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results[0][-2]
    except:
        print "ERROR updating Auth"

def checkauth(username):
    import pymysql
    db = pymysql.connect("52.66.46.128", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    sql = "SELECT * FROM userdb \
               WHERE username = '%s'" % (username.lower())
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if results[0][-1] == '0':
            return False
        else:
            return True
    except:
        print "ERROR CHECKING Auth"


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
        if results[0][-3] == password:
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

def mail_engine_authentication(name,username,emailid,authenticationid):
    import smtplib
    import string
    import traceback
    import sys
    fromaddr = 'remindme@prateekvachher.in'
    password = 'Welcome123'
    toaddrs  = emailid
    server_smtp = 'host5.dnsinweb.com'
    port_smtp = 465
    BODY = string.join((
            "From: %s" % fromaddr,
            "To: %s" % toaddrs,
            "Subject: %s" % 'Email Verification Required' ,
            "",
            'Hello %s, \nThanks for signing up to RemindMe! By having a RemindMe account you can set time based reminders without the need of any 3rd Party Applications. \n\nBefore you access your account, you will need to verify your email address. You can do so by logging into your account and entering the Verification ID as %s. \n\nJust a friendly reminder, your account details are: \nUsername: %s \nEmail ID: %s\nhttp://remindme.prateekvachher.in\n\nThanks for registering, I appreciate your support!\n\n--\nPrateek Vachher\nDeveloper-RemindMe\ncontact@prateekvachher.in\n\nhttps://www.facebook.com/pvachher\nhttps://github.com/PVachher'  % (name, authenticationid,username,emailid)
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


def mail_engine_reminder(name,reminder,emailid):
    import smtplib
    import string
    import traceback
    import sys
    fromaddr = 'reminder@prateekvachher.in'
    password = 'Welcome123'
    toaddrs  = emailid
    server_smtp = 'host5.dnsinweb.com'
    port_smtp = 465
    BODY = string.join((
            "From: %s" % fromaddr,
            "To: %s" % toaddrs,
            "Subject: REMINDER: %s" % reminder,
            "",
            'Hello %s, \nThanks for signing up to RemindMe! By having a RemindMe account you can set time based reminders without the need of any 3rd Party Applications. \n\nBefore you access your account, you will need to verify your email address. You can do so by logging into your account and entering the Verification ID as %s. \n\nJust a friendly reminder, your account details are: \nUsername: %s \nEmail ID: %s\nhttp://remindme.prateekvachher.in\n\nThanks for registering, I appreciate your support!\n\n--\nPrateek Vachher\nDeveloper-RemindMe\ncontact@prateekvachher.in\n\nhttps://www.facebook.com/pvachher\nhttps://github.com/PVachher'  % (name, 'TEST','TEST',emailid)
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

