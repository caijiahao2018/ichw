#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Cai Jiahao"
__pkuid__  = "1800011783"
__email__  = "caijiahao@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import string
import urllib
import http.client


def wcount(lines, topn=10):
    """count words from the text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """
    sy='''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
    sym=list(sy)  #建立标点符号列表
    d={}
    for i in lines:
        if i!='':
            s_n=''
            l=list(i)       
            while l!=[]:
                if l[0] in sym:
                    del l[0]
                else:
                    break
            while l!=[]:
                if l[-1] in sym:
                    del l[-1]
                else:
                    break   #去除列表首尾的符号
            if l!=[]:        
                for i in l:
                    s_n=s_n+i          #将去首尾符号的列表还原为单词
                if s_n in d.keys():
                    d[s_n]=d[s_n]+1
                else:
                    d[s_n]=1              #对单词进行统计
    dl=list(d.items())
    dl.sort(key=lambda x:x[1],reverse=True)    #排序
    if len(dl)<topn:
        for i in dl:
            for j in i:
                print(j,'\t',end='') 
            print('\t')                     
    else:
        for i in range(topn):
            for j in dl[i]:
                print(j,'\t',end='')
            print('\t')                #输出前topn项

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many words to output. If not given, will output top 10 words')
        sys.exit(1)

    else:
        url = sys.argv[1]    #获得输入的网址
        if len(sys.argv) >= 3:
            if str.isdigit(sys.argv[2]):
                topn = int(sys.argv[2])   #获得topn
            else:
                print('输入的topn必须是正整数，不能是{}'.format(sys.argv[2]))    #给定非法topn时
                topn = 0
        elif len(sys.argv) == 2:
            topn = 10    #未给定topn时
        
            
        try:
            txt = urlopen(url)    
            txt_bytes = txt.read()    
            txt.close()    
            txt_str = txt_bytes.decode('UTF-8','strict')    #字节流解码为字符串形式
            txt_lower = txt_str.lower()    #换为小写
            l=txt_lower.split()             #转化为列表
            wcount(l,topn)    #输出前topn项

        except urllib.error.HTTPError:    
            print(sys.exc_info()[1]) 
        except urllib.error.URLError:    
            print(sys.exc_info()[1])
        except http.client.RemoteDisconnected:
            print(sys.exc_info()[1])      
        except ValueError:
            print('输入的网址格式不正确')    
