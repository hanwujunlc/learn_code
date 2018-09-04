# coding=UTF-8
#!/usr/bin/python

import urllib
import urllib2
from html import Parse


book_tag = '¼ÆËã»ú'
page_num = 0

#url='http://www.douban.com/tag/'+urllib.quote(book_tag)+'/book?start='+str(page_num*15)
url = 'https://book.douban.com/tag/%E7%AE%97%E6%B3%95'
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

