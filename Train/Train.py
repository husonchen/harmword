#encoding:utf-8
import string
from numpy import *
wordsweight = {} #特征词的权重
threshold = 0.49 #TONE训练法的阈值
rate = 0.003

'''
计算样本和权重向量的乘积
'''
def arraymult(wordmap,weight):
    sum = 0;
    for k in wordmap.keys():
        wordnum = wordmap.get(k)
        if weight.has_key(k):
            sum += wordnum * weight.get(k)
    return sum
    
'''
样本梯度下降更新权重向量
'''    
def gradientdes(wordmap,weight,rate,p):
    desval = rate * p
    for k in wordmap.keys():
        if weight.has_key(k):
            weight[k] -= desval

'''
样本梯度上升更新权重向量
'''      
def gradientup(wordmap,weight,rate,p):
    upval = rate * (1-p)
    for k in wordmap.keys():
        if weight.has_key(k):
            weight[k] += upval


if __name__ == '__main__':
    file = open("train.txt")
    for line in file.readlines():
        words = line.split(' ')
        wordsmap = {}
        #去除标点符号
        delset = string.punctuation
        l = words[0].translate(None,delset)
        #把该条句子按照4-gram（中文2个字）划分特征
        for i in range(0,len(l.decode('utf-8'))-1):
            word = l.decode('utf-8')[i:i+2].encode('utf-8')
#             print word
            if wordsmap.has_key(word) == False:
                wordsmap[word] = 0
            wordsmap[word] += 1
            #添加到特征权重
            if wordsweight.has_key(word) == False:
                wordsweight[word] = 0
        
        #计算向量x和w的乘积
        xw = arraymult(wordsmap, wordsweight)
        expxw = exp(xw)
        #计算概率p
        p = expxw/(1+expxw)
        predict = "ham" #正常
        if p > 0.5:
            predict = "spam" #垃圾
        
        #TONE训练法
        if abs(p - 0.5) < threshold or predict != words[1]:
            #正例则梯度上升
            if words[1] == "spam":
                print "spam:"+line
                gradientup(wordsmap,wordsweight,rate,p)
            else:
                #反例则梯度下降
                print "ham:"+line
                gradientdes(wordsmap,wordsweight,rate,p)
    
    #保存结果
    filesave = open('result.txt', 'w')
    for k in wordsweight.keys():
        filesave.write(k + " " + str(wordsweight[k]) + ' \r\n')
    filesave.close()
