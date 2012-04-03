# coding: utf-8
import codecs
from datetime import date
import os
import re
import datetime
from grab import Grab

__author__ = 'alexander'

def logWebPage():
    g = Grab()
    g.go('http://www.life-moon.pp.ru/', log_file = 'logs/life-moon.txt')

def writeNewMoonDay():
    f = codecs.open('Life-moon.pp.ru-' + str(datetime.date.today()) + '.txt', 'w', 'utf-8')
    return f

def openTempFile():
    logWebPage()
    f = open('logs/life-moon.txt', 'r')
    return f.read().decode('utf-8')

def getTitle():
    title = re.search(r'<title>(.+)</title>'.decode('utf-8'), openTempFile(), re.IGNORECASE)
    return title.group(1)

def getMoonDay():
    moonDay = re.search(r'<h2>(О.+)</h2>'.decode('utf-8'), openTempFile(), re.IGNORECASE)
    return moonDay.group(1)

def getMoodDayNumber():
    moonDayNumber = re.search(r'\d+', getMoonDay(), re.IGNORECASE)
    return moonDayNumber.group()

def getMoonDayDescription():
    moonDayDescription = re.findall(r'\s-\s(.+)'.decode('utf-8'), openTempFile(), re.IGNORECASE)
    return moonDayDescription

def getMoonDayBirth():
    moonDayBirth = re.search(r'<strong>(Р.+)</strong>(\s.+)'.decode('utf-8'), openTempFile(), re.IGNORECASE)
    return moonDayBirth

def getMoonDoings():
    moonDoings = re.findall(r'<tr\s*.*>\n+\t+<th>(.+)</th>\n\t+<th\s*.*>(.+)</th>\n\t+<td>(.+)</td>\n\t+</tr>'.decode('utf-8'), openTempFile(), re.IGNORECASE)
    return moonDoings

def main():
    w = writeNewMoonDay()
    w.write(getTitle() + ' на '.decode('utf-8') + str(datetime.date.today()) + '\n')
    w.write(getMoonDay() + ": \n")
    w.write('Символ: '.decode('utf-8') + getMoonDayDescription()[0] + '\n')
    w.write('Камни: '.decode('utf-8') + getMoonDayDescription()[1] + '\n')
    w.write(getMoodDayNumber() +'-й'.decode('utf-8') + ' лунный день: '.decode('utf-8') + getMoonDayDescription()[2][:-4] + '\n')
    w.write(getMoonDayBirth().group(1) + getMoonDayBirth().group(2)[:-4] + '\n')
    moon = getMoonDoings()
    for doings in moon:
        w.write('Сфера деятельности: '.decode('utf-8') + doings[0] + '\t | \t Действие луны: '.decode('utf-8') + doings[1] + '\t | \t Комментарий: '.decode('utf-8') + doings[2] + '\n')
    os.system('libreoffice Life-moon.pp.ru-' + str(datetime.date.today()) + '.txt')


if __name__ == '__main__':
    main()
