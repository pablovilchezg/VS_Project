import time
import serial
import sys

def main(args):
	port = serial.Serial("/dev/serial0", baudrate=9600, timeout=3.0)
	txt=''

	var = "AT+CGPSSTATUS?\n"
	port.write(var)
	port.read( len(var) )
	time.sleep(2)
	txt = port.read(port.inWaiting())
	print (txt.count("Location 3D Fix"))
if __name__ == '__main__':
	main(sys.argv)
