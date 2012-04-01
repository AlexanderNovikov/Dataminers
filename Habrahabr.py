# coding: utf-8
from grab import Grab
from grab.tools.encoding import smart_str
import sys
import logging


__author__ = 'alexander'

def argv():
    if len(sys.argv) > 1:
        a = sys.argv[1]
    else:
        print 'Usage: python Habrahabr.py [arg1] (Example: software)'
        sys.exit()
    return a

def p(tag, pageId):
    return 'http://habrahabr.ru/search/page' + str(pageId) + '/?target_type=posts&order_by=relevance&q=' + tag

def main(tag):
    pageId = 0
    f = open(tag + '.txt', 'w')
    f.write(tag + ':\n' )
    while True:
        g = Grab()
        g.setup(timeout=60, connect_timeout=60)
        pageId += 1
        g.go(p(tag, pageId))
        v1 = g.xpath_text('//title')
        v2 = unicode("Хабрахабр — страница не найдена (404)", 'utf-8')
        if  v1 == v2:
            print 'Finished at page: ' + str(pageId) + '!'
            break
        for questionText in g.xpath_list('//a[@class="post_title"]'):
            f.write(smart_str(questionText.text_content().strip()) + '\n')
        print 'Page # ' + str(pageId) + ' parsed!'

if __name__ == '__main__':
    main(argv())

