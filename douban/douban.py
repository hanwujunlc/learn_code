#!/usr/bin/python
# coding=UTF-8

import urllib
import urllib2
import sys

from html import Parse

reload(sys)
sys.setdefaultencoding('utf8')

book_tag = '�����'
page_num = 0

#url='http://www.douban.com/tag/'+urllib.quote(book_tag)+'/book?start='+str(page_num*15)
url = 'https://book.douban.com/tag/' + urllib.quote(book_tag)
print(url)
result= ''

try:
    request = urllib2.Request(url)
    #request = urllib2.Request("http://www.baidu.com/")

    #response = urllib2.urlopen("http://www.baidu.com/")
    response = urllib2.urlopen(request)

    result = response.read()

#    print(result)
except (urllib2.HTTPError, urllib2.URLError), e:
    print e
    

#p = html.Parse(result)
p = Parse(result)

p.getContent()
p.getTitle()

#s = result
#values = []
#s = s.strip().replace('\n', '').replace('\r', '')
#while s != '':
#        str = s[s.find('<') + 1: s.find('>')]
#        #print(str)
#        values.append(str)
#        s = s[s.find('>') + 1: ]
#
##print (values)


