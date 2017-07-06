#!/usr/bin/env python
# coding:utf-8

a=u'中文'
print a
print '中文 unicode =', len(a)
print '中文 utf-8 = ', len(a.encode('utf-8'))

b='中文'
print b
print '中文 = ', len('中文')

print 'ABC unicode = ', len(u'ABC')
print 'ABC = ', len('ABC')
print 'ABC utf-8 = ', len('ABC'.encode('utf-8'))

