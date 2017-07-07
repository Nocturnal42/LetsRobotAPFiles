import cgi
from subprocess import call

print "HTTP/1.1 302 Found"
print "Location: /"

form=cgi.FieldStorage()
ssid = form.getvalue("SSID")
password = form.getvalue("password")

wpa = open("/etc/wpa_supplicant/wpa_supplicant.conf", "w");

wpa.write("country=US\n")
wpa.write("ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n")
wpa.write("update_config=1\n")
wpa.write("network={\n")
wpa.write("   ssid=\"%s\"\n" % ssid)
wpa.write("   psk=\"%s\"\n" % password)
wpa.write("}\n")

wpa.close()

call(["wpa_cli -i wlan0 reconfigure > /dev/null"], shell=True)

print "Connection: close \r\n"
