#!/usr/bin/python

#apt-get install python-dev
#apt-get install python-setuptools
#easy_install -U distribute
#pip install rpi.gpio
 
from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
 
lcd = Adafruit_CharLCD()
 
cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
 
lcd.begin(16,1)
 
def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

i = "" 
while 1:
        lcd.clear()
        ipaddr = run_cmd(cmd)
        #print ipaddr
        lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
        lcd.message('IP %s' % ( ipaddr ))
        #i = i+" "
        #if len(i)>15: i = ""
        #lcd.message(i+'Noemie !!')
        sleep(2)
