#Configurar noip

##Instalacion

Ejecutamos los siguientes comandos:

```

mkdir no-ip
cd no-ip
wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
tar -zxvf noip-duc-linux.tar.gz
cd noip-2.1.9-1/
make
sudo make install

```


##Inicio de  noip

Ahora lo establecemos para que se inicie con el sistema, creando el siguiente archivo **/etc/init.d/noip2**:

```

#! /bin/bash
### BEGIN INIT INFO
# Provides: Servicio No-IP
# Required-Start: $syslog
# Required-Stop: $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: arranque automatico para no-ip
# Description:
#
### END INIT INFO

case "$1" in
  start)
    echo "Arrancando noip"
    sudo /usr/local/bin/noip2
    ;;
  stop)
    echo "Deteniendo noip"
    sudo killall noip2
    ;;
  restart)
    echo "Deteniendo noip"
    sudo killall noip2
    echo "Arrancando noip"
    sudo /usr/local/bin/noip2
    ;;
  *)
    echo "Modo de uso: /etc/init.d/noip2 {start|stop|restart}"
    exit 1
    ;;
esac
 
exit 0

```

Actualizamos permisos y inicio del sistema

```

sudo chmod +x /etc/init.d/noip2
sudo update-rc.d noip2 defaults

```

##Bibliografia

https://geekytheory.com/tutorial-raspberry-pi-7-escritorio-remoto-vnc-no-ip/
