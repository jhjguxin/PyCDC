# -*- coding: utf-8 -*-
import chardet
def _smartcode(stream):
  """smart recove stream into UTF-8
  """

  ustring = stream
  codedetect = chardet.detect(ustring)["encoding"]
  print codedetect

  try:
    print ustring
    ustring = unicode(ustring, codedetect)
    print ustring
    return "%s %s"%("",ustring.encode('utf8'))#返回utf8编码
  except:
    return u"bad unicode encode try!"
if __name__=='__main__':   #this way the module can be

  #imported by other programs as well
  stream='经过测试,已确信它在各种情况下都可以正确识别!但是不论怎么尝试,已经保存下来的.cdc 文本依然是 ASCII 码!'

  _smartcode(stream)
