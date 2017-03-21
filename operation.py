# -*- coding=utf-8 -*-
from Word2Vec import usingWikiAlias
import rdflib

def post(symptom, panduan, second_symptom):
    # Load OWL
    g = rdflib.Graph()
    g.parse('zh_gastrointestinal_iaso.owl')

    symptom_input = symptom

    # 判断是否是首次输入症状，panduan=='1'则不是
    # 并获得分词结果、同义词近义词结果
    if panduan == '1':
        symptom_z = symptom_input.strip().split(' ')
        for second_symptom_item in second_symptom:
            symptom_z.append(second_symptom_item)
            symptom_input += ' ' + second_symptom_item
        segment_result = symptom_z
        match_result = symptom_z
    else:
        match_result, segment_result, symptom_z = segment(symptom)

    # 如果没有相似症状
    if len(symptom_z) == 0:
        return symptom_input, None, None, None, None, None

    # 与本体进行症状匹配
    symptom_match = match_symptom(symptom_z, g)

    # 从本体中获得症状相关的疾病及条件概率
    conditional_probability = load_conditional_probability(symptom_match, g)

    # 朴素贝叶斯
    disease_idlist = naive_bayes(conditional_probability)

    # 从本体中获取疾病相关属性
    disease_dict = load_disease(disease_idlist, g)

    # 对疾病进行排序等操作
    disease_list = disease_final_process(disease_dict, len(symptom_match)/2)

    # 根据疾病列表从本体中获取相关症状
    related_symptom_list = get_related_symptom(disease_list, symptom_match, g)
    return symptom_input, segment_result, match_result, symptom_match, disease_list, related_symptom_list


def segment(symptom):
    match_result = usingWikiAlias.alias(symptom)
    '''
    EXAMPLE:
    match_result = [u'宝宝 (无同义词): 宝宝 宝贝 乖乖 囡囡 小鬼 宝贝疙瘩 宝贝儿 小宝宝 Biliary 即处 中山楼 启脾丸 隔此 9.3 臣籍 早显 及颜 恭谨',
                    u'腹痛 (无同义词): 起泡 腹痛 作词家 大和国 赴宴 雷管 里弄 库兹涅 茫茫 强赛 王晶 阵形']
    '''
    segment_result = []
    symptom_z = []
    for word in match_result:
        items = word.decode('utf-8').strip().split(':')
        segment_result.append(items[0])
        symptom_z.extend(items[1].strip().split(' '))
    return match_result, segment_result, symptom_z

def match_symptom(symptom_z, owl):
    symptom_owl = []
    p = 'http://www.w3.org/2000/01/rdf-schema#subClassOf'
    o = 'http://purl.obolibrary.org/obo/iasoid.owl#症状'
    q = u"select ?node where {?node <%s> <%s>}" % (p.decode('utf-8'), o.decode('utf-8'))
    result = owl.query(q)
    if len(result) == 0:
        return []
    for s in list(result):
        symptom_owl.append(s[0].split('#')[1])
    symptom_match = []
    for symptom in symptom_z:
        if symptom in symptom_owl:
            symptom_match.append(symptom)
    return symptom_match

def load_conditional_probability(symptom_list, owl):
    conditional_probability = []
    for symptom in symptom_list:
        p = 'http://www.w3.org/2002/07/owl#someValuesFrom'
        o = 'http://purl.obolibrary.org/obo/iasoid.owl#%s' % symptom
        q = u"select ?node where {?node <%s> <%s>}" % (p, o)
        result = owl.query(q)
        for node in list(result):
            p1 = 'http://www.w3.org/2002/07/owl#equivalentClass'
            p2 = 'http://purl.obolibrary.org/obo/iasoid#probability'
            for s,p,o in owl:
                if s == node[0] and p.encode('utf-8') == p2:
                    probability = o
                if o == node[0] and p.encode('utf-8') == p1:
                    disease = s
            conditional_probability.append((disease, float(probability)))
    return conditional_probability


def naive_bayes(conditional_probability):
    temp = {} #disease_idlist
    max_count = 0
    for did, p in conditional_probability:
        if not temp.has_key(did):
            temp[did] = {}
            temp[did]['probability'] = 1.0
            temp[did]['count'] = 0.0
        temp[did]['probability'] *= p
        temp[did]['count'] += 1.0
        if temp[did]['count'] > max_count:
            max_count = temp[did]['count']

    for did in temp.keys():
        for i in range(int(max_count - temp[did]['count'])):
            temp[did]['probability'] *= 0.01
    return temp

def load_disease(disease_idlist, owl):
    disease_list = {}
    for did in disease_idlist.keys():
        s = did
        p1 = 'http://purl.obolibrary.org/obo/iasoid#disease_probability'
        p2 = 'http://www.w3.org/2000/01/rdf-schema#label'
        p3 = 'http://www.w3.org/2000/01/rdf-schema#subClassOf'
        q1 = u"select ?node where {<%s> <%s> ?node}" % (s, p1)
        q2 = u"select ?node where {<%s> <%s> ?node}" % (s, p2)
        q3 = u"select ?node where {<%s> <%s> ?node}" % (s, p3)
        result1 = owl.query(q1)
        result2 = owl.query(q2)
        result3 = owl.query(q3)
        disease_list[did] = {}
        disease_list[did]['id'] = did
        disease_list[did]['disease_probability'] = float(list(result1)[0][0])
        disease_list[did]['title'] = list(result2)[0][0]
        disease_list[did]['department'] = '肛肠科疾病'#list(result3)[0][0].split('#')[1]
        disease_list[did]['probability'] = disease_list[did]['disease_probability'] * disease_idlist[did]['probability']
        disease_list[did]['symptom_count'] = disease_idlist[did]['count']
        #print disease_list[did]['title'],disease_list[did]['department'],disease_list[did]['probability'],disease_list[did]['symptom_count']
    return disease_list

def disease_final_process(disease_dict, threshold):
    sorted_disease_list = sorted(disease_dict.values(), lambda x, y : cmp(x['probability'], y['probability']), reverse=True)
    probability_total = 0.0
    disease_final_list = []
    for disease in sorted_disease_list:
        if disease['symptom_count'] >= threshold:
            disease_final_list.append(disease)
            probability_total += disease['probability']
    if len(disease_final_list) < 4:
        disease_final_list = []
        probability_total = 0.0
        for disease in sorted_disease_list:
            disease_final_list.append(disease)
            probability_total += disease['probability']
    for disease in disease_final_list:
        disease['probability'] /= probability_total
    return disease_final_list

def get_related_symptom(disease_list, symptom_list, owl):
    related_symptom = []
    for disease in disease_list:
        s = disease['id']
        p1 = 'http://www.w3.org/2002/07/owl#equivalentClass'
        p2 = 'http://www.w3.org/2002/07/owl#someValuesFrom'
        q1 =  u"select ?node where {<%s> <%s> ?node}" % (s, p1)
        result1 = owl.query(q1)
        for node in list(result1):
            for s,p,o in owl:
                if s == node[0] and p.encode('utf-8') == p2:
                    symptom = o
                    if symptom.split('#')[1] not in symptom_list:
                        related_symptom.append(symptom.split('#')[1])
    return related_symptom


if __name__ == '__main__':
    #test()
    post('宝宝腹痛', None, None)


