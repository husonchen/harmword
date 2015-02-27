#encoding:utf-8
'''
Created on Feb 26, 2015

@author: root
'''
import Test
import sys

wordsweight = {}
if __name__ == '__main__':
    #读取权重文件
    resultfile = open("result.txt")
    for line in resultfile.readlines():
        temp = line.split(' ')
        wordsweight[temp[0]] = float(temp[1])
    
    testfile = open("onlinetest.txt")
    for line in testfile.readlines():
        temp = line[:-1] #除去换行符
        p = Test.prediction(temp, wordsweight)
        if p > 0.5 :
            print temp + ":垃圾信息 "+str(p)
        else:
            print temp + ":正常信息 "+str(p)