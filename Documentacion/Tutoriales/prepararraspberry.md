#Preparar el sistema operativo raspbian y configurarlo

Descargamos la ultima versión de berryboot con la que instalaremos el sistema

http://www.berryterminal.com/doku.php/berryboot

Formateamos la tarjeta SD a FAT32 y copiamos los archivos que contiene el zip descargado
de la web de berryboot

Enchufamos la raspberry, ponemos la configuración necesaria de internet, teclado, overscan
y audio/video.
A continuación aparecerá la información de los sistemas operativos, selecionamos el raspbian
y esperamos a que termine el proceso, al reinicio ya arrancará nuestro nuevo sistema.

##Pasos para configuración

Ejecutaremos un update y upgrade para que el sistema este actualizado

Podemos ejecutar la configuración de la raspberry y configurar algunas opciones, también tenemos
que descomentar la línea en */etc/fstab* que monta la partición */boot* y reiniciamos para poder
abrir raspi-config

```

sudo nano /etc/fstab
sudo raspi-config

```

Ahora tenemos un sistema con nombre de *usuario* **pi** y *contraseña* **raspberry**, por lo que cambiaremos
todo esto por motivos de seguridad, además de configurar el acceso por ssh para obtener la mayor
seguridad posible para el acceso ssh.



###Configuramos ssh

Para poder acceder desde ssh al usuario **root** para poder administrar la cuenta **pi**.
Para esto tenemos que copiar el siguiente fichero en */etc/ssh/sshd_config*

```

# Package generated configuration file
# See the sshd_config(5) manpage for details

# What ports, IPs and protocols we listen for
Port 2222
# Use these options to restrict which interfaces/protocols sshd will bind to
#ListenAddress ::
#ListenAddress 0.0.0.0
Protocol 2
# HostKeys for protocol version 2
HostKey /etc/ssh/ssh_host_rsa_key
HostKey /etc/ssh/ssh_host_dsa_key
HostKey /etc/ssh/ssh_host_ecdsa_key
HostKey /etc/ssh/ssh_host_ed25519_key
#Privilege Separation is turned on for security
UsePrivilegeSeparation yes

# Lifetime and size of ephemeral version 1 server key
KeyRegenerationInterval 3600
ServerKeyBits 1024

# Logging
SyslogFacility AUTH
LogLevel INFO

# Authentication:
LoginGraceTime 20
PermitRootLogin yes
StrictModes yes

RSAAuthentication yes
PubkeyAuthentication yes
#AuthorizedKeysFile	%h/.ssh/authorized_keys

# Don't read the user's ~/.rhosts and ~/.shosts files
IgnoreRhosts yes
# For this to work you will also need host keys in /etc/ssh_known_hosts
RhostsRSAAuthentication no
# similar for protocol version 2
HostbasedAuthentication no
# Uncomment if you don't trust ~/.ssh/known_hosts for RhostsRSAAuthentication
#IgnoreUserKnownHosts yes

# To enable empty passwords, change to yes (NOT RECOMMENDED)
PermitEmptyPasswords no

# Change to yes to enable challenge-response passwords (beware issues with
# some PAM modules and threads)
ChallengeResponseAuthentication no

# Change to no to disable tunnelled clear text passwords
#PasswordAuthentication yes

# Kerberos options
#KerberosAuthentication no
#KerberosGetAFSToken no
#KerberosOrLocalPasswd yes
#KerberosTicketCleanup yes

# GSSAPI options
#GSSAPIAuthentication no
#GSSAPICleanupCredentials yes

X11Forwarding yes
X11DisplayOffset 10
PrintMotd no
PrintLastLog yes
TCPKeepAlive yes
#UseLogin no

MaxStartups 2
MaxAuthTries 2
#Banner /etc/issue.net

# Allow client to pass locale environment variables
AcceptEnv LANG LC_*

Subsystem sftp /usr/lib/openssh/sftp-server

# Set this to 'yes' to enable PAM authentication, account processing,
# and session processing. If this is enabled, PAM authentication will
# be allowed through the ChallengeResponseAuthentication and
# PasswordAuthentication.  Depending on your PAM configuration,
# PAM authentication via ChallengeResponseAuthentication may bypass
# the setting of "PermitRootLogin without-password".
# If you just want the PAM account and session checks to run without
# PAM authentication, then enable this but set PasswordAuthentication
# and ChallengeResponseAuthentication to 'no'.
UsePAM yes

```

En definitiva lo que hemos camibado es el puerto, no permitir el root login y
añadir cuantas sesiones ssh y cuantos intentos podemos hacer para entrar.
Protocol siempre tiene que estar en 2, ya que el 1 es inseguro y tiempo que podemos
estar metiendo la contraseña 20 segudos.

```

Port 2222
Protocol 2
LoginGraceTime 20
PermitRootLogin no
MaxStartups 2
MaxAuthTries 2

```


###Cambio de nombre de usuario y contraseña

Como primer paso, en la configuración raspi-config ponemos que se inicie en modo consola, para que
podamos acceder directamente como usuario root y configuremos el usuario pi y su home. Además de
que podremos optar por iniciar la interfaz gráfica con startx o seguir en modo terminal.

Antes tenemos que ponerle contraseña al *root* desde el usuario *pi*

```

sudo passwd root

```
Ponemos la nueva contraseña y ya podemos acceder desde la terminal principal al usuario *root* desde
la que ejecutaremos los siguiente comandos para cambiar el nombre de usuario, el home y la contraseña:

```

passwd pi
usermod -l nombrenuevo pi
mv /home/pi /home/nombrenuevo
groupmod -n nombrenuevo pi

```

Al terminar la configuración, cambiaremos en el fichero de configuración el **PermitRootLogin** de *yes* a *no*,
para que no se pueda realizar el acceso a **root** por ssh

###Escritorio remoto

Si queremos tener un escritorio remoto, instalaremos un servidor vnc para tener un escritorio y acceder
remotamente. Para ello escribimos en el terminal:

```

sudo apt-get install tightvncserver

```

Una vez terminada la instalación, ejecutaremos un escritorio con el siguiente comando:

```

vncserver -geometry 800x600 -depth 24 :0

```

Donde geometry es la geometria de la pantalla donde vamos a visualizar el escritorio, depth la profundidad
de bits por pixel y :0 el escritorio que vayamos a tener, el 0, 1, 2 ... y ponemos una contraseña la primera
vez que lo ejecutamos, la cual será la que nos pida siempre que queramos ver ese escritorio.
Para acceder por ssh y tener una visualización segura de la pantalla, accedemos con este comando

```

ssh userpro@192.168.1.37 -p 3223 -L5900:localhost:5900

```

Ahora en local, podremos ejecutar vncviewer del display 0, ingresamos la contraseña para ver la pantalla
y ya tenemos el escritorio de la raspberry

```

vncviewer :0

```

###Acceso remoto a la raspberry

Para acceder remotamente configuramos nuestro router con el servicio NOIP para darle un dominio a nuestra
IP y poder acceder cuando queramos a ella. Lo que tenemos que hacer en la raspberry es modificar el archivo
*/etc/network/interfaces* donde fijaremos que la interfaz *wlan* le de una IP fija a la subred local para
poder redireccionar las peticiones ssh desde el exterior a la IP de la raspberry a la que queremos acceder.
Modificamos el apartado del archivo que configura la interfaz wlan para asignar una IP estatica

```

# interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d

auto lo
iface lo inet loopback

iface eth0 inet manual

allow-hotplug wlan0
iface wlan0 inet static
address 192.168.1.199
gateway 192.168.1.1
netmask 255.255.255.0
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

allow-hotplug wlan1
iface wlan1 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

```

Los cambios son que ponemos la interfaz con ip estatica y le damos la dirección, puerta de enlace
y mascara de subred.
Reiniciamos y ya podemos acceder remotamente, hacer túneles, etc.


##Ejecutar programas en el inicio

Por ejemplo creamos el siguiente programa en **/etc/init.d/detector-init**:

```

#! /bin/sh
# /etc/init.d/detector-init
 
### BEGIN INIT INFO
# Provides:          detector-init
# Required-Start:    $all
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Script de ejemplo de arranque automático
# Description:       Script para arrancar el detector de presencia
### END INIT INFO
 
 
# Dependiendo de los parámetros que se le pasen al programa se usa una opción u otra
case "$1" in
  start)
    echo "Arrancando detector-init"
    # Aquí hay que poner el programa que quieras arrancar automáticamente
    /usr/bin/python /home/pi/detector.py
    ;;
  stop)
    echo "Deteniendo detector-init"
 
    ;;
  *)
    echo "Modo de uso: /etc/init.d/detector-init {start|stop}"
    exit 1
    ;;
esac
 
exit 0

```

Después ejecutamos los siguientes comandos y ya lo tenemos:

```

sudo chmod 755 /etc/init.d/detector-init
sudo update-rc.d detector-init defaults

```



##Bibliografia


https://nideaderedes.urlansoft.com/2013/12/20/como-ejecutar-un-programa-automaticamente-al-arrancar-la-raspberry-pi/
http://elinux.org/RPi_VerifiedPeripherals (Periféricos verificados para raspberry)
