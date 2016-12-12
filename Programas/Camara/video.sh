#!/bin/bash

  rm /home/userpro/Project/Multimedia/Videos/last.mp4
  raspivid -o /home/userpro/Project/Multimedia/Videos/last.h264 -t 10000 -fps 5
  MP4Box -fps 5 -add /home/userpro/Project/Multimedia/Videos/last.h264 /home/userpro/Project/Multimedia/Videos/last.mp4
  rm /home/userpro/Project/Multimedia/Videos/last.h264
  _date=`date +%Y-%m-%d`
  _time=`date +%H:%M:%S`
  _vidfile="/home/userpro/Project/Multimedia/Videos/$_date/$_time.mp4"
  mkdir -p /home/userpro/Project/Multimedia/Videos/$_date
  cp /home/userpro/Project/Multimedia/Videos/last.mp4 $_vidfile
