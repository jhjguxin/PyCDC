# -*- coding:utf-8 -*-
# cdctools.py
import os
import chardet
import time
import pdb
from ConfigParser import RawConfigParser as rcp
import pickle
#from smartcode import * 记住是导入到 当前目录不是cdctools
from threading import Thread  # 导入线程支持模块

#扫描光盘信息记录为文件
def cdWalker(cdrom,cdcfile):
  u'''光盘扫描主函式
  @param cdrom: 光盘访问路径
  @param cdcfile: 输出的光盘信息记录文件(包含路径,绝对、相对都可以)
  @return: 无,直接输出成*.cdc 文件
  @attention: 从 v0.7 开始不使用此扫描函式,使用 iniCDinfo()
  '''
  print "*"*70
  print cdWalker.__name__
  print cdWalker.__doc__

  export=''
  for root,dirs,files in os.walk(cdrom):
#    export+='\n %s;%s;%s'%(root,dirs,files)
    print formatCDinfo(root,dirs,files)
    export+=formatCDinfo(root,dirs,files)   #将光盘文件编码读出并转化为utf-8编码保存

  open(cdcfile,'w').write(export)


def formatCDinfo(root,dirs,files):
  u'''光盘信息记录格式化函式
  @note: 直接利用 os.walk() 函式的输出信息进行重组
  @param root: 当前根
  @param dirs: 当前根中的所有目录
  @param files: 当前根中的所有文件
  @return: 字串,组织好的当前目录信息
  '''
  print "*"*70
  print formatCDinfo.__name__
  print formatCDinfo.__doc__

  export = "\n"+root+"\n"
  for d in dirs:
    export+= "-d "+root+_smartcode(d)+"\n"
  for f in files:
    export+= "-f %s %s \n" % (root,_smartcode(f))
  export+= "="*70
  return export

def _smartcode(ustring):
  u"""smart recove stream into UTF-8
  """
  print "*"*50
  print _smartcode.__name__
  print _smartcode.__doc__

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
  u'''光盘信息.ini 格式化函式
  @note: 直接利用 os.walk() 函式的输出信息由 ConfigParser.RawConfigParser
  @param cdrom: 光盘访问路径
  @param cdcfile: 输出的光盘信息记录文件(包含路径,绝对、相对都可以)
  @return: 无,直接输出成组织好的.ini文件
  '''

  print "*"*70
  print iniCDinfo.__name__
  print iniCDinfo.__doc__

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

#搜索打开所有符合要求的文件,读取每一行,如果有指定关键词在行内就打印输出到屏幕......
def cdcGrep(cdcpath,keyword):
  u''''\n'光盘信息搜索主函式
  @note: 直接利用 pickle 函式搜索打开所有符合要求的文件,读取每一行,如果有指定关键词在行内就打印输出到屏幕......
  @param cdcpath: 搜索路径(包含路径,绝对、相对都可以)
  @return: searched.dump
  '''
  print "*"*70
  print cdcGrep.__name__
  print cdcGrep.__doc__

  expDict = {}
  filelist = os.listdir(cdcpath) # 搜索目录中的文件
  for cdc in filelist: # 循环文件列表
    if ".ini" in cdc:
      cdcfile = open(cdcpath+cdc)# 拼合文件路径,并打开文件
      expDict[cdc] = []
      for line in cdcfile.readlines():# 读取文件每一行,并循环
        if keyword in line:# 判定是否有关键词在行中
          #print line
          expDict[cdc].append(line) # 打印输出
  pickle.dump(expDict,open("searched.dump","w"))


#多线程初始化
class grepIt(Thread):
  "多线程初始化"
  def __init__ (self,cdcfile,keyword):
    Thread.__init__(self)
    self.cdcf = cdcfile
    self.keyw = keyword
    self.report = ""
  def run(self):
    if ".ini" in self.cdcf:
      self.report = markIni(self.cdcf,self.keyw)

def markIni(cdcfile,keyword):
  '''配置文件模式匹配函式:
  '''
  report = ""
  keyw = keyword
  cfg = rcp()
  cfg.read(cdcfile)
  nodelist = cfg.sections()
  nodelist.remove("Comment")
  nodelist.remove("Info")
  for node in nodelist:
    if keyw in node:
      print node
      report += "\n %s"%node # error as "\n",node|str(node)...
      continue
    else:
      for item in cfg.items(node):
        if keyw in item[0]:
          report += "\n %s/%s "%(node,item)
  return report

def grpSearch(cdcpath,keyword):
  u'''光盘信息多线程群体搜索主函式
  @note: 直接利用 pickle 函式搜索打开所有符合要求的文件,读取每一行,如果有指定关键词在行内就打印输出到屏幕......
  @param cdcpath: 搜索路径(包含路径,绝对、相对都可以)
  '''
  print "*"*70
  print grpSearch.__name__
  print grpSearch.__doc__

  begin = time.time()
  filelist = os.listdir(cdcpath) # 搜索目录中的文件
  searchlist = [] # 记录发起的搜索编程

  for cdcf in filelist:
    pathcdcf = "%s/%s"%(cdcpath,cdcf)
    current = grepIt(pathcdcf,keyword) # 初始化线程对象
    searchlist.append(current) # 追加记录线程队列
    current.start()  # 发动线程处理

  for searcher in searchlist:
    searcher.join()
    print "Search from ",searcher.cdcf," out ",searcher.report
  print "usage %s s"%(time.time()-begin)


if __name__=="__main__":    #this way the module can be
  '''cdctools 自测响应处理
  '''
  print '''cdctools 自测响应处理
  '''
  CDCPATH = "/home/jhjguxin/Desktop/code/PyCDC/cdc/"

  CDROM=os.getcwd()

  cdWalker(CDROM,CDCPATH+'cdctools.cdc')#只有单文件执行才执行这部分
  iniCDinfo(CDROM,CDCPATH+'try.ini')

  ## 需要根据实际情况指向真实的目录

  cdcGrep(CDCPATH,"cdc")
  print pickle.load(open("searched.dump"))

