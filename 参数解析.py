#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/27 16:12
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 提取输入参数.py
# @Software: PyCharm
if __name__ == '__main__':
    s = input()
    ls = s.split(" ")
    print(len(ls))
    for item in ls:
        print(item)