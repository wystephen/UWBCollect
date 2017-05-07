# -*- coding:utf-8 -*-
# carete by steve at  2017 / 05 / 07　14:35

import serial
import time

if __name__ == '__main__':
   start_time = time.time()
   print(start_time)
   save_source_file = open("./"+str(start_time)+"_uwbdata.txt",'wb')

   # print(time.strftime("%Y-%m-%d", start_time))
   t=serial.Serial('com3',115200)
   while( t.isOpen()):

      data = t.readline()
      print(data)
      save_source_file.write((data))


   t.close()
   save_source_file.close()





