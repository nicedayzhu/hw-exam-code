#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 21:06
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 超长正整数相加.py
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
