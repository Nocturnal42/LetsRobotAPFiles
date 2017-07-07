import cgi
from subprocess import call

print "HTTP/1.1 302 Found"
print "Location: /"

form=cgi.FieldStorage()
bright = form.getvalue("brightness")

call(["/usr/bin/v4l2-ctl --set-ctrl brightness=%s > /dev/null" % bright ], shell=True) 

print "Connection: close \r\n"
