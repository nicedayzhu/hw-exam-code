#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 16:23
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@
# @Site    : 
# @File    : 称砝码.py
# @Software: PyCharm
# @Describe: 
def fama(n,weight,nums):
    # 计算第一列
    # weight nums
    # 1   *   0
    # 1   *   1
    # 1   *   2

    res = set()
    for i in range(nums[0]+1):
        res.add(weight[0]*i)

    for i in range(1,n): # 计算 n-1 轮， res即为不重复的重量集合
        temp = list(res)
        for num in range(1,nums[i]+1):
            for rr in temp: #变成list在这里才能遍历
                res.add(rr+weight[i]*num)
    return len(res)
while True:
    try:
        n = int(input())
        weight = [int(i) for i in input().split()]
        nums = [int(i) for i in input().split()]
        print(fama(n,weight,nums))
    except:
        break
