#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 11:29
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 汉诺塔.py
# @Software: PyCharm

# 总次数为：2^n - 1
def move(n, a, b, c):
    if n == 1:   # 如果a只有1盘子
        print(a, '-->', c);   # 直接把盘子从a移到c
    else:   # 如果a有n个盘子(n > 1)，那么分三步
        move(n-1, a, c, b)   # 先把上面n-1个盘子，借助c，从a移到b
        move(1, a, b, c)   # 再把最下面的1个盘子，借助b，从a移到c
        move(n-1, b, a, c)   # 最后把n-1个盘子，借助a，从b移到c

if __name__ == '__main__':
    move(6,'A','B','C')  # 测试