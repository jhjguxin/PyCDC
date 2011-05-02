# -*-coding: utf-8 -*-
import os
#print os.listdir('/home/jhjguxin/Desktop/')
for root,dirs,files in os.walk(os.getcwd()):
  print root,dirs,files
