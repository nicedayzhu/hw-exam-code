#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 11:38
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 棋盘格子走法种类.py
# @Software: PyCharm

# 组合问题，在 n + m中选取n个向下的路径，C(4,2)组合数
def zuhe(n, m):
    """
    :param n: 长
    :param m: 宽
    :return:  组合数
    """
    s_b = 1 # s_b指的是组合数公式下面的数
    s_t = 1 # s_t指的是组合数公式上面的数
    t = n + m
    for i in range(n):
        s_b = s_b * (i+1)
        s_t = s_t * (t-i)
    return int(s_t / s_b)


if __name__ == '__main__':
    while True:
        try:
            n, m = map(int, input().split())
            res = zuhe(n, m)
            print(res)
        except:
            break
