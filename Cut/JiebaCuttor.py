#encoding:utf-8
'''
Created on Feb 27, 2015

@author: root
'''
import jieba

def cutstring(l,wordsmap,wordsweight):
    seglist = jieba.cut(l)
    for value in seglist:
        word = value.encode('utf-8')
#         print word
        if wordsmap.has_key(word) == False:
            wordsmap[word] = 0
        wordsmap[word] += 1
        #添加到特征权重
        if wordsweight.has_key(word) == False:
            wordsweight[word] = 0
    
if __name__ == '__main__':
    str = "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"
    cutstring(str, {}, {})