#Crear punto de acceso

##Requisitos

Instalar hostapd y udhcpd:

```

sudo apt-get install hostapd udhcpd

```

##Configuramos el udhcpd y hostapd

Para ello, ponemos los siguientes parámetros en el fichero */etc/udhcpd.conf*

```

start 192.168.42.2 # This is the range of IPs that the hostspot will give to client devices.
end 192.168.42.20
interface wlan0 # The device uDHCP listens on.
remaining yes
opt dns 8.8.8.8 4.2.2.2 # The DNS servers client devices will use.
opt subnet 255.255.255.0
opt router 192.168.42.1 # The Pi's IP address on wlan0 which we will set up shortly.
opt lease 864000 # 10 day DHCP lease time in seconds

```

En el fichero */etc/default/udhcpd* comentamos las ĺineas siguientes, para que quede así:

```

DAEMON_CONF="/etc/hostapd/hostapd.conf"
#DHCPD_ENABLED="no"

```

Ahora creamos el fichero */etc/hostapd/hostapd.conf* y ponemos los siguiente:

```

interface=wlan0
driver=nl80211
ssid=Rasp
hw_mode=g
channel=6
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=holaquetal
wpa_key_mgmt=WPA-PSK
#wpa_pairwise=TKIP	# You better do not use this weak encryption (only used by old client devices)
rsn_pairwise=CCMP
ieee80211n=1          # 802.11n support
wmm_enabled=1         # QoS support
ht_capab=[HT40][SHORT-GI-20][DSSS_CCK-40]

```

##Configuramos los interfaces

Modificaremos el fichero */etc/network/interfaces* quedando así:

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
address 192.168.42.1
netmask 255.255.255.0

allow-hotplug wlan1
iface wlan1 inet static
address 192.168.1.199
gateway 192.168.1.1
netmask 255.255.255.0
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

```
##Configuramos el NAT

Editamos el archivo */etc/sysctl.conf* y añadimos la línea siguiente al final:

```

net.ipv4.ip_forward=1

```

Para que siempre al inicio del sistema se le asigne wlan0 al interface wifi integrado
en la raspberry y wlan1 al otro por usb crear */etc/udev/rules.d/70-persistent-net.rules*
e introducir lo siguiente, cambiando en ATTR y poniendo la mac del interface:

```

ACTION=="add", SUBSYSTEM=="net", DRIVERS=="?*", ATTR{address}=="11:11:11:11:11:11", NAME="wlan0"

ACTION=="add", SUBSYSTEM=="net", DRIVERS=="?*", ATTR{address}=="22:22:22:22:22:22", NAME="wlan1"

```

##Configuramos tablas de enrutamento

Los siguientes comandos configuran iptables, pero no se hacen permanentes, probar
primero y si funcionan, hacerlos permanentes

```

sudo iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE
sudo iptables -A FORWARD -i wlan1 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i wlan0 -o wlan1 -j ACCEPT

```

##Ejecutar punto de acceso

Para ello levantamos los servicios:

```

sudo service hostapd start
sudo service udhcpd start

```

##Fijar configuracion de enrutamiento y ejecución de punto de acceso

Para fijar iptables, después de tener ejecutados los anteriores comandos de iptables, ejecutar éstos:

```

sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"

```
Y ahora editamos */etc/network/interfaces*, al final del archivo introducimos:

```

up iptables-restore < /etc/iptables.ipv4.nat

```

Para que los servicios arranquen al inicio del sistema:

```

sudo update-rc.d hostapd enable
sudo update-rc.d udhcpd enable

```


##Bibliografia

http://elinux.org/RPI-Wireless-Hotspot
https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=132187
