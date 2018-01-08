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
from ExtractKeywords.keywords import result

# import modules & set up logging
import gensim, logging

#sys.setdefaultencoding('utf-8')

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

firstRun = True
#firstRun = False

if firstRun:

    sentences = []
    file_path = '/var/www/html/test/Application/Home/Controller/Word2Vec/testjieba/neike_out.txt'
    #filename = 'seg_wiki'
    f = open(file_path,'r')
    count = 0

    for line in f:
        count += 1
        if count >= 2000000000:
            break
        #print line
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



    model = gensim.models.Word2Vec(sentences, min_count=3)
    # model.save('/mymodel_wds')
    model.save('/mymodel_zq_internalMed')

else:
    model = gensim.models.Word2Vec.load('/mymodel_wds')
    # model = gensim.models.Word2Vec.load('/mymodel_zq_internalMed')






# words = ['拉肚子','头痛','感冒','头疼','发烧','发热','高热','青年',
#          '老头','老人','成年人','抽筋','睡不着','瘦','抑郁','流鼻涕']

user_input = '少许'
    # "我发烧了，拉肚子，心情不好，晚上失眠，还流鼻涕。" \
             #"肌电图提示持续性的感觉运动脱髓鞘性多发神经病，推断可能是营养缺乏导致的症状。在接受 8 天的医院供餐以及维生素 B1 补充后，患者症状有所改善。他的既往病史为慢性酗酒史和退行性关节疾病，长期的高血压病史未接受治疗。患者神清，定向力正常，颅神经正常，没有感觉障碍，上下肢重度无力，心、肺和腹部未见明显异常，足部轻度水肿。"

#从张强的程序里面获取结果
words = result(user_input,5)


for i in words:
    i = i.encode('utf-8')
# words = ['晚上']
''''''
# for word in words:
#     print '----------------'
#     print 'word:',word
#     try:
#         res = model.most_similar(word)#.encode('utf-8'))
#
#         for i in res:
#             print i[0],i[1]
#         print ''
#     except:
#         continue







symptoms = []#['腹痛','腹泻','恶心','呕吐','包块','呕吐','宿食','振水音','老年人','黑便','龛影','抽搐','上腹痛','腹部包块','消瘦','成人','受凉','发烧','咳铁锈色痰','青少年','高热']

#从文件里获取症状
file_path = '/var/www/html/test/Application/Home/Controller/Word2Vec/symptom_wds.txt'
#filename = 'seg_wiki'
f = open(file_path,'r')
count = 0

for line in f:
    # count += 1
    # if count >= 200:
    #     break
    #print line[:-1]
    symptoms.append(line[:-1])

# for i in symptoms:
#     print i


for word in words:
    print '--------------'
    res = ''
    maxx_sim = 0
    word = word.encode('utf-8')
    print 'word:',word#,chardet.detect(word)

    #计算整个 word2vec 里面，与这个词最接近的十个词
    # try:
    #     res = model.most_similar(word)
    #
    #     for i in res:
    #         print i[0],i[1]
    #     print ''
    # except:
    #     continue

    try:
        res = model.most_similar(word)

        for i in res:
            print i[0],i[1]
        print ''
    except:
        continue


    #二次迭代
    # 计算整个 word2vec 里面，与这个词最接近的十个词
    dic = {}

    resWordsNum = 10
    s_dic = []

    try:
        res = model.most_similar(word)
        count = 10
        for i in res:
            count -= 1
            print i[0],i[1]

            res2 = model.most_similar(i[0])
            for j in res2:
                #print ' '+j[0],j[1]
                if j[0] not in dic.keys():
                    # dic[j[0]] = (i[1] + count + 10) * j[1]
                    dic[j[0]] = (i[1]) * j[1]
                    print i[1] + 10 + count,j[1]
        print ''

        print len(dic)
        s_dic = sorted(dic.iteritems(), key = lambda d:d[1], reverse = False)
        # print type(s_dic)


        #打印结果
        for i in s_dic:
            print i[0],i[1]
    except:
        continue


    #二次迭代的结果进行一个聚类，然后再跟所有的症状进行计算，总分

    res_dic = {}
    dic_num = len(s_dic)
    for i in symptoms:
        score = 0
        for j in s_dic:
            try:
                t = model.similarity(i,j[0]) * j[1]
                score += t

            except:
                continue
        res_dic[i] = score
        # if score != 0:
        #     print i,score

    print '\n\nbelow is the together result'
    res_list = sorted(res_dic.iteritems(), key = lambda d:d[1], reverse = False)
    for i in res_list[len(res_list) - 10 :]:
        if i[1] == 0:
            continue
        print i[0],i[1]



    #与全部标准症状进行比较，取最高的
    res = ''
    for i in symptoms:
        try:
            #print word,i,model.similarity(i,word)
            if model.similarity(i,word) > maxx_sim and i != word:
                maxx_sim = model.similarity(i,word)
                res = i
        except:
            continue
    print 'res:',word,res

#print model.
