#Servidor para camara

##Instalacion de paquetes

Ejecutamos los siguientes comandos en la raspberry:

```

cd /usr/src
sudo mkdir mjpg-streamer
sudo chown `whoami`:users mjpg-streamer
cd mjpg-streamer
git clone https://github.com/jacksonliam/mjpg-streamer.git .
sudo apt-get install libv4l-dev libjpeg8-dev imagemagick build-essential cmake subversion
cd mjpg-streamer-experimental
make

```

##Ejecucion

Para ejecutar el servidor de video:

```

export LD_LIBRARY_PATH=/usr/src/mjpg-streamer/mjpg-streamer-experimental/
/usr/src/mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 640 -y 480 -fps 20 -ex night"

```


##Bibliografia

http://petrkout.com/electronics/low-latency-0-4-s-video-streaming-from-raspberry-pi-mjpeg-streamer-opencv/
