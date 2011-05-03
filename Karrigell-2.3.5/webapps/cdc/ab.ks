# -*- coding: utf-8 -*-
from HTMLTags import *
def index(**args):
  print HTML( HEAD(TITLE('Test document')) +
  BODY(H1('This is a test document')+
  TEXT('First line')+BR()+
  TEXT('Second line')))

