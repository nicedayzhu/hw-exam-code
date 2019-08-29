#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 19:34
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 2019-8-28-华为第三题.py
# @Software: PyCharm
# @Describe: 

def cut(s):
    results = []

    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            if x == 0:
                results.append(s[i:i + x + 1])
            elif x < 2:
                for j in range(len(s) - x - i):
                    results.append(s[i] + s[j + x + i])
            else:
                for j in range(len(s) - x - i):
                    results.append(s[i:i+x] + s[j + x + i])

    return results

if __name__ == '__main__':
    n = int(input())
    ls1 = input().split()
    ls2 = input().split()
    cut_ls1 = cut(ls1)
    cut_ls2 = cut(ls2)
    print(cut_ls1)
    print(cut_ls2)
    for item in cut_ls1:
        if item in cut_ls2:
            print(item)