# coding=UTF-8
#!/usr/bin/python

import re

class Parse:
    def __init__(self, content):
        '''Initializes func'''
        content = content.strip().replace('\n', '').replace('\r', '')
        self.content = content
    
    def __del__(self):
        '''Deinit func'''
        self.content = ''
    
    def getContent(self):
        '''Parse the html get the content'''
        s = self.content
        while s != '':
            str = s[s.find('<') + 1: s.find('>')]
#            print(str)
            s = s[s.find('>') + 1: ]

    def getHead(self):
        s = self.content
        

    def getTitle(self):
        s = self.content
        #s = s[s.find('<title>') + len('<title>'): s.find('</title>')]
        #s = s.strip()

        p = '(?<=<title>).+?(?=</title>)'
        pattern = re.compile(p)
        s = pattern.findall(s)
        
        print s[0].strip()
#        print s
        self.title = s
        self.getList()

    def getList(self):
        s = self.content
        listlen = s.count('subject-item')
        #print s.count('class="subject-item"')
        #print s.count('</li>')
        p = '(?<=<li class="subject-item">).+?(?=</li>)'
        pattern = re.compile(p)
        list_content = pattern.findall(s)
        
        print len(list_content)
        for i in list_content :
            print(i)
            break

#        #debug 
#        listlen = 1
#        for i in range(listlen) :
#            s_begin = '<li class="subject-item">'
#            s_end = '</li>'
#            #s = s[s.find(s_begin): ]
#            #list_content = s[s.find(s_begin) + len(s_begin): s.find(s_end)]
#            p = '(?<=<li class="subject-item">).+?(?=</li>)'
#            pattern = re.compile(p)
#            list_content = pattern.findall(s)
#
#            print len(list_content)
#            #print list_content[0].strip()
#            #s = s[s.find(s_end) + len(s_end): ]
#
#            #print list_content.count('<div')
#            #print list_content.count('</div>')
#            div_len = list_content.count('<div')
#
#            div_list = {}
#
#            #debug
#            div_len = 1 
#
#            for j in range(div_len) :
#                div_content = list_content
#                j_begin = '<div'
#                j_end = '</div>'
#                div_content = s[s.find(j_begin) + len(j_begin): s.find(j_end)]
#                #print(div_content)
#                p1 = '<div.+</div>'
#                pattern = re.compile(p1)
#                #print pattern.findall(div_content)
#
#                #print div_content.find(r'<div(\w+)>')
#                #if ('' == div_content[]
#                    

