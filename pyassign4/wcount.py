#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Cai Jiahao"
__pkuid__  = "1800011783"
__email__  = "caijiahao@pku.edu.cn"
"""

sys=input()
s=sys.split()
from urllib.request import urlopen
import string
import urllib
import http.client

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
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

    if  len(s) == 1:
        print('A')
    else:
        url = s[1]    #获得输入的网址
        if len(s) >= 3:
            if str.isdigit(s[2]):
                topn = int(s[2])   #获得topn
            else:
                print('输入的topn必须是正整数，不能是{}'.format(s[2]))    #给定非法topn时
                topn = 0
        elif len(s) == 2:
            topn = 10    #未给定topn时
        
            
    
        txt = urlopen(url)    #打开网页获得txt文件
        txt_bytes = txt.read()    #得到字节流形式文本
        txt.close()    #关掉网页
        txt_str = txt_bytes.decode('UTF-8','strict')    #字节流解码为字符串形式
        txt_lower = txt_str.lower()   #换为小写以方便统计
        l = txt_lower.split()
        wcount(l,topn)
        
        
        print(l)   #统计次数输出前topn

