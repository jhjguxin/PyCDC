# -*- coding:utf-8 -*-
import os,sys
print sys.argv
def cdWalker(cdrom,cdcfile):
  export=''
  for root,dirs,files in os.walk(cdrom):
    export+='\n %s;%s;%s'%(root,dirs,files)
  open(cdcfile,'w').write(export)
#cdWalker(os.getcwd(),'cd1.cdc')

