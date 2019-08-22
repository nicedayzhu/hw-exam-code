#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 21:01
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 求n以下的所有质数.py
# @Software: PyCharm
# @Describe: 

def findSushu(num):
    """
    找出所有质数
    :param num:
    :return:
    """
    sushu_ls = []
    for i in range(2,num):
        if i == 2:
            sushu_ls.append(i)
            continue
        for j in range(2,i+1):
            if j == i:
                sushu_ls.append(i)
            if i % j ==0: # 如果能在 i一下的所有数中找到一个除了1和i本身之外，能够整除i的数，则跳出
                break
    return sushu_ls

if __name__ == '__main__':
    num = int(input())
    sushu = findSushu(num)
    print(sushu)