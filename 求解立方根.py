#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 18:38
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@
# @Site    : 
# @File    : 求解立方根.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    while True:
        try:
            n = float(input())
            if n:
                res = n**(1/3)
                print("%.1f" % res)
            else:
                break
        except:
            break