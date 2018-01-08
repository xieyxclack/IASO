#!/usr/bin/python  
#-*- coding: utf-8 -*-
filename = '/var/www/html/test/Application/Home/Controller/Word2Vec/readableVersion.txt'

file_symptoms = '/var/www/html/test/Application/Home/Controller/Word2Vec/symptoms.txt'

#f = open(filename, "r")
#out = open(filename + 'res', 'w')
#text = ""
#    text = f.get()

path = ''

def getFileContent(filename):

    f = open(path + filename,"r")
    return f


#计算两个单词的编辑距离
def wordEditDistance(m,n):
    """compute the least steps number to convert m to n by insert , delete , replace .
    动态规划算法,计算单词距离
    print word_distance("abc","abec")
    1
    print word_distance("ababec","abc")
    3
    """

    len_1=lambda x:len(x)+1
    c=[[i] for i in range(0,len_1(m)) ]
    c[0]=[j for j in range(0,len_1(n))]

    for i in range(0,len(m)):
    #    print i,' ',
        for j in range(0,len(n)):
            c[i+1].append(
                min(
                    c[i][j+1]+1,#插入n[j]
                    c[i+1][j]+1,#删除m[j]
                    c[i][j] + (0 if m[i]==n[j] else 1 )#改
                )
            )
    #        print c[i+1][j+1],m[i],n[j],' ',
    #    print ''
    edit_distance = c[-1][-1]
    edit_distance_score = 1.0 - (edit_distance+0.0) / max(len(m),len(n))
    return edit_distance_score# c[-1][-1]


#to get the synonyms
def getSynonym():
    ''''''
    count = 0

    dic = {}

    synonym_data = getFileContent("/var/www/html/test/Application/Home/Controller/Word2Vec/readableVersion.txt")

    #this is to get all the synonyms,and put in a dict
    for line in synonym_data:
    #    print line#
        count += 1
        if count == 100000:
            break
        line = line[:-1]
        line = line.decode("utf8",'ignore').encode('utf-8')
        #print line 

        temp = line.split(' ')

        # 跳过只有一个词的同义词行
        if len(temp) <= 2:
            continue

        key = temp[0]
        # for j in temp[1:]:
        #     pass#print j

        dic[key] = temp[1:]
    return dic


def getSymptoms():

    symptoms_list = []
    symptoms_data = getFileContent("symptoms.txt")

    for line in symptoms_data:
        line.strip()
        symptoms_list.append(line[:-1])

    print 'all symptoms:',
    for i in symptoms_list:
        print i,
    print ''
    return symptoms_list
    #print symptoms_list



def searchWordInTotal(dic,symptoms_list,word_list):
    for word in word_list:
        print '---------------------'
        print '用户输入的词：',word

        word_candidate_list = []
        for (k, v) in dic.items():
            for j in v:
                if word == j:
                    #this is to print the dic items
                    #print k,
                    for j in v:
                        if j not in word_candidate_list:
                            word_candidate_list.append(j)
                        #print j,
                    #print ''
                    break


        #this is to print the word_candidate_list
        print '\nword_candidate_list:',
        for i in  word_candidate_list:
            print i,
        print '\n'


        #this is to the result
        print '匹配的标准描述：',
        for i in  word_candidate_list:
            #print i
            if i in symptoms_list:
                print i
        print ''


def searchWordByEach(dic,symptoms_list,word_list):
    for word in word_list:
        print '---------------------'
        print '用户输入的词：',word

        word_candidate_list = []
        for (k, v) in dic.items():
            for j in v:
                if word == j:
                    #this is to print the dic items
                    #print k,
                    for j in v:
                        if j not in word_candidate_list:
                            word_candidate_list.append(j)
                        #print j,
                    #print ''
                    break


        #this is to print the word_candidate_list
        print '\nword_candidate_list:',
        for i in  word_candidate_list:
            print i,
        print '\n'


        #this is to the result
        print '匹配的标准描述 的 编辑距离：\n',

        max_similarity = 0
        res_word = ''

        for i in  symptoms_list:
            #print i
            similarity = 0
            for j in word_candidate_list:
                #print i,j
                i = unicode(i)
                j = unicode(j)
            #    print i,j,wordEditDistance(i,j)
                similarity += wordEditDistance(i,j)
            #print similarity
            if similarity > max_similarity:
                max_similarity = similarity
                res_word = i
        print '',res_word
        if res_word == '':
            print '~~~~'
            searchDirectlyFromStandardSymptpms(word,symptoms_list)



        #return res_word


def searchDirectlyFromStandardSymptpms(word,symptoms_list):

    max_similarity = 0
    res_word = ''

    for i in symptoms_list:
        print i,
        similarity = wordEditDistance(i,word)

        if similarity > max_similarity:
            max_similarity = similarity
            res_word = i

    print '\n ##',i


# word = '瘦'
# word_list1 = ['瘦','老头','肚子疼','大人','发烧','着凉']
#
# word_list2 = ['发烧','肚子疼']
#
#
#
# dic = getSynonym()
#
# print len(dic)
#
# for i,j in dic.items():
#     # print i,j
#     for jj in j:
#         print jj,
#     print ''



# symptoms_list = getSymptoms()
# searchWordInTotal(dic,symptoms_list,word_list1)



# print '######################'
# print '######################'
# print '######################'
# res_word = searchWordByEach(dic,symptoms_list,word_list2)



#计算编辑距离
# str1 = u'发高烧'
# str2 = '发烧'

# str2 = unicode(str2)
#print len(str2)


#print wordEditDistance(str1,str2)










