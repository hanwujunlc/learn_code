#!/usr/bin/python
# coding=UTF-8

import urllib
import urllib2
import sys
import getopt 

sys.path.append('douban')
from html import Parse

reload(sys)
sys.setdefaultencoding('utf8')

book_tag = '�����'
page_num = 0

#url='http://www.douban.com/tag/'+urllib.quote(book_tag)+'/book?start='+str(page_num*15)
url = 'https://book.douban.com/tag/' + urllib.quote(book_tag)
#print(url)
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
#p = Parse(result)

#p.getContent()
#p.getTitle()

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

def do_spider(tag_list):
    print tag_list[0]    

class Usage(Exception) :
    def __init__(self, msg):
        self.msg = msg



def main(argv=None):
    print 'call the main function'
    
    print argv 
    if argv is None:
        argv = sys.argv
#        print argv 

    try :
        try :
            opts,args = getopt.getopt(argv[1:], 'h:', ['help'])
            #opts,args = getopt.getopt(argv[1:], 'ho:v', ['help', 'output='])

        except getopt.error, msg:
            raise Usage(msg)
        #more code, unchanged 
        for o, a in opts :
            print o
            print a

        print '------'

        for i in args :
            print i

    except Usage, err:
#        print >> sys.stderr, err.msg
        print err.msg
        print >> sys.stderr, 'for help us --help'

    #book_tag_lists = ['����','�ж������','�㷨','���ݽṹ','����','��ʷ']
    #book_tag_lists = ['����','��ѧ','���','��ҵ','���','���ѧ','���']
    #book_tag_lists = ['˼��','�Ƽ�','��ѧ','web','��Ʊ','����','����']
    #book_tag_lists = ['�����','����ѧϰ','linux','android','���ݿ�','������']
    #book_tag_lists = ['��ѧ']
    #book_tag_lists = ['��Ӱ','���','����','����','����','�ɳ�','���','����','����','����']
    #book_tag_lists = ['��ҵ','���','����']  
    #book_tag_lists = ['����']
    #book_tag_lists = ['����','����','����','����','��ѧ']
    #book_tag_lists = ['�ƻ�','˼ά','����']
    book_tag_lists = ['���˹���','ʱ�����','Ͷ��','�Ļ�','�ڽ�']
    #book_list = do_spider(book_tag_list)

    #print_book_list_execl(book_list)

    return 2

if __name__ == '__main__' :
    sys.exit(main())
