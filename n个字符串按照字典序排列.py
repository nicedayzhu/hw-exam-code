#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 21:10
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : n个字符串按照字典序排列.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            ls = []
            for i in range(n):
                ls.append(input())
            ls.sort()
            for i in ls:
                print(i)
        except:
            break