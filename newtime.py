import time
from modules import mail_engine_reminder, getemail, getname
def updatedb(username,data,date,time):
    import pymysql
    db = pymysql.connect("52.66.105.87", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    sql = "UPDATE reminder SET notif= 1\
                   WHERE username = '%s' AND reminder_data = '%s' AND reminder_date = '%s' AND reminder_time='%s'" % (username,data,date,time)
    try:
        cursor.execute(sql)
        db.commit()
        print 'UPDATED'
    except:
        db.rollback()
        print "ERROR Updating Auth"
def difference_in_seconds(presenttime,timetobereached):
    timetobereached = timetobereached.split(':')
    seconds = 0
    seconds += (int(timetobereached[0])-int(presenttime[0]))*3600
    seconds += (int(timetobereached[1])-int(presenttime[1]))*60
    seconds += (int(timetobereached[2])-int(presenttime[2]))
    return seconds
def getdate():
    localtime = time.localtime(time.time())
    year = localtime[0]
    month =localtime[1]
    date = localtime[2]
    return [date, month, year]

def gettime():
    localtime = time.localtime(time.time())
    hour = localtime[3]
    minute = localtime[4]
    seconds = localtime[5]
    return [hour, minute, seconds]

def getdata():
    import pymysql
    db = pymysql.connect("52.66.105.87", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    database = {}
    sql = "SELECT * FROM `reminder` WHERE `notif`=0;"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for k in results:
            f1 = ""
            f2 = ""
            date = k[2].split('-')
            for l in date:
                f1 += str(int(l))
                f1 += " "
            f1 = f1[:-1]
            time = k[3].split(':')
            for l in time:
                f2 += str(int(l))
                f2 += " "
            f2 = f2[:-1]

            if date[-1] in database:
                if date[-2] in database[date[-1]]:
                    if date[-3] in database[date[-1]][date[-2]]:
                        if k[3] in database[date[-1]][date[-2]][date[-3]]:
                            if k not in database[date[-1]][date[-2]][date[-3]][k[3]]:
                                database[date[-1]][date[-2]][date[-3]][k[3]].append(k)
                        else:
                            database[date[-1]][date[-2]][date[-3]][k[3]] = []
                            database[date[-1]][date[-2]][date[-3]][k[3]].append(k)
                    else:
                        database[date[-1]][date[-2]][date[-3]] = {}
                        database[date[-1]][date[-2]][date[-3]][k[3]] = []
                        database[date[-1]][date[-2]][date[-3]][k[3]].append(k)
                else:
                    database[date[-1]][date[-2]] = {}

                    database[date[-1]][date[-2]][date[-3]] = {}
                    database[date[-1]][date[-2]][date[-3]][k[3]] = []
                    database[date[-1]][date[-2]][date[-3]][k[3]].append(k)
            else:
                database[date[-1]] = {}
                database[date[-1]][date[-2]] = {}
                database[date[-1]][date[-2]][date[-3]] = {}
                database[date[-1]][date[-2]][date[-3]][k[3]] = []
                database[date[-1]][date[-2]][date[-3]][k[3]].append(k)
        return database
    except:
        print "ERROR CHECKING Auth"

while True:
    database = getdata()
    for temp in database:
        if int(temp) == int(getdate()[-1]):
            for temp1 in database[temp]:
                if int(temp1) == int(getdate()[-2]):
                    for temp2 in database[temp][temp1]:
                        if int(temp2) == int(getdate()[-3]):
                            array = database[temp][temp1][temp2].keys()
                            array.sort()
                            for temp4 in array:
                                if temp4 > gettime():
                                    print 'TIME', difference_in_seconds(gettime(),temp4)
                                    if difference_in_seconds(gettime(),temp4) < 30 and difference_in_seconds(gettime(),temp4) > 0:
                                        print difference_in_seconds(gettime(),temp4)
                                        time.sleep(difference_in_seconds(gettime(),temp4))
                                        var = database[temp][temp1][temp2][temp4]
                                        for temp5 in var:
                                            mail_engine_reminder(getname(temp5[0]), temp5[1], temp5[2], temp5[3], getemail(temp5[0]))
                                            print 'SENT', temp5
                                            updatedb(temp5[0],temp5[1], temp5[2], temp5[3])

                                    elif difference_in_seconds(gettime(),temp4) < 0:
                                        var = database[temp][temp1][temp2][temp4]
                                        for temp5 in var:
                                            mail_engine_reminder(getname(temp5[0]), temp5[1], temp5[2], temp5[3], getemail(temp5[0]))
                                            print 'SENT', temp5
                                            updatedb(temp5[0], temp5[1], temp5[2], temp5[3])

                        elif int(temp2) < int(getdate()[-3]):
                            for temp3 in database[temp][temp1][temp2]:
                                for temp4 in database[temp][temp1][temp2][temp3]:
                                    mail_engine_reminder(getname(temp4[0]), temp4[1], temp4[2], temp4[3], getemail(temp4[0]))
                                    print 'SENT', temp4
                                    updatedb(temp4[0], temp4[1], temp4[2], temp4[3])


                elif int(temp1) < int(getdate()[-2]):
                    for temp2 in database[temp][temp1]:
                        for temp3 in database[temp][temp1][temp2]:
                            for temp4 in database[temp][temp1][temp2][temp3]:
                                mail_engine_reminder(getname(temp4[0]), temp4[1], temp4[2], temp4[3], getemail(temp4[0]))
                                print 'SENT', temp4
                                updatedb(temp4[0], temp4[1], temp4[2], temp4[3])


        elif int(temp) < int(getdate()[-1]):
            for temp1 in database[temp]:
                for temp2 in database[temp][temp1]:
                    for temp3 in database[temp][temp1][temp2]:
                        for temp4 in database[temp][temp1][temp2][temp3]:
                            mail_engine_reminder(getname(temp4[0]), temp4[1], temp4[2], temp4[3], getemail(temp4[0]))
                            print 'SENT', temp4
                            updatedb(temp4[0],temp4[1],temp4[2],temp4[3])
    print
    print
    print
    time.sleep(5)