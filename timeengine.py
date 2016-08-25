import time
def difference_time(time_to_reach,time_reached):
    time_to_reach = str(time_to_reach).split(':')
    time_reached = time_reached.split(':')
    z1 = int(time_to_reach[0]) - int(time_reached[0])
    z2 =int(time_to_reach[1]) - int(time_reached[1])
    z3 = int(time_to_reach[2]) - int(time_reached[2])
    return z1*(3600)+z2*(60) + z3
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
    import pymysql
    db = pymysql.connect("52.66.46.128", "root", "Welcome123", "remindme")
    cursor = db.cursor()
    data = []
    sql = "SELECT * FROM reminder "
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for k in results:
            final = ""
            z = k[-2]
            z = z.split('-')
            final += z[-1]
            final += ":"
            final += z[-2]
            final += ":"
            final += z[-3]
            final += ":"
            final += k[-1]
            data.append(final)
        return data
    except:
        print "ERROR CHECKING Auth"





while True:
    time1 = getdata()
    time1.sort()
    localtime = time.localtime(time.time())
    time_reached = str(localtime[3]) + ":" + str(localtime[4]) + ":" + str(localtime[5])
    for k in time1:
        print k
        time.sleep(difference_time(k,time_reached))
        print "ITS TIME"
        localtime = time.localtime(time.time())
        print gettime()
        print ""
        localtime = time.localtime(time.time())
        time_reached = str(localtime[3]) + ":" + str(localtime[4]) + ":" + str(localtime[5])