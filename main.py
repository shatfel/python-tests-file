#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import datetime
import time
import re

##
_C = {
  'DEBUG': False,

  'format': {
    'date': "%Y%m%d",
    'time':"%H%M%S"
    },

  'date': datetime.date.today().strftime('%Y-%m-%d %H:%M:%S'), 

  'fPath': './test',
  'fName': 'test00.txt',
  'fNameRe': '%s*.log' % datetime.date.today().strftime('%Y%m%d-%H%M%S'),
  'search': {
    'line': '<result "yes">',
    'lineCount': 4,
    }
}


## checn debug env
_envDebug = None
if 'DEBUG' in os.environ:
  _envDebug = os.environ['DEBUG']
  if _envDebug != None and _envDebug != '' and _envDebug != 0:
    if _envDebug == '1' or _envDebug == 't' or _envDebug == "true":
      _C['DEBUG'] = True


###
##
###
def prDebug(msg):
   if _C['DEBUG']:
     print ("/d/ %s" % msg)

###
##
###
def getDateTime(fmt=None):
  _fmt = "%s-%s" % (_C['format']['date'], _C['format']['time'])
  
  if fmt != None:
    _fmtDate, _fmtTime = fmt.split(' ')
    _fmt = "%s-%s" % (getDate(_fmtDate), getTime(_fmtTime))

  _date = _fmt % (getDate(_C), getTime())
  return _date


###
##
###
def getDate(fmt=None):
  _fmt = _C['format']['date']

  if fmt != None:
    _fmt = fmt

  _date = datetime.datetime.today().strftime(_fmt)
  return _date


###
##
###
def getTime(fmt=None):
  _fmt = _C['format']['time']
  
  if fmt != None:
    _fmt = fmt

  _time = datetime.datetime.today().strftime(_fmt)
  return _time


###
##
###
def getFileAttrs(fName=None):
  _fName = "%s/%s" % (_C['fPath'], _C['fName'])
  
  if fName != None:
    _fName = fName

  ## return create time, modify time, access time
  _r = [ time.ctime(os.path.getctime(_fName)), time.ctime(os.path.getmtime(_fName)), time.ctime(os.path.getatime(_fName)) ]
  return  _r


###
##
###
def checkFileExistsRe(fName=None, fPath=None):
  _fName = _C['fName']
  _fPath = _C['fPath']
  
  if fName != None:
    _fName = fName

  if fPath != None:
    _fPath = fPath

  ## prepare regexp
  _re = re.compile(_fName)

  prDebug(' fName => %s' % _fName)

  for _f in os.scandir(_C['fPath']):
    if _f.is_file:
      prDebug(_f.name)
      if _re.match(_f.name):
        return 1

  return 0
  

###
## main
###
if __name__ == "__main__":
  if _C['DEBUG']:
    prDebug('date => %s' % getDate('%Y-%m-%d'))
    prDebug('time => %s' % getTime('%H:%M:%S'))

    _attrs = getFileAttrs('./test/test00.txt')
    _fName = "%s/%s" % (_C['fPath'], _C['fName'])
    prDebug('times of %s:\ncreate => %s\nmodify => %s\naccess => %s' % (_fName, _attrs[0], _attrs[1], _attrs[2]))
    for _fName in None, '202106', 'test':
      prDebug('file regexp check for %s: %d' % (_fName, checkFileExistsRe(_fName)))