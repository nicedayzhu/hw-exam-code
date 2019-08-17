#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 20:26
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    :
# @File    : 字符串逆序输出.py
# @Software: PyCharm
# list的切片有三个参数:起点,终点,步长
#
# list[::-1] 相当于起点为最后的一个,终点为第一个,然后一次减少一个
# >>> a = [0,1,2,3,4,5,6,7,8,9]
# >>> a
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> a.reverse()
# >>> a
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# >>> a.reverse()
# >>> a
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> a[:]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> a[::]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> a[5::-1]
# [5, 4, 3, 2, 1, 0]
# >>> a[:5:-1]
# [9, 8, 7, 6]
# >>> a[5:1:-1]
# [5, 4, 3, 2]

# 方法一，切片
if __name__ == "__main__":
    num = input()
    print(num[::-1])
    # 方法二：列表reverse()
    # ls = list(num)
    # ls.reverse()
    # print(''.join(ls))