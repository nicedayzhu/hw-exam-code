#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 10:38
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 整数转二进制.py
# @Software: PyCharm
# @Describe: 

# 整数转二进制：
# 1、采用%2的方式计算
# 2、采用python自带了方法 bin.
# 比如bin(10) 回返回字符串'0b1010' ，只留下‘0’，‘1’序列需要把‘0b’去掉.
number = int(input())
bin(number).replace('0b','') # 或bin(number)[2:]
# >>> bin(10)  // 为了下边表示方便 放入t中
# '0b1010'
