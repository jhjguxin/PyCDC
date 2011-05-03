# -*- coding: utf-8 -*-
from cdctools import *
from HTMLTags import *
from Karrigell_QuickForm import Karrigell_QuickForm as KQF
#print dir()  #通过检查名称空间进行测试,结果如图 CDay2-4 所示。


def _htmhead(title):
  '''默认页面头声明
  @note: 为了复用,特别的组织成独立函式,根据 Karrigell 非页面访问约定,函式名称前加"_"
  @param title: 页面标题信息
  @return: 标准的 HTML 代码
  '''
  htm = """<html><HEAD>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<title>%s</title></HEAD>
<body>"""%title
  return htm
## 默认页面尾声明
htmfoot="""
<h5>design by:<a href="mailto:864248765@qq.com">Email to JHJguxin</a>
    powered by : <a href="http://python.org">Python</a> +
<a href="http://karrigell.sourceforge.net"> KARRIGELL 2.3.5</a>
</h5>
</body></html>"""

## 全局变量
CDCPATH = "/home/jhjguxin/Desktop/code/PyCDC/cdc"
#CDROM = '/media/cdrom0'
CDROM = '/home/jhjguxin/Desktop/code/PyCDC'

def index(**args):
  '''默认主页
  @note: 使用简单的表单/链接操作来完成原有功能的界面化
  @param args: 数组化的不定参数
  @return: 标准的 HTML 页面
  '''
  print _htmhead("PyCDC WEB")
  p = KQF('fm_cdwalk','POST',"index","CD Walk")
  p.addHtmNode('text',"keywd",u"文件名",{'size':20,'maxlength':50})
  p.addGroup(["submit","btn_submit","Walk it!","btn"])
  p.display()
  p = KQF('fm_cdwalk','POST',"index","CD Walk")
  p.addHtmNode('text',"keywd",u"关键字",{'size':20,'maxlength':50})
  p.addGroup(["submit","btn_submit","Search it!","btn"])
  p.display()

  if 0 == len(QUERY):
    pass
  else:
    if "Search" in QUERY['btn_submit']:
      if "" == QUERY['keywd']:
        print H3("pls import SearchKey!")
      else:
        print I("try search *.cdc for KEY:%s"%QUERY['keywd'])
        print BR()#,cdcGrep("%s/"%CDCPATH,QUERY['keywd'])
        cdcGrep("%s/"%CDCPATH,QUERY['keywd'])
        searcheDict = pickle.load(open("searched.dump"))
        for cdc in searcheDict.keys():
          print H5(cdc)
          for line in searcheDict[cdc]:
            print BR(line)
    elif "Walk" in QUERY['btn_submit']:
      print I("try walk CD for:%s ..."%QUERY['keywd'])
      iniCDinfo(CDROM,"%s/%s"%(CDCPATH,QUERY['keywd']))
      print BR(),B("had export info. file as::%s/%s"%(CDCPATH,QUERY['keywd']))
    else:
      pass
  print htmfoot

