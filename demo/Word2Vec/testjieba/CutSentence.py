#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path


print '你'

count = 1
file_path= 'D:\linshi\hudong_html_after_analyze'
out_path = 'D:\linshi\hudong_seged\\'

for a,b,filenames in os.walk('D:\linshi\hudong_html_after_analyze'):
    for filename in filenames:
        if count > 2:
            break
        count += 1

        f = open(file_path +'\\' + filename,'r')
        content = f.read()

        content.replace('@@','')
        content.replace('None','')

        content = content.split('。')
        res = ''
        for i in content:
            #print i
            i = i.strip()
            i = i.lstrip()
            i = i.rstrip()
            if '@@' == i or 'None' == i:
                continue
            res += i + '\n'
        print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        print res



'''
import codecs

if __name__ == '__main__':
    my_filepath = ['testset1/','testset2/','testset3/','testset4/','testset5/','testset6/','testset7/','testset8/','testset9/','testset10/']

    filepath = "wds.txt"

    file_obj = codecs.open(filepath,'r','utf-8')
    try:
        content = file_obj.read()
    finally:
        file_obj.close()

    for i in range(0,len(my_filepath)):
        sent_len = 25
        filepath = my_filepath[i]

        count = 0
        sentences = []

        while count < sent_len:
            juhao = u"。"
            index = content.index(juhao) + 1
            sentence = content[:index]
            content = content[index:]

            if len(sentence) > 0:
                count += 1
                sentence=sentence.strip('\r\n')
                sentence = sentence.replace("\r","")
                sentence = sentence.replace("\n","")
                sentences.append(sentence)

        print len(sentences)

        file_object = open(filepath + "test1.txt",'w')
        file_object.write("\n".join(sentences))
        file_object.close()
'''