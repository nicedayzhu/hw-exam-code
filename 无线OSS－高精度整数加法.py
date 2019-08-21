#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 15:41
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 无线OSS－高精度整数加法.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    while True:
        try:

            a = eval(input())
            b = eval(input())
            if a and b:
                print(a+b)
            else:
                break
        except:
            break