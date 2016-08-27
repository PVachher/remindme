def dndsms(mobilenumber):
    url = "http://bhashsms.com/api/sendmsg.php?user=9811224261&pass=GK2online(sms)&sender=GKERWA&phone=" + str(mobilenumber) + "&text=Test%20SMS&priority=ndnd&stype=normal"
    import urllib2
    z= urllib2.urlopen(url)
    z = z.read()
    print z