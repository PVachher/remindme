import time
from modules import mail_engine_reminder, getname, getemail
database = {}
def difference_time(time_to_reach,time_reached):
    time_to_reach = str(time_to_reach).split(':')
    time_reached = time_reached.split(':')
    z1 = int(time_to_reach[-3]) - int(time_reached[0])
    z2 =int(time_to_reach[-2]) - int(time_reached[1])
    z3 = int(time_to_reach[-1]) - int(time_reached[2])
    return z1*(3600)+z2*(60) + z3

def convert_to_ist(timestr):
    timestr = timestr.spilt()

def getdate():
    localtime = time.localtime(time.time())
    year = localtime[0]
    month =localtime[1]
    date = localtime[2]
    print date, month, year
def gettime():
    localtime = time.localtime(time.time())
    hour = localtime[3]
    minute = localtime[4]
    seconds = localtime[5]
    print hour, minute, seconds
def getdata():
    global database
    import pymysql
    db = pymysql.connect("52.66.149.217", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    data = []
    sql = "SELECT * FROM `reminder` WHERE `notif`=0;"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
#        return results
        for k in results:
            final = ""
            z = k[-3]
            z = z.split('-')
            final += z[-1]
            final += ":"
            final += z[-2]
            final += ":"
            final += z[-3]
            final += ":"
            final += k[-2]
            data.append(final)
            if final not in database:
                database[final] = []
                database[final].append([k[0],k[1],k[2],k[3]])
            else:
                if [k[0],k[1],k[2],k[3]] in database[final]:
                    pass
                else:
                    database[final].append([k[0],k[1],k[2],k[3]])
            print "DATABASE", database
        return data

    except:
        print "ERROR CHECKING Auth"

def updatedb(username,data,date,time):
    import pymysql
    db = pymysql.connect("52.66.149.217", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    sql = "UPDATE reminder SET notif= 1\
                   WHERE username = '%s' AND reminder_data = '%s' AND reminder_date = '%s' AND reminder_time='%s'" % (username,data,date,time)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "ERROR Updating Auth"


while True:
    time.sleep(2)
    time1 = getdata()
    time1.sort()
    localtime = time.localtime(time.time())
    time_reached = str(localtime[3]) + ":" + str(localtime[4]) + ":" + str(localtime[5])
    for k in time1:
        print time_reached
        print k, difference_time(k,time_reached)
        if difference_time(k,time_reached) < 30:
            print "DIFF LESS THAN 30"
            if difference_time(k,time_reached) < 0:
                pass
            else:
                time.sleep(difference_time(k,time_reached))
            print "ITS TIME"
            for z in database[k]:
                print database[k],z
                updatedb(z[0],z[1],z[2],z[3])
                mail_engine_reminder(getname(z[0]),z[1],z[2],z[3],getemail(z[0]))
            localtime = time.localtime(time.time())
            print gettime()
            time_reached = str(localtime[3]) + ":" + str(localtime[4]) + ":" + str(localtime[5])
            print ""
        else:
            print "DIFF MORE THAN 30"
            break
