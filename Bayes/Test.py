#encoding:utf-8
'''
Created on Mar 9, 2015

@author: root
'''
import string

harmwordRate = {}
spamwordRate = {}
harmRate = 0
spamRate = 0

def prediction(line):
    spamP = float(1)
    harmP = float(1)
    for i in range(0,len(line.decode('utf-8'))-1):
        word = line.decode('utf-8')[i:i+1].encode('utf-8')
        #print word
        if spamwordRate.has_key(word):
            spamP *= spamwordRate[word]
        if harmwordRate.has_key(word):
            harmP *= harmwordRate[word]
    spamP *= spamRate
    harmP *= harmRate
#     print spamP
    if spamP > harmP:
        return "spam"
    else:
        return "ham"
    
if __name__ == '__main__':
    
    harmwordcount = {}
    harmsentence = 1
    spamwordcount = {}
    spamsentence = 1

    #读取权重文件
    harmfile = open("result_harm.txt")
    for line in harmfile.readlines():
        temp = line.split(' ')
        harmwordcount[temp[0]] = float(temp[1])
    harmfile.close();
    
    spamfile = open("result_spam.txt")
    for line in spamfile.readlines():
        temp = line.split(' ')
        spamwordcount[temp[0]] = float(temp[1])
    spamfile.close();
    
    sentencefile = open("result_sentence.txt")
    for line in sentencefile.readlines():
        temp = line.split(' ')
        if temp[0] == "harm":
            harmsentence = float(temp[1])
        else:
            spamsentence = float(temp[1])
    sentencefile.close();
    
    totalsentence = harmsentence + spamsentence
    
    
    for k in harmwordcount.keys():
        harmwordRate[k] = harmwordcount[k] / harmsentence
    for k in spamwordcount.keys():
        spamwordRate[k] = spamwordcount[k] / spamsentence
    
    harmRate = harmsentence / totalsentence
    spamRate = spamsentence / totalsentence
    
    #检查测试集合
    testfile = open("test.txt")
    hamwrong = 0 #正常的判定为垃圾的个数
    spamwrong = 0 #垃圾的判断为正常的个数
    total = 0
    for line in testfile.readlines():
        temp = line.split(' ')
        #去除标点符号
        delset = string.punctuation
        l = temp[0].translate(None,delset)
        category = prediction(temp[0])
        #如果错误
        if category != temp[1]:
            print temp[0]+" "+ temp[1]+"判定为"+category
            if temp[1] == "ham":
                hamwrong += 1
            else :
                spamwrong += 1
        total += 1
    
    print "正常的判定为垃圾的概率:"+ str(float(hamwrong)/total*100)+"%"
    print "垃圾的判断为正常的概率:"+ str(float(spamwrong)/total*100)+"%"