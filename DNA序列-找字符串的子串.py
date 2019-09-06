#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 10:46
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@
# @Site    : 
# @File    : DNA序列.py
# @Software: PyCharm
# @Describe:
#
# 找到长度为5的所有子串

def cutStr(str,n):
    out_str = []
    for i in range(len(str)-n+1):
        sub = str[i:i+n]
        out_str.append(sub)
    return out_str

if __name__ == '__main__':
    while True:
        try:
            mystr = input()
            mystr_len = len(mystr)
            num = int(input())
            if mystr:
                # out_dic = {}
                max_GC = 0
                max_index = 0
                out_cut = cutStr(mystr,num)
                for i in range(len(out_cut)):
                    G_C = out_cut[i].count('G') + out_cut[i].count('C')
                    G_C_All = G_C / mystr_len
                    if G_C_All>max_GC:
                        max_GC = G_C_All
                        max_index = i
                        # out_dic[i] = out_dic.setdefault(i,out_cut[i]) # 如果找到G_C 比大于默认值的，就把子串添加到新字典
                # max_k = max(out_dic.keys()) # 找到字典中key值最大的元素
                # print(out_dic[max_k])
                print(out_cut[max_index])
            else:
                break
        except:
            break


