#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 20:16
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@
# @Site    : 
# @File    : 最少换钱问题.py
# @Software: PyCharm
# @Describe: https://blog.csdn.net/qq_34342154/article/details/77104520

# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

def minCoins2(arr, aim):
    if arr == None or len(arr) == 0 or aim < 0:
        return -1
    row = len(arr)
    dp = [sys.maxsize for i in range(aim+1)]
    dp[0] = 0
    for i in range(1, aim+1):
        if i % arr[0] == 0:
            dp[i] = i // arr[0]
    for i in range(1, row):
        dp[0] = 0
        for j in range(1, aim+1):
            left = sys.maxsize
            if j - arr[i] >= 0 and dp[j-arr[i]] != sys.maxsize:
                left = dp[j-arr[i]] + 1
            dp[j] = min(left, dp[j])
    return dp[aim] if dp[aim] != sys.maxsize else -1

# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************

def solution(prices, budget):
    if prices == None or len(prices) == 0 or budget < 0:
        return -1
    row = len(prices)
    dp = [[sys.maxsize for i in range(budget + 1)] for j in range(row)]
    for i in range(row):
        dp[i][0] = 0
    for j in range(1, budget + 1):
        if j % prices[0] == 0:
            dp[0][j] = j // prices[0]
    for i in range(1, row):
        for j in range(1, budget + 1):
            left = sys.maxsize
            if j - prices[i] >= 0 and dp[i][j - prices[i]] != sys.maxsize:
                left = dp[i][j - prices[i]] + 1
            dp[i][j] = min(left, dp[i - 1][j])
    return dp[row - 1][budget] if dp[row - 1][budget] != sys.maxsize else -1

def coins5(arr, aim):
    if arr == None or len(arr) == 0 or aim < 0:
        return 0
    dp = [0 for i in range(aim+1)]
    for i in range(aim//arr[0]+1):
        dp[arr[0]*i] = 1
    for i in range(len(arr)):
        for j in range(1, aim+1):
            dp[j] += dp[j-arr[i]] if j-arr[i] >= 0 else 0
    return dp[aim]
# ******************************结束写代码******************************


_prices_cnt = 0
_prices_cnt = int(input())
_prices_i = 0
_prices = []
while _prices_i < _prices_cnt:
    _prices_item = int(input())
    _prices.append(_prices_item)
    _prices_i += 1

_budget = int(input())

res = solution(_prices, _budget)

print(str(res) + "\n")