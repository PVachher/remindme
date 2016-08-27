url = "http://bhashsms.com/api/sendmsg.php?user=9811224261&pass=c54a98b&sender=TESTTO&phone=" + raw_input("Enter Mobile Number") + "&text=Test%20SMS&priority=ndnd&stype=normal"
import urllib2
z= urllib2.urlopen(url)
z = z.read()
print z