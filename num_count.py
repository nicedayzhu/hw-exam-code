#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 16:14
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : num_count.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    ls = [1,2,3,3,3,3]
    len_ls = len(ls) /2
    count = 0
    for i in ls:
        geshu = ls.count(i)
        print(i)
        print(geshu)