import time
database = {}

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
    global database
    import pymysql
    db = pymysql.connect("52.66.105.87", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    data = []
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
                            database[date[-1]][date[-2]][date[-3]][k[3]].append(k)
                        else:
                            database[date[-1]][date[-2]][date[-3]][k[3]] = []
                            database[date[-1]][date[-2]][date[-3]][k[3]].append(k)
                    else:
                        database[date[-1]][date[-2]][date[-3]] = []
                        database[date[-1]][date[-2]][date[-3]][k[3]] = []
                        database[date[-1]][date[-2]][date[-3]][k[3]].append(k)
                else:
                    database[date[-1]][date[-2]] = {}
                    database[date[-1]][date[-2]][date[-3]] = []
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

print getdate()
print getdata()

for temp in database:
    if int(temp) == int(getdate()[-1]):
        for temp1 in database[temp]:
            if int(temp1) == int(getdate()[-2]):
                for temp2 in database[temp][temp1]:
                    print temp2
                    print getdate()[-3]
                    if int(temp2) == int(getdate()[-3]):
                        array = database[temp][temp1][temp2]
                        array.sort()
                        print array

                    elif int(temp2) == int(getdate()[-3]):
                        for temp3 in database[temp][temp1][temp2]:
                            for temp4 in database[temp][temp1][temp2][temp3]:
                                print 'SENT', temp4

            elif int(temp1) < int(getdate()[-2]):
                for temp2 in database[temp][temp1]:
                    for temp3 in database[temp][temp1][temp2]:
                        for temp4 in database[temp][temp1][temp2][temp3]:
                            print 'SENT', temp4

    elif int(temp) < int(getdate()[-1]):
        for temp1 in database[temp]:
            for temp2 in database[temp][temp1]:
                for temp3 in database[temp][temp1][temp2]:
                    for temp4 in database[temp][temp1][temp2][temp3]:
                        print 'SENT', temp4