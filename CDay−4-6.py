# -*- coding:utf -8 -*-
import os
#export = ""
#for root, dirs, files in os.walk('/media/cdrom0'):
#export+="\n %s;%s;%s" % (root,dirs,files)
#open('mycd2.cdc', 'w').write(export)

export=[]
#for root,dirs,files in os.walk('/home/jhjguxin/Desktop/'):
for root,dirs,files in os.walk(os.getcwd()):
  export.append('\n %s;%s;%s'%(root,dirs,files))
open('mycd2.cdc','w').write(''.join(export))
