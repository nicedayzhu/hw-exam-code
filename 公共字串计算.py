#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 19:47
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 公共字串计算.py
# @Software: PyCharm
# @Describe: 

def cutStr(str):
    ls_cut = []
    for i in range(len(str)): # 从字符串的第 i个元素开始向后截取
        for j in range(len(str)-i): # 以第 i个元素开头的截取所有字符串的个数为 len(str)-i个
            ls_cut.append(str[i:i+j+1])
    ls_cut = list(set(ls_cut))
    # print(ls_cut)
    return ls_cut


if __name__ == '__main__':
    while True:
        try:
            # ls = input().strip().split() # 一行输入多个字符串，以空格分割
            lsa = input()
            lsb = input()
            if lsa and lsb:
                lsa = lsa.lower()
                lsb = lsb.lower()
                lsa_cut = cutStr(lsa)
                lsb_cut = cutStr(lsb)
                max = 0
                for i in range(len(lsa_cut)):
                    # if lsb_cut.count(lsa_cut[i]):
                    if lsa_cut[i] in lsb_cut: # 这个语句的意思是，如果 a能够在 b中找到，则返回True，否则返回False
                        # print(lsa_cut[i]) # 输出lsb_cut与lsa_cut中相同的字符串
                        max_temp = len(lsa_cut[i])
                        if max_temp>max:
                            max = max_temp
                print(max)
            else:
                break
        except:
            break


