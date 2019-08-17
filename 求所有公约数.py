#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 21:42
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 求所有公约数.py
# @Software: PyCharm

def yueshu(n):
    """
    :param n: 输入整数
    :return: 包含所有公约数的list
    """
    ls = list()
    # 开方降低计算时间复杂度
    for i in range(int( n ** 0.5 )):
        # 计算商和余数
        div = divmod(n, i+1)
        # 如果余数是0
        if(div[1] == 0):
            ls.append(div[0])
            ls.append(i+1)
    # 去重
    ls_res = list(set(ls))
    # 从大到小排列
    ls_res.sort()
    return ls_res

if __name__ == '__main__':
    n = int(input())
    ls = yueshu(n)
    print(ls)