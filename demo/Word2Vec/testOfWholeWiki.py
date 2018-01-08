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



sentences = []
# file_path = 'C:\Users\PrlNcE\Desktop\wiki\\'
# filename = 'seg_wiki'
# f = open(file_path +'\\' + filename,'r')
# count = 0
#
# for line in f:
#     count += 1
#     if count >= 2000000:
#         break
#     #print line
#     #print isinstance(line, unicode)
#     #print chardet.detect(line)
#     sentence = []
#     line = line.replace('　','')#.decode('GB2312','ignore').encode('utf-8')
#     temp = line.split(' ')
#     for i in temp:
#         if i == ' ' or i == '' or i == ' ':# or i == '' or i == '@@' or i :
#             continue
#         #print i
#         #print chardet.detect(i)
#         i.strip()
#         i.lstrip()
#         i.rstrip()
#         if len(i) > 2:
#             sentence.append(i)
#         #sentences.append([i])
#     if len(sentence) > 2:
#         sentences.append(sentence)




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
#model.save('/mymodel_wiki')

model = gensim.models.Word2Vec.load('/mymodel_wiki')


words = ['许多']#,'头痛','感冒','头疼','发烧','发热','高热','青年','老头','老人','成年人']
''' '''
for word in words:
    print '----------------'
    print 'word:',word
    res = model.most_similar(word)#.encode('utf-8'))

    for i in res:
        print i[0],i[1]
    print ''


# symptoms = ['腹痛','腹泻','恶心','呕吐','包块','呕吐','宿食','振水音','老年人','黑便','龛影','慢性溃疡疼痛规律改变','上腹痛','腹部包块','消瘦','左锁骨上淋巴结肿大','成人','受凉','发烧','咳铁锈色痰','青少年','高热']
#
# for word in words:
#     print '--------------'
#     res = ''
#     maxx_sim = 0
#     for i in symptoms:
#         try:
#             #print word,i,model.similarity(i,word)
#             if model.similarity(i,word) > maxx_sim:
#                 maxx_sim = model.similarity(i,word)
#                 res = i
#         except:
#             continue
#     print 'res:',word,res

#print model.
