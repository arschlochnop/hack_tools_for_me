#!/usr/bin/env python
# coding=utf-8

#author:phantomer

import urllib,urllib2
import re
url="http://s.tool.chinaz.com/same"
url2=raw_input("要输入的站:")
def gethtml(url):
    data={
        "s":url2
    }
    f=urllib2.urlopen(url,urllib.urlencode(data))
    html=f.read()
    return html

def getpangzhan(html):
    reg=re.compile(ur'[1-9]\d*.</span>.+[0-9a-zA-Z].')
    #reg2=re.compile
    pangzhanre=re.compile(reg)
    pangzhanlist=re.findall(pangzhanre,html)
    return pangzhanlist

html=gethtml(url)
list=getpangzhan(html)
print list

fo=open("output.txt","wb")

fo.writelines(list)

fo.close()
