#encoding:utf-8
'''
Created on Feb 26, 2015

@author: root
'''
import random
if __name__ == '__main__':
    datafile = open("data.txt")
    trainfile = open("train.txt","w")
    testfile = open("test.txt","w")
    totaldata = [i for i in range(1,26247)]
    test = random.sample(totaldata, 2624)
    print test
    linenum = 1
    for line in datafile.readlines():
        #测试数据
        if(linenum in test):
            testfile.write(line)
        else:#训练数据
            trainfile.write(line)
        linenum += 1
            