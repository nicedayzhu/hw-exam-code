#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 18:45
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : int_1_count.py
# @Software: PyCharm

if __name__ == "__main__":
    num = int(input())
    flag = 0
    while num > 0:
        if(num % 2):
            flag +=1
        num = num // 2
    print(flag)
