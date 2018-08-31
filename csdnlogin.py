#!/usr/bin/python

import urllib
import urllib2
import string 

#values = {"username":"hanwujunlc", "passwd":"hwj19890929"}
values = {}
values['usename'] = 'hanwujunlc'
values['password'] = 'hwj19890929'
data = urllib.urlencode(values)
#url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
#request = urllib2.Request(url, data)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
print(geturl)
request = urllib2.Request(geturl)


response = urllib2.urlopen(request)
#print response.read()
#result = response.read()
result = response.readlines()

#for line in result:
#        print(line)

string.find(result, "body")


