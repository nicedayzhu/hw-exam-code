#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 21:07
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 求最大连续bit数.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            max = 0
            if n:
                sbit = bin(n)
                sbit = sbit[2:]
                # print(sbit)
                count = 0
                for i in sbit:
                    if i=='1': # 判断每个元素是否为 1
                        count +=1
                    else:       # 如果不为1，则计数清零
                        count = 0
                    if count>max:
                        max = count
                print(max)
            else:
                break
        except:
            break