#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 19:08
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 求三角形.py
# @Software: PyCharm
# @Describe: 给定三角形周长，求满足周长的直角三角形个数

if __name__ == '__main__':
    ls = []
    n = int(input())
    for x in range(1,n//3):
        yushu = (n**2-2*x*n)%(2*n-2*x)
        if yushu:
            pass
        else:
            y = (n**2-2*x*n)//(2*n-2*x)
            ls.append([x,y,n-x-y])
    print(ls)