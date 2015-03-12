#encoding:utf-8
'''
Created on Mar 9, 2015

@author: root
'''
import string

harmwordcount = {}
harmsentence = 1
spamwordcount = {}
spamsentence = 1

if __name__ == '__main__':
    file = open("train.txt")
    
#     Cut.YahaCuttor.init()
    for line in file.readlines():
        words = line.split(' ')
        wordsmap = {}
        #去除标点符号
        delset = string.punctuation
        l = words[0].translate(None,delset)
        
        for i in range(0,len(l.decode('utf-8'))-1):
            word = l.decode('utf-8')[i:i+1].encode('utf-8')
            #print word
            if words[1] == "spam":
                spamsentence += 1
                if spamwordcount.has_key(word) == False:
                    spamwordcount[word] = 1
                spamwordcount[word] += 1
            else:
                harmsentence += 1
                if harmwordcount.has_key(word) == False:
                    harmwordcount[word] = 1
                harmwordcount[word] += 1
    
    #保存结果
    fileharmsave = open('result_harm.txt', 'w')
    for k in harmwordcount.keys():
        fileharmsave.write(k + " " + str(harmwordcount[k]) + ' \r\n')
    fileharmsave.close()
    
    filespamsave = open('result_spam.txt', 'w')
    for k in spamwordcount.keys():
        filespamsave.write(k + " " + str(spamwordcount[k]) + ' \r\n')
    filespamsave.close()
    
    filesentencesave = open('result_sentence.txt', 'w')
    filesentencesave.write("harm " + str(harmsentence) + ' \r\n')
    filesentencesave.write("spam " + str(spamsentence) + ' \r\n')
    filesentencesave.close()