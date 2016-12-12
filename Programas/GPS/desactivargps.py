import time
import serial

port = serial.Serial("/dev/serial0", baudrate=9600, timeout=3.0)
txt=''

var = "AT+CGPSPWR=0\n"
port.write(var)
port.read( len(var) )
time.sleep(2)
txt = port.read(port.inWaiting())
print txt
