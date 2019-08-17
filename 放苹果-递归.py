#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 10:36
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 放苹果.py
# @Software: PyCharm

# 链接：https://www.nowcoder.com/questionTerminal/bfd8234bb5e84be0b493656e390bdebf
# 来源：牛客网
#
# //分为两种情况，1：每个盘子都有苹果，2：存在至少一个空盘子。//
# //第一种即每个盘子先放一个，剩余m-n个放进n个盘子，即f(m-n,n)//
# //第二种情况，等价于最后一个盘子不放时的总个数，因为只要最后一个盘子不放苹果，就至少有空盘子 //
# //第二种即f(m,n-1),所以f(m,n)=f(m,n-1)+f(m-n,n)。//
def putApple(m, n):
    if m == 0 or n == 1:
        return 1
    if n > m:
        return putApple(m, m)
    else:
        return putApple(m, n - 1) + putApple(m - n, n)


if __name__ == '__main__':
    while True:
        try:
            m, n = map(int, input().split())
            print(putApple(m, n))
        except:
            break
