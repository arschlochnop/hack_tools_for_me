#!/usr/bin/env python
# coding=utf-8

#author : phantomer

import string

print "本程序用来简易的转换22位MD5到规范的MD5\n"


name=raw_input("请输入22位MD5：")

table1={
    'A':'0','B':'1','C':'2','D':'3','E':'4','F':'5','G':'6','H':'7','I':'8','J':'9','K':'10','L':'11','M':'12','N':'13','O':'14','P':'15','Q':'16','R':'17','S':'18','T':'19','U':'20','V':'21','W':'22','X':'23','Y':'24','Z':'25'
}
table2={
    'a':'26','b':'27','c':'28','d':'29','e':'30','f':'31','g':'32','h':'33','i':'34','j':'35','k':'36','l':'37','m':'38','n':'39','o':'40','p':'41','q':'42','r':'43','s':'44','t':'45','u':'46','v':'47','w':'48','x':'49','y':'50','z':'51'
}
table3={
    '0':'52','1':'53','2':'54','3':'55','4':'56','5':'57','6':'58','7':'59','8':'60','9':'61','+':'62','/':'63'
}
global strings
strings=""
for i in name:
    if i in table1:
        a=bin(int(table1[i])).zfill(8)
        a=a[2:]
    elif i in table2:
        a=bin(int(table2[i])).zfill(8)
        a=a[2:]
    elif i in table3:
        a=bin(int(table3[i])).zfill(8)
        a=a[2:]
    if i==name[-1]:
        a=a[0:2]
    if 'b' in a:
        a=string.replace(a,"b","0")
    strings+=a

liststring = [strings[x:x+8] for x in range(0,len(strings),8)]

global strings2
strings2=""
for i in range(16):
    liststring[i]=hex(int(liststring[i],2))
    a=liststring[i]
    a=a[2:].upper()
    strings2+=a

print "生成的32位md5：",strings2
