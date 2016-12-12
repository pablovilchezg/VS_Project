import time
import serial

port = serial.Serial("/dev/serial0", baudrate=9600, timeout=3.0)
txt=''

var = "AT+CGPSINF=0\n"
port.write(var)
port.read( len(var) )
time.sleep(2)
txt = port.read(port.inWaiting())
site = txt.find("+CGPSINF:")
site = site + 12

print (txt[site:(site+19)] + txt[(site+30):(site+31+14)])
