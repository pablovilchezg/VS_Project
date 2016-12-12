#Modem 3G

Descargamos sakis3g

Los comandos son:

```

sudo apt-get install ppp
sudo wget "http://www.sakis3g.com/downloads/sakis3g.tar.gz" -O sakis3g.tar.gz
sudo tar -xzvf sakis3g.tar.gz
sudo chmod +x sakis3g
./sakis3g --interactive

```

Una vez comprobado el funcionamiento, creamos el fichero */etc/sakis3g.conf* e introducimos los siguiente:

```

MODEM="12d1:1001"
SIM_PIN="****"
APN="movistar.es"

```

Y ya podemos ejecutar desde la terminal lo siguiente, que conectará automáticamente y no tendremos que
interactuar con el programa:

```

sudo ./sakis3g connect

```

Para ponerlo como un servicio que se inicie al sistema y nos conectemos automaticamente a internet, crearemos
el archivo **/etc/init.d/sakis** con el siguiente contenido:

```

#! /bin/bash
### BEGIN INIT INFO
# Provides: Arranca el 3G
# Required-Start: $syslog
# Required-Stop: $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: arranque automatico para el 3g
# Description:
#
### END INIT INFO

case "$1" in
  start)
    echo "Arrancando 3G"
    sudo /home/userpro/Project/sakis3g/sakis3g connect
    sudo service noip2 restart
    ;;
  stop)
    echo "Deteniendo 3G"
    sudo /home/userpro/Project/sakis3g/sakis3g disconnect
    ;;
  restart)
    echo "Deteniendo 3G"
    sudo /home/userpro/Project/sakis3g/sakis3g disconnect
    echo "Arrancando 3G"
    sudo /home/userpro/Project/sakis3g/sakis3g connect
    sudo service noip2 restart
    ;;
  *)
    echo "Modo de uso: /etc/init.d/sakis {start|stop|restart}"
    exit 1
    ;;
esac
 
exit 0


```
Actualizamos permisos y inicio del sistema

```

sudo chmod +x /etc/init.d/sakis
sudo update-rc.d sakis defaults

```

##Bibliografia


http://www.sakis3g.com/#comments
http://raspberry-at-home.com/installing-3g-modem/
