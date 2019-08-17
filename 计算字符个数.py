#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 17:20
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 计算字符个数.py
# @Software: PyCharm
# @Describe: 
if __name__ == '__main__':
    while True:
        try:
            a = input().lower()
            b = input().lower()
            print(a.count(b))
        except:
            break
