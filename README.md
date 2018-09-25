# samsung-exlink-remote


create /etc/udev/rules.d/99-usb-serial.rules

Replace VendorID, Product ID, find serial via 
udevadm info -a -n /dev/ttyUSB0 | grep '{serial}' | head -n1

    SUBSYSTEM=="tty", ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303",
    ATTRS{serial}=="SERIAL", SYMLINK+="NAMEOFDEVICE"

python samsungtv.py 'ARG'

command options:  
vardict={
'tvon':"\x08\x22\x00\x00\x00\x02\xd4",
'tvoff':"\x08\x22\x00\x00\x00\x01\xd5",
'mute':"\x08\x22\x02\x00\x00\x02\xd4",
'hdmi1':"\x08\x22\x0a\x00\x05\x00\xc7",
'hdmi2':"\x08\x22\x0a\x00\x05\x01\xc6",
'back20':"\x08\x22\x0b\x01\x00\x14\xb6",}
