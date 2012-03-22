from grab import Grab
from grab.tools.encoding import smart_str
import sys

__author__ = 'alexander'

def argv():
    if len(sys.argv) > 1:
        a = sys.argv[1] + '-' + sys.argv[2] + '-' + sys.argv[3]
    else:
        print 'Usage: python Glassdoor.py [arg1] + [arg2] + [arg3] (Example: software engineer google)'
        sys.exit()
    return a


def p(tag, pageId, extension):
    return 'http://www.glassdoor.com/Interview/' + tag + '-interview-questions-SRCH_KO0,17_KE18,24_IP' + str(pageId) + '.' + extension

def main(tag):
    employerHeaderPageId = 1
    questionTextPageId = 0
    g = Grab()
    f = open(tag + '.txt', 'w')
    g.go(p(tag, employerHeaderPageId, 'htm'))
    employerHeader = g.xpath('//h1').text_content()
    f.write(smart_str(employerHeader) + ':\n')
    while True:
        g = Grab()
        questionTextPageId += 1
        g.go(p(tag, questionTextPageId, 'htm'))
        if int(g.xpath('//li[@class="currPage"]').text) <= (questionTextPageId - 1):
            print 'Finished at page: ' + g.xpath('//li[@class="currPage"]').text + '!'
            break
        for questionText in g.xpath_list('//p[@class="questionText"]'):
            f.write(smart_str(questionText.text_content().strip()) + '\n')
        print 'Page # ' + g.xpath('//li[@class="currPage"]').text + ' parsed!'

if __name__ == '__main__':
    main(argv())





