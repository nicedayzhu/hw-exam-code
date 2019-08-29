#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 11:13
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 输入多个abcd.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            # print("ABCD" * int(input()))
            for i in range(n):
                print("ABCD",end='')
                if i ==n-1:
                    print("")
        except:
            break