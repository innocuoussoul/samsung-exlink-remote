#!/usr/bin/env python
import time, serial, sys
ser = serial.Serial(port='/dev/pgmtvleft', baudrate=9600, timeout=1)
resp=""
loop="true"
string="030cf1"

vardict={
'tvon':"\x08\x22\x00\x00\x00\x02\xd4",
'tvoff':"\x08\x22\x00\x00\x00\x01\xd5",
'mute':"\x08\x22\x02\x00\x00\x02\xd4",
'hdmi1':"\x08\x22\x0a\x00\x05\x00\xc7",
'hdmi2':"\x08\x22\x0a\x00\x05\x01\xc6",
'back20':"\x08\x22\x0b\x01\x00\x14\xb6",}


hexcode = vardict.get(sys.argv[1])
print hexcode
while loop:
  if string in resp:
    print "found it"
    break
    ser.close()
  else:
    ser.write(hexcode)
    data = ser.read(24)
    resp=data.encode('hex')
    print resp
    time.sleep(1)
print "finished"
