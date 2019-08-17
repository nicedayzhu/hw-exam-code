#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 16:18
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 兔子个数-斐波那契数列.py
# @Software: PyCharm
# @Describe: 链接：https://www.nowcoder.com/questionTerminal/1221ec77125d4370833fd3ad5ba72395?f=discussion
# 来源：牛客网
#
#     ///关键是找到递推式 f(n)=f(n-1)+f(n-2) (n>=4)
#     ///递推式的解释:对于第n个月的兔子数量：有两部分组成，
#     ///一部分是上个月的兔子f(n-1)，另一部是满足3个月大的兔子
#     ///会生一只兔子f(n-2)

if __name__ == '__main__':
    while True:
        try:
            month = int(input())
            if month:
                ls = [0]*100 # 初始化100个数
                ls[1] = ls[2] =1
                ls[3] = 2

                for i in range(4,100):
                    ls[i] = ls[i-1] + ls[i-2]
                print(ls[month])
            else:
                break
        except:
            break