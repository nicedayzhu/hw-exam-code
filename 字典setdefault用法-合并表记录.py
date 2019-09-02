#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 20:31
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@
# @Site    : 
# @File    : 合并表记录.py
# @Software: PyCharm
# @Describe: Python 字典(Dictionary) setdefault()方法
# https://www.runoob.com/python/att-dictionary-setdefault.html
# 描述
# Python 字典 setdefault() 函数和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
#
# 语法
# setdefault() 方法语法：
#
# dict.setdefault(key, default=None)
# 参数
# key -- 查找的键值。
# default -- 键不存在时，设置的默认键值。
# 返回值
# 如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值。

# count = int(input())
# c = {}
# for _ in range(count):
#     k, v = [ i for i in map(lambda x: int(x) ,input().split(' '))]
#     c[k] = c.setdefault(k, 0) + v
# for k, v in c.items():
#     print(k, v)


def solution():
    dicin = {}
    for i in range(n):
        k, v = map(int, input().split())
        if k in dicin.keys(): # 如果key已经存在于dicin的键中，那么把value相加
            dicin[k] = dicin[k] + v
        else:
            dicin[k] = v
    # print(dicin)
    for i in sorted(dicin.keys()): # 对 key 进行排序，升序
        print(str(i) + " " + str(dicin[i]))
    # print(dicin.keys())

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            if n:
                solution()
            else:
                break
        except:
            break
