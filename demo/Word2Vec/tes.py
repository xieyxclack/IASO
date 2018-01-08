#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'PrlNcE'

import os.path
import sys
import multiprocessing
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import chardet

# import modules & set up logging
import gensim, logging

#sys.setdefaultencoding('utf-8')

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#sentences = [['first', 'sentence'], ['second', 'sentence']] * 10000
#sentences = [['我','爱'],['让我们看一下训练好的中文维基百科']] * 20000

sentences = []


count = 1
file_path= 'C:\Users\PrlNcE\Desktop\Word2Vec\hudong_seged'
for a,b,filenames in os.walk(file_path):
    for filename in filenames:
        if count > 1111111:
            break
        count += 1
        #print chardet.detect(filename)




        f = open(file_path +'\\' + filename,'r')
        for line in f:
            #print isinstance(line, unicode)
            #print chardet.detect(line)
            sentence = []
            line = line.replace('　','')#.decode('GB2312','ignore').encode('utf-8')
            temp = line.split(' ')
            for i in temp:
                if i == ' ' or i == '' or i == ' ':# or i == '' or i == '@@' or i :
                    continue
                #print i
                #print chardet.detect(i)
                i.strip()
                i.lstrip()
                i.rstrip()
                if len(i) > 2:
                    sentence.append(i)
                #sentences.append([i])
            if len(sentence) > 2:
                sentences.append(sentence)




#sentences = [['感冒','发热']]*10000
'''

print len(sentences)
for i in sentences:
    if len(i) < 1:
        print 'NNNNNNNNNNNNNNNNNNNNNNNNNNNN'
    #print i#,chardet.detect(i)
    for j in i:
        print j+'||',
    print ''
'''


#model = gensim.models.Word2Vec(sentences, min_count=3)
#model.save('/mymodel')

model = gensim.models.Word2Vec.load('/mymodel')


words = ['腹泻','感冒','头疼','发烧','发热','高热']

for word in words:
    print '----------------'
    print 'word:',word
    res = model.most_similar(word)#.encode('utf-8'))

    for i in res:
        print i[0],i[1]
    print ''




print model.similarity("感染","流感")
