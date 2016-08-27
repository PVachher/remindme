def nondndsms(mobilenumber):
    url = "http://bhashsms.com/api/sendmsg.php?user=9811224261&pass=GK2online(sms)&sender=EXCLNT&phone=" + str(mobilenumber) + "&text=Testing%20SMSEngine%20&priority=ndnd&stype=normal"
    import urllib2
    print url
    z= urllib2.urlopen(url)
    z = z.read()
    print z
