import subprocess

print "Currently connected to: "
proc = subprocess.Popen(["/sbin/iwgetid", "-s", "wlan0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output=proc.stdout.read()

if output:
    print output.splitlines()
else:
     print "None"



