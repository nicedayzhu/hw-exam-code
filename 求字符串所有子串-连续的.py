#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 10:40
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 求字符串所有子串-连续的.py
# @Software: PyCharm
# @Describe: 

def cutStr(str):
    ls_cut = []
    for i in range(len(str)): # 从字符串的第 i个元素开始向后截取
        for j in range(len(str)-i): # 以第 i个元素开头的截取所有字符串的个数为 len(str)-i个
            ls_cut.append(str[i:i+j+1])
    # ls_cut = list(set(ls_cut))

    # print(ls_cut)
    return ls_cut

def cutStr2(str):
    ls_cut = []
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            sub = str[i:j]
            ls_cut.append(sub)
    return ls_cut

if __name__ == '__main__':
    str_in = input()
    print(cutStr(str_in))