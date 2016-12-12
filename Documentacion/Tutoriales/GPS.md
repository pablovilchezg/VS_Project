#Uso del GPS por UART SIM808


###Habilitar el puerto serie

Previamente, con raspi-config habilitamos el puerto serie. Una vez realizado, ya podemos
escribir un programa para comunicarnos con el GPS.

##Puerto serie con Python

Escribir el siguiente programa y ejecutarlo con *sudo python programagps.py*

```python

import time
import serial

port = serial.Serial("/dev/serial0", baudrate=9600, timeout=3.0)
txt=''

while True:
    port.write("AT+CGPSINF=0\n")
    time.sleep(2)
    txt = port.read(port.inWaiting())
    print txt

```
```
   AT+CGPSINF=0\n
```
Lo podremos sustituir por el comando AT que queramos mandarle al GPS y obtendremos su respuesta
que tendremos en txt


##Bibliografia


http://www.elinux.org/Serial_port_programming
http://www.elinux.org/RPi_Serial_Connection#Preventing_Linux_using_the_serial_port
http://technikegge.blogspot.com.es/

SIM808

P.S.
The link to download the instructions
- https://www.dropbox.com/s/ocigkcxi5hkzgv2/Breakout%20SIM808%20Board-EN%20V2.1.rar?dl=0

Other helpful links:
1. SIM808 with Arduino:
http://www.dfrobot.com/wiki/index.php?title=SIM808_with_Leonardo_mainboard_SKU:DFR0355
http://www.elecrow.com/wiki/index.php?title=Elecrow_SIMduino_UNO%2BSIM808_GPRS/GSM_Board
2. SIM808 Arduino Library: https://github.com/leffhub/DFRobotSIM808_Leonardo_mainboard/raw/master/Library/SIM808.zip
3. similar SIM808 Board: http://www.seeedstudio.com/wiki/Mini_GSM/GPRS_%2B_GPS_Breakout_-_SIM808


https://github.com/yangguozhanzhao/sim808/blob/master/test.py(Supuestamente un ejemplo para programar en python el sim808)

https://github.com/jojo-/Trackduino/tree/master/web(Otro programa)

http://raspberrypi.stackexchange.com/questions/50913/raspberry-pi-3-with-sim808-7inch-display-module-issues-in-communication-uart (Resolucion de problema con UART)
