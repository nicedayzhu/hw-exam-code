#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 11:17
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 去重排序-不改变原来位置顺序.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    str1 = list(input())
    ls_n = [int(x) for x in str1] # 将str1中的数字字符转为整型数字
    print(str1)
    str_o = list(set(str1))
    print(str_o)
    str_o.sort(key=str1.index) # 按照原来顺序输出
    print(str_o)

    print(ls_n)
    ls_n_set = list(set(ls_n))
    print(ls_n_set)
    ls_n_set.sort(key=ls_n.index) # 按照原来顺序输出
    print(ls_n_set)