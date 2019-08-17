#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 19:46
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 整型负数转二进制.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            if n>0:
                sbit = bin(n)
                print(sbit[2:]) # 输出不含"0b"的二进制字符串
                print(sbit,type(sbit))
                print(sbit.count('1')) # 输出二进制符串中 1 的个数
            else:
                hexstr = hex(n,0xFFFFFFFF)
                sbit_fu = bin(hexstr)

        except:
            break