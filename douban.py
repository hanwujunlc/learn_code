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

book_tag = '计算机'
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

    #book_tag_lists = ['心理','判断与决策','算法','数据结构','经济','历史']
    #book_tag_lists = ['传记','哲学','编程','创业','理财','社会学','佛教']
    #book_tag_lists = ['思想','科技','科学','web','股票','爱情','两性']
    #book_tag_lists = ['计算机','机器学习','linux','android','数据库','互联网']
    #book_tag_lists = ['数学']
    #book_tag_lists = ['摄影','设计','音乐','旅行','教育','成长','情感','育儿','健康','养生']
    #book_tag_lists = ['商业','理财','管理']  
    #book_tag_lists = ['名著']
    #book_tag_lists = ['科普','经典','生活','心灵','文学']
    #book_tag_lists = ['科幻','思维','金融']
    book_tag_lists = ['个人管理','时间管理','投资','文化','宗教']
    #book_list = do_spider(book_tag_list)

    #print_book_list_execl(book_list)

    return 2

if __name__ == '__main__' :
    sys.exit(main())
