#PIR Motion Sensor

##Configuración del sensor de movimiento

Para la utilización del sensor, identificamos las patillas de alimentación
del sensor y la patilla que cambiará de estado cuando detecte movimiento.

![pinoutpir](./Imagenes/PIRsensor.png "Pines del sensor")

La salida nos dara un pulso alto (3V) cuando se detecte una presencia, y estará en nivel bajo mientras no se detecte nada
Es capaz de detectar a 6 metro con un rango de 110 x 70 grados
La alimentación puede ir de 3V a 9V, siendo el ideal 5V

Con los tornillos de ajuste podemos ajustar dos parámetros:
· Con Delay Time cambiamos el tiempo que permanece la salida en alto después de detectar la presencia
· Con Sensitive, ajustamos si queremos que se detecte la presencia con más o menos facilidad

También tenemos un jumper, con el que seleccionamos o la opción H o la opción L. Con la H la salida estará en alta mientras esté detectando, y con L mientras detecte estará cambiando de baja a alta.

![pirtornillosajuste](./Imagenes/pirtornillosajuste.jpg "Funciones sensor PIR")


##Codigo para usarlo

Generamos un codigo para usar el sensor, con un led que nos avisa cuando cambia de estado la salida del sensor.

Implementaremos el hardware de la siguiente forma:

![pirconexiones](./Imagenes/pircon.jpg "Conexión del PIR para probarlo")

Podemos utilizar el siguiente código para probar el funcionamiento

```python

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
while True:
       i=GPIO.input(11)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             GPIO.output(3, 0)  #Turn OFF LED
             time.sleep(0.1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             GPIO.output(3, 1)  #Turn ON LED
             time.sleep(0.1)

```

El anterior consume mucha CPU, por lo que para la implementación final, utilizaremos éste otro código

```python

import RPi.GPIO as GPIO
import time

boolean = 0
GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)
def MOTION(PIR_PIN):
    global boolean
    if boolean == 0:
        print "Motion Detected"
        boolean = 1
    else:
        print "No hay motion"
        boolean = 0
print "PIR Module Test (CTRL+C to exit)"
time.sleep(2)
print "Ready"

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.BOTH, callback=MOTION)
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()


```

##Bibliografia

http://www.tweaking4all.com/hardware/pir-sensor/
http://diyhacking.com/raspberry-pi-gpio-control/
