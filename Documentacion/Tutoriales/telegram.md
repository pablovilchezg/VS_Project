#Usar Telegram en Raspberry

##Clonar y compilar telegram

Ejecutamos lo siguiente para instalar y compilar telegram

```

sudo apt-get install libreadline-dev libconfig-dev libssl-dev lua5.2 liblua5.2-dev libevent-dev make
git clone --recursive https://github.com/vysheng/tg.git && cd tg
./configure --disable-json
make

```


##Ejecutar telegram

Ejecutamos el cliente de telegram:


```

bin/telegram-cli -k tg-server.pub -W

```

La primera vez nos pedirá el numero de telefono y luego la clave que nos mandan.

Si nos lanza el error **telegram-cli: tgl/mtproto-utils.c:101: BN2ull: Assertion `0' failed**, simplemente comentamos la línea 101 en ese archivo y volvemos a hacer **make**

Ahora podemos ejecutar comandos para hablar con quien queramos o mandar archivos y multimedia

##Ejecución automatica ante mensajes

Si queremos automatizar que cuando le enviemos un mensaje clave a la raspberry nos conteste con
lo que queramos automatizar, lo haremos con un action.lua que pondremos en la ejecución del cliente


En el archivo action.lua metemos lo siguiente

```

function on_msg_receive (msg)
      if msg.out then
          return
      end
      if (msg.text=='ping') then
         send_msg (msg.from.print_name, 'pong', ok_cb, false)
      end
  end

  function on_our_id (id)
  end

  function on_secret_chat_created (peer)
  end

  function on_user_update (user)
  end

  function on_chat_update (user)
  end

  function on_get_difference_end ()
  end

  function on_binlog_replay_end ()
  end

```

También podemos automatizar que nos mande una foto:

- Creamos un fichero foto.sh que ejecutara para crear la foto con el siguiente
contenido

```

#!/bin/bash

  raspistill -w 1920 -h 1080 -o /home/userpro/Project/Multimedia/Fotos/foto.jpg

```

- Cambiamos los permisos para que se pueda ejecutar

```

sudo chmod -R 0655 /home/userpro/Project/Programas/Camara/foto.sh

```

- Editamos action.lua con el siguiente contenido

```

if (msg.text=='foto') then
     os.execute('/home/userpro/Project/Programas/Camara/foto.sh')
     send_photo (msg.from.print_name, '/home/userpro/Project/Multimedia/Fotos/foto.jpg', ok_cb, false)
  end

```

- Ejecutamos telegram-cli

```

/home/userpro/Project/tg/bin/telegram-cli -k /home/userpro/Project/tg/tg-server.pub -W -s /home/userpro/Project/tg/action.lua

```

También podemos crear un script bash para ejecutar el envio de una foto.
El primer parametro es a quien lo envias y el segundo el path de la foto
**sendphoto.sh**

```

#!/bin/bash
to=$1
msg=$2
tgpath=/home/userpro/Project/tg
(echo "send_photo $to $msg"; echo "safe_quit") | ${tgpath}/bin/telegram-cli -k ${tgpath}/tg-server.pub -W

```

##Bibliografia

http://www.instructables.com/id/Raspberry-remote-control-with-Telegram/
http://www.blog.emmeshop.eu/?q=node/44
