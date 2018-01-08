#encoding=utf-8

from zhcnSegment import *
import codecs,os

if __name__ == '__main__':


    file_path= 'C:\Users\PrlNcE\Desktop\Word2Vec\\testjieba\\abstract_hudong.txt'
    out_path = 'C:\Users\PrlNcE\Desktop\Word2Vec\\testjieba\\abstract_hudong_out.txt'

    file_obj = codecs.open(file_path,'r','utf-8')


    content = file_obj.read()
    segment = 100000
    pos = 0
    wds = Seg()
    while pos + segment < len(content):
        new_content = ''
        new_content = content[pos:pos + segment]
        #print len(content)
        print pos
        pos += segment


        seg_list = wds.cut(new_content)
        #print(" ".join(seg_list))

        res = " ".join(seg_list)


        output = open(out_path , 'a')
        output.write(res.encode('utf-8'))
        output.close()




    '''
    #this is the multi_file version

    count = 1
    file_path= 'D:\linshi\hudong_html_after_analyze'
    out_path = 'D:\linshi\hudong_seged\\'

    for a,b,filenames in os.walk('D:\linshi\hudong_html_after_analyze'):
        for filename in filenames:
            if count > 1111111:
                break
            #if count % 100 == 0:
            print count
            count += 1

            file_obj = codecs.open(file_path +'\\' + filename,'r','utf-8')
            try:
                content = file_obj.read()

                content = content.split(u'。')
                new_content = ''
                for i in content:
                    #print i
                    i = i.strip()
                    i = i.lstrip()
                    i = i.rstrip()
                    if '@@' == i or 'None' == i:
                        continue
                    new_content += i + '\n'
                #print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
                #print new_content

            finally:
                file_obj.close()

            wds = Seg()
            seg_list = wds.cut(new_content)
            #print(" ".join(seg_list))

            res = " ".join(seg_list)


            output = open(out_path + filename, 'w')
            output.write(res.encode('utf-8'))
            output.close()
        '''