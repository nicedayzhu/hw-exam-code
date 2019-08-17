#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 19:44
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 计算字符串最后一个单词的长度.py
# @Software: PyCharm
if __name__ == '__main__':
    a = input()
    list = a.split(" ")
    print(len(list[-1]))

