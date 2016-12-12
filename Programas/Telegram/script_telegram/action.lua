function on_msg_receive (msg)
      if msg.out then
          return
      end
      if (msg.text=='ping') then
         send_msg (msg.from.print_name, 'pong', ok_cb, false)
      end
      if (msg.text=='actnot') then
         archivo = io.open("/home/userpro/Project/Programas/Camara/notificaciones.txt","w")
         archivo:write("1")
	 archivo:close()
	 send_msg ('Yo', 'Notificaciones activadas', ok_cb, false)
      end
      if (msg.text=='desactnot') then
         archivo = io.open("/home/userpro/Project/Programas/Camara/notificaciones.txt","w")
         archivo:write("0")
	 archivo:close()
	 send_msg ('Yo', 'Notificaciones desactivadas', ok_cb, false)
      end
      if (msg.text=='foto') then
	 archivo = io.open("/home/userpro/Project/Programas/Camara/notificaciones.txt","r")
         linea = archivo:read()
	 if (linea == '0') then
		 os.execute('/home/userpro/Project/Programas/Camara/foto.sh')
		 send_photo ('Yo', '/home/userpro/Project/Multimedia/Fotos/last.jpg', ok_cb, false)
	 end
         archivo:close()
      end
      if (msg.text=='video') then
	 archivo = io.open("/home/userpro/Project/Programas/Camara/notificaciones.txt","r")
         linea = archivo:read()
	 if (linea == '0') then
		 os.execute('/home/userpro/Project/Programas/Camara/video.sh')
		 send_video ('Yo', '/home/userpro/Project/Multimedia/Videos/last.mp4', ok_cb, false)
	 end
         archivo:close()
      end
      if (msg.text=='temperatura') then
	 os.execute('python /home/userpro/Project/Programas/TempHum/DHT11.py 11 4 > /home/userpro/Project/Programas/TempHum/temphumact.txt')
	 archivo = io.open("/home/userpro/Project/Programas/TempHum/temphumact.txt","r")
         linea = archivo:read()
	 send_msg ('Yo', linea, ok_cb, false)
         archivo:close()
      end
      if (msg.text=='help') then
	 send_msg (msg.from.print_name, 'Comandos: - actnot - desactnot - ping - foto - video - temperatura - help -', ok_cb, false)
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

