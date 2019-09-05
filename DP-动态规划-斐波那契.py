#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 16:42
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@
# @Site    : 
# @File    : 斐波那契-动态规划.py
# @Software: PyCharm
# @Describe: 

# https://blog.csdn.net/lz867422770/article/details/80660831
# 递归的的斐波那契数列解决方法 时间复杂度O(2^n)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# print(fib(50))

# 动态规划 先解决小数据量的 再层层递推的解决大数据量级的问题 时间复杂度O(n)
def fib2(n):
    memo = [-1 for x in range(n + 1)]
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


# print(fib2(50))

# 记忆化搜索

def fib3(n):
    MAXSIZE = 1000
    memo = [-1 for i in range(MAXSIZE)]

    if n == 0:
        return 0
    if n == 1:
        return 1
    if memo[n] == -1:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]

#动态规划版Python代码
def Fibonacci(n):
    """
    https://blog.csdn.net/songyunli1111/article/details/80283429
    :param n:
    :return:
    """
    a=0
    b=1
    for i in range(n-1):
        a=a+b
        a,b=b,a
    return b

if __name__ == '__main__':

    n = int(input())
    out = Fibonacci(n)
    print(out)