#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 11:49
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 最小公倍数.py
# @Software: PyCharm
# @Describe: 最小公倍数 = 两数之积除以最大公约数

def gcd(a, b):
    # 求最大公约数
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # 求最小公倍数
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

if __name__ == '__main__':
    while True:
        try:
            num1, num2 = map(int,input().split())
            result = lcm(num1, num2)
            # numMax = num1 if num1>num2 else num2
            # numMin = num1 if num1<num2 else num2
            # result = 0
            # if numMax % numMin ==0:
            #     result = numMax
            # else:
            #     if (num1 %2 !=0) or (num2 %2 !=0): # 两个数中有一个是奇数
            #         result = num1 * num2
            #     elif (num1 %2 ==0) and (num2 %2 ==0): # 两个数都是偶数
            #         num1_zc = num1 // 2 # 整除的结果
            #         num2_zc = num2 // 2 # 整除的结果
            #         result = 2 * num1_zc * num2_zc
            print(result)
        except:
            break