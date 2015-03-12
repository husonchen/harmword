#encoding:utf-8
'''
Created on Feb 27, 2015

@author: root
'''
import sys, re, codecs
import cProfile
from yaha import Cuttor, RegexCutting, SurnameCutting, SurnameCutting2, SuffixCutting
from yaha.wordmaker import WordDict
from yaha.analyse import extract_keywords, near_duplicate, summarize1, summarize2, summarize3

cuttor = Cuttor()

def init():
    cuttor.set_stage1_regex(re.compile('(\d+)|([a-zA-Z]+)', re.I|re.U))
    surname = SurnameCutting2()
    cuttor.add_stage(surname)
    suffix = SuffixCutting()
    cuttor.add_stage(suffix)
    
def cutstring(str,wordsmap,wordsweight):
    seglist = cuttor.cut(str)
    for value in list(seglist):
        word = value.encode('utf-8')
        print word
        if wordsmap.has_key(word) == False:
            wordsmap[word] = 0
        wordsmap[word] += 1
        #添加到特征权重
        if wordsweight.has_key(word) == False:
            wordsweight[word] = 0
            
if __name__ == '__main__':
    init()
    str = "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"
    