#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 9:31
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 等差数列.py
# @Software: PyCharm
# @Describe: 

def getSum(n):
    sum = int((3*n + 1)*n/2)
    return sum

if __name__ == '__main__':
    while True:
        try:
            n = int(input()) # 获取输入，如果输入不是整数则跳出程序
            if n:
                sum = getSum(n)
                print(sum)
            else:
                break
        except:
            break
