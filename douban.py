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

def do_spider(lists):
    print 'call the do spider function'
    print len(lists)
    for tag in lists:
        #print urllib.quote(tag), tag
    
        url = 'https://book.douban.com/tag/' + urllib.quote(tag)
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            result = response.read()
            
        except (urllib2.HTTPError, urllib2.URLError), e:
            print e
        
        p = Parse(result)
            
        title = p.getTitle()
        print title
        
        data = p.getList()
        for d in data:
            print d['img']

    
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
 #       for o, a in opts :
 #           print o
 #           print a

        print '------'

#        for i in args :
#            print i

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
    book_list = do_spider(book_tag_lists)

    #print_book_list_execl(book_list)

    return 2

if __name__ == '__main__' :
    sys.exit(main())


