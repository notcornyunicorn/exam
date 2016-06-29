import re
import os

def readfile(filename):
    f = open(filename, 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    return text

def firsttask(text):
    regex = '[А-Я]\. [А-Я][а-я]+'
    result = re.findall(regex, text)
    if result:
        for name in result:
            print(name)

def secondtask(text):
    regex1 = '[А-Я]\. [А-Я]\. [А-Я][а-я]+'
    regex2 = '[А-Я][а-я]+ [А-Я][а-я]+'
    result1 = re.findall(regex1, text)
    f = open('имена.txt', 'a', encoding = 'utf-8')
    if result1:
        for name in result1:
            print(name)
            f.write(name + '\n')
    result2 = re.findall(regex2, text)
    if result2:
        for name in result2:
            print(name)
            f.write(name + '\n')
    f.close()
    #в файл я записываю для следующего задания

def thirdtask(text):
    f = open('имена.txt', 'r', encoding = 'utf-8')
    names = f.readlines()
    f.close()
    surnames = []
    regex = ' [А-Я][а-я]+'
    for name in names:
        result = re.findall(regex, name)
        if result:
            surname = ' '.join(result)
            surname = surname.strip()
            surnames.append(surname)
    for surname in surnames:
        if not os.path.exists(surname):
            os.makedirs(surname)
    #дальше не успела

def main():
    reading = readfile(r'C:\Users\student\Desktop\михайловский дворец.txt')
    first = firsttask(reading)
    second = secondtask(reading)
    third = thirdtask(reading)

if __name__=='__main__':
    main()
