#!/bin/bash

  raspistill -w 1920 -h 1080 -o /home/userpro/Project/Multimedia/Fotos/last.jpg
  _date=`date +%Y-%m-%d`
  _time=`date +%H:%M:%S`
  _imgfile="/home/userpro/Project/Multimedia/Fotos/$_date/$_time.jpg"
  mkdir -p /home/userpro/Project/Multimedia/Fotos/$_date
  cp /home/userpro/Project/Multimedia/Fotos/last.jpg $_imgfile
