#!/bin/bash
to=$1
msg=$2
tgpath=/home/userpro/Project/tg
${tgpath}/bin/telegram-cli -k ${tgpath}/tg-server.pub -W -e "msg $to $msg" -d
