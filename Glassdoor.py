from grab import Grab
from grab.tools.encoding import smart_str
import sys

__author__ = 'alexander'

def p(lookFor, jobTitle, company, tag, pageId):
    if len(tag) == 0:
        return 'http://www.glassdoor.com/Interview/' + jobTitle + '-' + company + '-' + lookFor + '-SRCH_KO0,' + str(len(jobTitle)) + '_KE' + str(len(jobTitle) + 1) + ',' + str(len(jobTitle) + len(company) + 1) + '_IP' + str(pageId) + '.htm'
    elif len(jobTitle) == 0 and len(company) == 0:
        return 'http://www.glassdoor.com/Interview/' + tag + '-' + lookFor + '-SRCH_KT0,' + str(len(tag)) + '_IP' + str(pageId) + '.htm'
    else:
        return 'http://www.glassdoor.com/Interview/' + jobTitle + '-' + company + '-' + tag + '-' + lookFor + '-SRCH_KO0,17_KE18,24_KT25,29' + str(pageId) + '.htm'

def main(lookFor, jobTitle, company, tag):
    employerHeaderPageId = 1
    questionTextPageId = 0
    g = Grab()
    f = open(jobTitle + '-' + company + '.txt', 'w')
    g.go(p(lookFor, jobTitle, company, tag, employerHeaderPageId))
    employerHeader = g.xpath('//h1').text_content()
    f.write(smart_str(employerHeader) + ':\n')
    while True:
        g = Grab()
        questionTextPageId += 1
        g.go(p(lookFor, jobTitle, company, tag, questionTextPageId))
        if int(g.xpath('//li[@class="currPage"]').text) <= (questionTextPageId - 1):
            print 'Finished at page: ' + g.xpath('//li[@class="currPage"]').text + '!'
            break
        for questionText in g.xpath_list('//p[@class="questionText"]'):
            f.write(smart_str(questionText.text_content().strip()) + '\n')
        print 'Page # ' + g.xpath('//li[@class="currPage"]').text + ' parsed!'

if __name__ == '__main__':
    lookFor = raw_input('Look For: ')
    jobTitle = raw_input('Job Title: ')
    company = raw_input('Company: ')
    tag = raw_input('Tag (Optional): ')
    if len(tag) == 0:
        main(lookFor,jobTitle,company,'')
    elif len(jobTitle) == 0 and len(company) == 0:
        main(lookFor,'','',tag)
    else:
        print p(lookFor,jobTitle,company,tag,1)









