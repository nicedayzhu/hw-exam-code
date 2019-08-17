#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 11:23
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 二进制1的个数.py
# @Software: PyCharm
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            sbit = bin(n)
            print(sbit[2:]) # 输出不含"0b"的二进制字符串
            print(sbit,type(sbit))
            print(sbit.count('1')) # 输出二进制符串中 1 的个数
        except:
            break