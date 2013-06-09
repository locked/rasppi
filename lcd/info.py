#!/usr/bin/python

#apt-get install python-dev
#apt-get install python-setuptools
#easy_install -U distribute
#pip install rpi.gpio
 
from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import requests
import json

try: 
    lcd = Adafruit_CharLCD()
    lcd.begin(16,1)
except:
    pass

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

nagios_url = "http://mon.lunasys.fr/nagios/json.php"

while 1:
    lcd.clear()
    lcd.message(datetime.now().strftime('%d/%m %H:%M\n'))

    msgs = []

    r = requests.get(nagios_url)
    #print r.text
    try:
        nag = r.json
        #print nag
        if len(nag)>0:
            msgs.append("NagWarn:%d" % len(nag))
    except Exception as e:
        print e
        pass

    lcd.message("/".join(msgs))
    sleep(2)
