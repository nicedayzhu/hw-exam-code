#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 10:35
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 查找两个字符串a,b中的最长公共子串.py
# @Software: PyCharm
# @Describe: 
def cutStr2(str):
    ls_cut = []
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            sub = str[i:j]
            ls_cut.append(sub)
    return ls_cut

if __name__ == '__main__':
    while True:
        try:
            s1 = input().strip() # strip()方法，用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
            s2 = input().strip()
            if s1 =='' or s2 =='':
                break
            n=0
            sub_max = ''
            if len(s1)>len(s2): # 求长度最小的序列，最小序列为s1
                s1,s2 = s2,s1
            for i in range(len(s1)):
                for j in range(i+1,len(s1)+1):
                    sub = s1[i:j]
                    if sub in s2 and j-i>n: # 如果s1子串能够在s2中找到，并且字串长度大于上一个子串长度，则把此字串赋值给最大子串
                        n = j-i
                        sub_max = sub
            print("".join(sub_max))
        except:
            break