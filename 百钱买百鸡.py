#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 17:32
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 百钱买鸡.py
# @Software: PyCharm
# @Describe: 

# 100只鸡
# x+y+z =100
# 100钱
# 5x+3y +z/3 = 100

def func():
    for i in range(0, 21):
        for j in range(0, 34):
            if 5 * i + 3 * j + (100 - i - j) / 3.0 == 100:
                print(i, j, (100 - i - j))

if __name__ == '__main__':
    while True:
        try:
            n = input()
            if n:
                func()
            else:
                break
        except:
            break