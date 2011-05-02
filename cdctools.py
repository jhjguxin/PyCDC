# -*- coding:utf-8 -*-
# cdctools.py
import os
import chardet
import pdb
from ConfigParser import RawConfigParser as rcp
#from smartcode import * 记住是导入到 当前目录不是cdctools

#扫描光盘信息记录为文件
def cdWalker(cdrom,cdcfile):
  '''光盘扫描主函式
  @param cdrom: 光盘访问路径
  @param cdcfile: 输出的光盘信息记录文件(包含路径,绝对、相对都可以)
  @return: 无,直接输出成*.cdc 文件
  @attention: 从 v0.7 开始不使用此扫描函式,使用 iniCDinfo()
  '''

  export=''
  for root,dirs,files in os.walk(cdrom):
#    export+='\n %s;%s;%s'%(root,dirs,files)
    print formatCDinfo(root,dirs,files)
    export+=formatCDinfo(root,dirs,files)   #将光盘文件编码读出并转化为utf-8编码保存

  open(cdcfile,'w').write(export)

#搜索打开所有符合要求的文件,读取每一行,如果有指定关键词在行内就打印输出到屏幕......
def cdcGrep(cdcpath,keyword):
  "#搜索打开所有符合要求的文件,读取每一行,如果有指定关键词在行内就打印输出到屏幕......"
  for root,dirs,files in os.walk(cdcpath):  #找出根目录下的所有目录需要三个参数才行哦
    filelist = os.listdir('%s'%(root,)) # 搜索目录中的文件
    for cdc in filelist:        # 循环文件列表
      if ".cdc" in cdc:         # 过滤可能的其它文件,只关注.cdc
        cdcfile = open(cdcpath+cdc)         # 拼合文件路径,并打开文件
        for line in cdcfile.readlines():    # 读取文件每一行,并循环
          if keyword in line:      # 判定是否有关键词在行中
            print line               # 打印输出

def formatCDinfo(root,dirs,files):
  '''光盘信息记录格式化函式
  @note: 直接利用 os.walk() 函式的输出信息进行重组
  @param root: 当前根
  @param dirs: 当前根中的所有目录
  @param files: 当前根中的所有文件
  @return: 字串,组织好的当前目录信息
  '''

  export = "\n"+root+"\n"
  for d in dirs:
    export+= "-d "+root+_smartcode(d)+"\n"
  for f in files:
    export+= "-f %s %s \n" % (root,_smartcode(f))
  export+= "="*70
  return export

def _smartcode(ustring):
  """smart recove stream into UTF-8
  """
  codename = chardet.detect(ustring)["encoding"]
  print codename

  try:
    print ustring
    ustring = unicode(ustring, codename)
    print ustring
    return "%s %s"%("",ustring.encode('utf8'))#返回utf8编码
  except:
    return u"bad unicode encode try!"

def iniCDinfo(cdrom,cdcfile):
  '''光盘信息.ini 格式化函式
  @note: 直接利用 os.walk() 函式的输出信息由 ConfigParser.RawConfigParser
  @param cdrom: 光盘访问路径
  @param cdcfile: 输出的光盘信息记录文件(包含路径,绝对、相对都可以)
  @return: 无,直接输出成组织好的类.ini 的*.cdc 文件
  '''
  walker={}
  for root,dirs,files in os.walk(cdrom):
    walker[root]=(dirs,files)  # 这里是个需要理解的地方
  cfg = rcp()
  cfg.add_section("Info")
  cfg.add_section("Comment")
  cfg.set("Info", 'ImagePath', cdrom)
  cfg.set("Info", 'Volume', cdcfile)
  dirs = walker.keys()
  i = 0
  for d in dirs:
    i+=1
    cfg.set("Comment",str(i),d)
  for p in walker:
    cfg.add_section(p)
    for f in walker[p][1]:
      cfg.set(p,f,os.stat("%s/%s"%(p,f)).st_size)
  cfg.write(open(cdcfile,'w'))





if __name__=="__main__":    #this way the module can be
  CDROM=os.getcwd()
  cdWalker(CDROM,'cdctools.cdc')#只有单文件执行才执行这部分
  iniCDinfo(CDROM,'try.ini')
