#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 15:27
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 按字节截取字符串.py
# @Software: PyCharm
# @Describe: 编写一个截取字符串的函数，输入为一个字符串和字节数，输出为按字节截取的字符串。
# 但是要保证汉字不被截半个，如"我ABC"4，应该截为"我AB"，输入"我ABC汉DEF"6，应该输出为"我ABC"而不是"我ABC+汉的半个"。

while True:
    try:
        a, b = input().split()
        print(a[:int(b)])

    except:
        break