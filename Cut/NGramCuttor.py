#encoding:utf-8
'''
Created on Feb 27, 2015

@author: root
'''
def cutstring(l,wordsmap,wordsweight):
    #把该条句子按照4-gram（中文2个字）划分特征
    for i in range(0,len(l.decode('utf-8'))-1):
        word = l.decode('utf-8')[i:i+2].encode('utf-8')
        #print word
        if wordsmap.has_key(word) == False:
            wordsmap[word] = 0
        wordsmap[word] += 1
        #添加到特征权重
        if wordsweight.has_key(word) == False:
            wordsweight[word] = 0
        
if __name__ == '__main__':
    pass