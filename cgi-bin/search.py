import subprocess
import re
import string

proc = subprocess.Popen(["/sbin/iwlist", "wlan0", "scan"], stdout=subprocess.PIPE, \
                                                     stderr=subprocess.PIPE)
output=proc.stdout.read()
for line in output.splitlines():
    m = re.search("ESSID:\".+\"", line)
    if m:
        print (re.split('"', line))[1]

