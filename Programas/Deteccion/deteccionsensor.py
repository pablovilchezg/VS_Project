import RPi.GPIO as GPIO
import time
import os, commands, sys

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)
TACTIL_PIN = 27
GPIO.setup(TACTIL_PIN, GPIO.IN)
VIBRACION_PIN = 22
GPIO.setup(VIBRACION_PIN, GPIO.IN)


def MOTION(PIN):

    if PIN == TACTIL_PIN:
	    infile = open('/home/userpro/Project/Programas/Camara/notificaciones.txt', 'r')
	    notificaciones = infile.read()
	    infile.close()
	    infile = open('/home/userpro/Project/Programas/Camara/notificaciones.txt', 'w')
	    os.system('sudo killall telegram-cli')
	    os.system('sudo killall telegram-cli')
	    if notificaciones == "0":
		    infile.write('1')
		    os.system('/home/userpro/Project/Programas/Telegram/sendmsg_tg.sh Yo ' + 'Notificaciones_activadas')
	    else:
		    infile.write('0')
		    os.system('/home/userpro/Project/Programas/Telegram/sendmsg_tg.sh Yo ' + 'Notificaciones_desactivadas')
	    infile.close()
	    os.system('/home/userpro/Project/tg/bin/telegram-cli -k /home/userpro/Project/tg/server.pub -W -s /home/userpro/Project/tg/action.lua -d &')
	    

    else:
	    infile = open('/home/userpro/Project/Programas/Camara/notificaciones.txt', 'r')
	    notificaciones = infile.read()
	    if notificaciones == "1":
		    os.system('sudo killall telegram-cli')
		    os.system('sudo killall telegram-cli')
		    os.system('/home/userpro/Project/Programas/Camara/foto.sh')
		    timestr = time.strftime("%Y-%m-%d.%H:%M:%S")
		    if PIN == PIR_PIN:
			pindetectado = '_Movimiento'
		    else:
			pindetectado = '_Vibracion'
		    intrusionstr = 'Deteccion_' + timestr + pindetectado
		    os.system('/home/userpro/Project/Programas/Telegram/sendmsg_tg.sh Yo ' + intrusionstr)
		    os.system('/home/userpro/Project/Programas/Telegram/sendphoto_tg.sh Yo /home/userpro/Project/Multimedia/Fotos/last.jpg')

		    os.system('/home/userpro/Project/tg/bin/telegram-cli -k /home/userpro/Project/tg/server.pub -W -s /home/userpro/Project/tg/action.lua -d &')
	    infile.close()


def CONGELACION():
    	infil = open('/home/userpro/Project/Programas/Camara/notificaciones.txt', 'r')
	noti = infil.read()
	if noti == "1":
		res = commands.getstatusoutput('sudo python /home/userpro/Project/Programas/TempHum/DHT11.py 11 4')
		print(res)
		if (res[1][0:3] != 'Fail'):
		    if(float(res[1][0:3]) < 0):
			os.system('sudo killall telegram-cli')
			os.system('sudo killall telegram-cli')
			os.system('/home/userpro/Project/Programas/Telegram/sendmsg_tg.sh Yo ' + res[1] + '_riesgo_de_congelacion')
			os.system('/home/userpro/Project/tg/bin/telegram-cli -k /home/userpro/Project/tg/server.pub -W -s /home/userpro/Project/tg/action.lua -d &')
	infil.close()


print "Modulo de vigilancia"
print "Sistema iniciado"
os.system('sudo killall telegram-cli')
os.system('sudo killall telegram-cli')
os.system('/home/userpro/Project/tg/bin/telegram-cli -k /home/userpro/Project/tg/server.pub -W -s /home/userpro/Project/tg/action.lua -d &')

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    GPIO.add_event_detect(TACTIL_PIN, GPIO.RISING, callback=MOTION)
    GPIO.add_event_detect(VIBRACION_PIN, GPIO.RISING, callback=MOTION)
    while 1:
	CONGELACION()
        time.sleep(60)
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()

