#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 20:49
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 尼科彻斯定理.py
# @Software: PyCharm
# @Describe: 任何一个整数m的立方都可以写成m个连续奇数之和。

def GetSequeOddNum(n):
    res = n ** 3
    mid = int(res / n) # 获得立方后数值的平均值，即中间的那个数
    ls = []
    count = n // 2
    if mid % 2==1: # 如果中间的数是奇数
        ls.append(mid)
        for i in range(count):
            ls.append(mid - 2 * (i + 1))
            ls.append(mid + 2 * (i + 1))
    else: # 如果中间的数是偶数
        for i in range(count):
            ls.append(mid - (2*i + 1))
            ls.append(mid + (2*i + 1))
    return ls

if __name__ == '__main__':
    while True:
        try:
            n = input()
            if n:
                new_ls = GetSequeOddNum(int(n))
                new_ls.sort()
                length = len(new_ls)
                for i in range(length):
                    # 顺序打印数字和加号，最后一个数字不需要在后面追加 "+" 号
                    if i !=length -1:
                        print(new_ls[i], end='')
                        print("+",end='')
                    else:
                        print(new_ls[i])
            else:
                break
        except:
            break


