#!/usr/bin/env python
# coding=utf-8

#author:phantomer

import urllib,urllib2
import re
url="http://s.tool.chinaz.com/same"
url2=raw_input("要输入的站:")
def gethtml(url):
    data={
        "s":"glltjx.com"
    }
    f=urllib2.urlopen(url,urllib.urlencode(data))
    html=f.read()
    return html

def getpangzhan(html):
    reg=re.compile(ur'[1-9]\d*.</span>.+[0-9a-zA-Z].')
    pangzhanre=re.compile(reg)
    pangzhanlist=re.findall(pangzhanre,html)
    return pangzhanlist

html=gethtml(url)
list=getpangzhan(html)
print list

#def zhengli(list):
#    for x in list:

