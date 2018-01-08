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
import json

import textDealer
import  DBconnector
from ExtractKeywords.keywords import result
import gensim, logging
def alias(symptom_input):  #zlz：如果模块是被导入，__name__的值为模块名字;如果模块是被直接执行，__name__的值为’__main__’
    reload(sys)
    sys.setdefaultencoding('utf-8')
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


    def loadFileToTrain(filepath, content):
        f = open(filepath, 'r')
        count = 0

        for line in f:
            count += 1
            if count >= 1000000:
                break
            # print line
            # print isinstance(line, unicode)
            # print chardet.detect(line)
            sentence = []
            line = line.replace('　', '')  # .decode('GB2312','ignore').encode('utf-8')
            temp = line.split(' ')
            for i in temp:
                if i == ' ' or i == '' or i == ' ':
                    continue
                # print i
                # print chardet.detect(i)
                i.strip()
                i.lstrip()
                i.rstrip()
                if len(i) > 2:
                    sentence.append(i)
            if len(sentence) > 2:
                sentences.append(sentence)
        # for i in xrange(100):
        #     print sentences[i]
        return sentences


    def trainWord2Vec(sentences):
        #/var/www/html/test/Application/Home/Controller/Word2Vec/
        file_path = 'testjieba/neike_out.txt'


    #firstRun = True
    firstRun = False

    if firstRun:

        sentences = []

        file_path = 'Word2Vec/testjieba/'

        sentences += loadFileToTrain(file_path + 'neike_out.txt', '')
        print len(sentences)
        sentences += loadFileToTrain(file_path + 'abstract_baidu_out.txt', '')
        print len(sentences)
        sentences += loadFileToTrain(file_path + 'abstract_hudong_out.txt', '')
        print len(sentences)

        # file_path = u'C:\Users\PrlNcE\Desktop\wiki分词之后的结果\\'
        filename = 'seg_wiki'

        sentences += loadFileToTrain(file_path + filename, '')
        print len(sentences)

        model = gensim.models.Word2Vec(sentences, min_count=10)
        # model.save('/mymodel_wds')
        # model.save('/mymodel_zq_internalMed')
        model.save('Word2Vec/mymodel_wds_wiki_all')


    else:
        # model = gensim.models.Word2Vec.load('/mymodel_wds')
        model = gensim.models.Word2Vec.load('Word2Vec/mymodel_wds_wiki_all')
        # model = gensim.models.Word2Vec.load('/mymodel_zq_internalMed')

    # zlz：测试
    #user_input = "流鼻涕"
    user_input = symptom_input
    #
    # user_input = user_input.decode("utf-8")
    # user_input = user_input.encode("ISO-8859-1")
    # print user_input
    # print "123456"
    # user_input = "宝宝发烧了，深夜拉肚子，感冒，流感，晚上失眠，还流鼻涕，少许，大量，微量，庞大，较多，肾炎，咳嗽。" \
    # "肌电图提示持续性的感觉运动脱髓鞘性多发神经病，推断可能是营养缺乏导致的症状。在接受 8 天的医院供餐以及维生素 B1 补充后，患者症状有所改善。他的既往病史为慢性酗酒史和退行性关节疾病，长期的高血压病史未接受治疗。患者神清，定向力正常，颅神经正常，没有感觉障碍，上下肢重度无力，心、肺和腹部未见明显异常，足部轻度水肿。"

    # 从张强的程序里面获取结果
    words = result(user_input, 5)

    #for i in words:
        #print i

    symptoms = []  # ['腹痛','腹泻','恶心','呕吐','包块','呕吐','宿食','振水音','老年人','黑便','龛影','抽搐','上腹痛','腹部包块','消瘦','成人','受凉','发烧','咳铁锈色痰','青少年','高热']

    # 从文件里获取症状
    file_path = 'Word2Vec/symptom_wds.txt'
    # filename = 'seg_wiki'
    f = open(file_path, 'r')
    count = 0

    for line in f:
        symptoms.append(line[:-1])

    # 利用alias同义词
    alias_dic = {}
    alias_set = set()
    alias_list = []
    res = DBconnector.getAll()

    for i in res:
        # print i[0],i[1]
        alias_dic[i[0]] = alias_dic.get(i[0], []) + [i[1]]
        # if i[0] not in alias_dic.keys():
        #     alias_dic[i[0]] = [i[1]]
        # else:
        #     alias_dic[i[0]].append(i[1])

    # zlz：注释
    # print len(symptoms)

    hit_dic = textDealer.getSynonym()

    # print len(hit_dic)

    # final_dic = combineTwoDics(alias_dic,hit_dic)

    ret = []
    # print "1234"
    for word in words:

        # print byte(word)
        # zlz：注释掉
        # print '--------'
        # zlz：注释掉
        # print word,':',
        # t_set = set()
        t_set = set()
        #zlz：测试
        res_zz="";
        for k, v in alias_dic.items():
            # print k,v
            if word == k or word in v:
                t_set.add(k)
                res_zz=res_zz+k
                for i in v:
                    t_set.add(i)
                    res_zz=res_zz+i+" "

        word = word.encode('utf-8')
        for k, v in hit_dic.items():
            # print chardet.detect(v[0])
            # print chardet.detect(word)
            if word in v[:]:
                for i in v:
                    # print i
                    t_set.add(i)
                    res_zz=res_zz+i+" "

        if len(t_set) !=  -10:
            # zlz：测试
            try:
                res = model.most_similar(word)

                # res_zz += '||w2c:'
                for i in res:
                   res_zz=res_zz+i[0]+" "
                    # print i[0], i[1]
                # print ''
                ret.append(word+'(无同义词):'+res_zz)
                print word, '(无同义词):',res_zz
            except:
                continue
            continue

        ret.append(word+':'+res_zz)
        print word, ':',res_zz
        # for i in t_set:
            # print i,
        # print ''

    return ret





