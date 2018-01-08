#!/usr/bin/env python
#coding=utf-8

'''
    caculate TFIDF

    @author: zhangqiang
    @date: 2016/4/15
'''

from __future__ import division
import math


def TFIDF(cutWords,cutCorpuss):
    #计算TF值
    length = len(cutWords)
    myset = set(cutWords) #myset是另外一个列表，里面的内容是mylist里面的无重复项
    #print set(cutWords)
    tfs = []#所有元素的tf值列表
    for item in myset:
        tf = cutWords.count(item)/length#结果为实数，需要from __future__ import division
        tfs.append(tf)
    #print 'TF值：',tfs

    #计算IDF值，以语料库中的一行（问诊记录）为一个文档
    totalDocs = len(cutCorpuss)
    idfs = []

    for item in myset:
        count = 0
        for doc in cutCorpuss:
            if item in doc:
                count += 1
        idfs.append(math.log(totalDocs/(count+1)))
    #print 'IDF值：',idfs

    #计算TF-IDF值
    tfidfs = []
    for i in range(len(tfs)):
        tfidfs.append(tfs[i]*idfs[i])
    #print 'TF-IDF值',tfidfs

    return tfidfs,myset

