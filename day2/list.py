#!/usr/bin/env python
# -*- coding: utf-8 -*-

classmates = ['zhangsan', 'lisi', 'wangwu']
print classmates

print classmates[0]
print classmates[-1]
print classmates[len(classmates)-1]

print classmates[1]
print classmates[-2]

#初始化
p = []
print len(p);

#增
classmates.append('songliu')
classmates.insert(-1,'qi')
print classmates

#删
classmates.pop()
classmates.pop(-1)
print classmates

#改
classmates[1] = 'lishi'
print classmates

#遍历
for name in classmates:
   print name 
n = len(classmates)
while n > 0:
    print classmates[n-1]
    n = n - 1
a = ''
for name in raw_input():
    if name != ' ':
        a = '%s%s'%(a,name)
    else:
        print a
        a = ''
print a

mates = ('aaa','bbb', 'ccc')
print len(mates)
