#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 16:35
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 自守数.py
# @Software: PyCharm
# @Describe:自守数是指一个数的平方的尾数等于该数自身的自然数。
# 例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。请求出n以内的自守数的个数

def zishou(n):
    """如果满足自守数，则返回True，否则返回False
    :param n:
    :return:
    """
    temp = str(n**2)
    aim_len = len(str(n))
    cut_temp = temp[-aim_len:] #从后面截取长度为输入数字长度的正序字符串
    if str(n) == cut_temp:
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            if n:
                count = 0
                for i in range(n+1):
                    flag = zishou(i)
                    if flag:
                        count +=1
                print(count)
            else:
                break
        except:
            break

