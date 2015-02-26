#encoding:utf-8
'''
Created on Feb 26, 2015
@author: root
'''
import Train
from numpy import *
import string

wordsweight = {}

'''
计算分类
'''
def prediction(wordstr,weight): 
    wordsmap = {}
    #去除标点符号
    delset = string.punctuation
    l = wordstr.translate(None, delset)
    # 把该条句子按照4-gram（中文2个字）划分特征
    for i in range(0, len(l.decode('utf-8')) - 1):
        word = l.decode('utf-8')[i:i + 2].encode('utf-8')
#         print word
        if wordsmap.has_key(word) == False:
            wordsmap[word] = 0
        wordsmap[word] += 1
        
    # 计算向量x和w的乘积
    xw = Train.arraymult(wordsmap, weight)
    expxw = exp(xw)
    # 计算概率p
    p = expxw / (1 + expxw)
    return p
    
    
if __name__ == '__main__':
    #读取权重文件
    resultfile = open("result.txt")
    for line in resultfile.readlines():
        temp = line.split(' ')
        wordsweight[temp[0]] = float(temp[1])
        
    #检查测试集合
    testfile = open("test.txt")
    hamwrong = 0 #正常的判定为垃圾的个数
    spamwrong = 0 #垃圾的判断为正常的个数
    total = 0
    for line in testfile.readlines():
        temp = line.split(' ')
        p = prediction(temp[0],wordsweight)
        category = "ham"
        if p > 0.5:
            category = "spam"
        #如果错误
        if category != temp[1]:
            print temp[0]+" "+str(p)+" "+ temp[1]+"判定为"+category
            if temp[1] == "ham":
                hamwrong += 1
            else :
                spamwrong += 1
        total += 1
    
    print "正常的判定为垃圾的概率:"+ str(float(hamwrong)/total*100)+"%"
    print "垃圾的判断为正常的概率:"+ str(float(spamwrong)/total*100)+"%"