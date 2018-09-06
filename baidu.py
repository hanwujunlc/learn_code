#!/usr/bin/python

import urllib2

request = urllib2.Request("http://www.baidu.com/")
#response = urllib2.urlopen("http://www.baidu.com/")
response = urllib2.urlopen(request)

result = response.read()

#print(result)
s = result
values = []
s = s.strip().replace('\n', '').replace('\r', '')
while s != '':
        str = s[s.find('<') + 1: s.find('>')]
        print(str)
        values.append(str)
        s = s[s.find('>') + 1: ]
        break

#print (values)


if __name__ == "__main__" :
    print 'test main function'
