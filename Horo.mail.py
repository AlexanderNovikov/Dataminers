# coding: utf-8
import codecs
import os
import re
import datetime
from grab import Grab

__author__ = 'alexander'

def attributes():
    attribute = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
    return attribute

def logWebPages(attribute):
    g = Grab()
    g.go('http://horo.mail.ru/prediction/' + attribute + '/today/', log_file = 'logs/' + attribute + '.txt')

def writeNewHoro():
    f = codecs.open('Horo.mail.ru-' + str(datetime.date.today()) + '.txt', 'w', 'utf-8')
    return f

def openTempFile(attribute):
    logWebPages(attribute)
    f = open('logs/' + attribute + '.txt', 'r')
    return f.read().decode('windows-1251')

def getTitle(attribute):
    title = re.search(r'<h1\sclass=mb15>(.+)</h1>', openTempFile(attribute), re.IGNORECASE)
    return title.group(1)

def getPrediction(attribute):
    prediction = re.findall(r'<p>\r*\n(.+)\n</p>', openTempFile(attribute), re.IGNORECASE)
    return prediction

def main():
    w = writeNewHoro()
    for attribute in attributes():
        w.write(getTitle(attribute) + '\n')
        w.write('\t' + getPrediction(attribute)[0] + '\n' + getPrediction(attribute)[1] + '\n\n')
    os.system('libreoffice Horo.mail.ru-' + str(datetime.date.today()) + '.txt')

if __name__ == '__main__':
    main()
