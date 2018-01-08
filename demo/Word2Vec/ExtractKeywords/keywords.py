#!/usr/bin/env python
#coding=utf-8

'''
    segment userInput and corpus, and output according to TFIDF.
    you can set the number of keywords in result(sentence,k)
    note:segmenting corpus is very slow, but we can finish it offline.

    @author: zhangqiang
    @date: 2016/4/15
'''

import jieba
import codecs
from TFIDF import TFIDF
import re
import json

import chardet

def fenci(sentence):
    #导入自定义词典
    #加载字典导致参差速度有些慢
    # jieba.load_userdict('ExtractKeywords/dataset/diseaseDict.txt')

    #加入停用词此表，分词后去停用词
    stopwords = frozenset((line.rstrip() for line in codecs.open('Word2Vec/ExtractKeywords/dataset/stopword.txt','r','utf-8')))
    #print stopwords

    segs = jieba.cut(sentence)

    #print "分词列表:", " ".join(jieba.cut(sentence))
    cutWords = ''
    for seg in segs:
        if seg not in stopwords:
            cutWords += seg + ' '
    cutWords = cutWords.strip()#去掉开头和结尾的空格
    cutWords = re.split(r'[\s]+', cutWords)#去掉字符之间的空格
    #print '去停用词:',json.dumps(cutWords,encoding='utf-8',ensure_ascii=False)
    #print '-------------------------------------------------------------------------------'
    return cutWords

def result(sentence,k):
    cutWords = fenci(sentence)
    #将语料库中每一行进行分词
    #zlz：注释
    # print("正在对语料库内容分词，请等待...")
    cutCorpuss = []
    for line in open('Word2Vec/ExtractKeywords/dataset/corpus.txt').readlines():
        cutCorpus = fenci(line)
        cutCorpuss.append(cutCorpus)
    #print("语料库内容分词结束！")
    #将用户输入和语料库中分词结果传给TFIDF函数
    tfidfs,myset = TFIDF(cutWords,cutCorpuss)
    cutWords = [i for i in myset]
    cutWordsdict = dict(zip(cutWords,tfidfs))#将列表转化为字典
    #print '分词TFIDF值字典：',json.dumps(cutWordsdict,encoding='utf-8',ensure_ascii=False)
    sortCutWordsdict = sorted(cutWordsdict.iteritems(), key=lambda d:d[1], reverse = True)#将字典按值排序
    #print '分词TFIDF值字典排序：',json.dumps(sortCutWordsdict,encoding='utf-8',ensure_ascii=False)

    #sortCutWordsdict = tuple(sortCutWordsdict)
    wordlist = []
    for i in sortCutWordsdict:
        #print json.dumps(i,encoding='utf-8',ensure_ascii=False) #+  '\r\n'
        wordlist.append(i[0])
    #zlz：先注释掉
    # print"用户输入内容按重要性排序：",json.dumps(wordlist,encoding='utf-8',ensure_ascii=False)
    # print json.dumps(wordlist, encoding='utf-8', ensure_ascii=False)

    j = 0
    wordlistk = []
    for i in sortCutWordsdict:
        if j<k:
            j += 1
            wordlistk.append(i[0])
    # zlz：先注释掉
    # print"输出前%s个关键词："%k,json.dumps(wordlistk,encoding='utf-8',ensure_ascii=False)
    # print json.dumps(wordlistk, encoding='utf-8', ensure_ascii=False)


    #print chardet.detect(wordlist[0].encode('utf8'))
    return wordlist


if __name__ == '__main__':
    userInput = u'我最近感觉不舒服,咳嗽，流鼻涕，拉肚子，' \
               u'可能是得了肺结核病，假期肌肤综合症，还有点头疼呢'
    res = result(userInput,20)

    for i in res:
        print i

