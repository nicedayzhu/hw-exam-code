#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 21:08
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 提取不重复的整数.py
# @Software: PyCharm
# @Describe:
# https://blog.csdn.net/shuifa2008/article/details/38085955
# python 使用set对列表去重，并保持列表原来顺序
# https://blog.csdn.net/Jerry_1126/article/details/84677212


if __name__ == '__main__':
    while True:
        try:
            num_origin = list(input())
            if num_origin:
                num_origin.reverse() # 反转
                # print(num_origin)
                num_out = list(set(num_origin)) #去重
                num_out.sort(key=num_origin.index) # 按原来的顺序输出
                print(''.join(num_out))
            else:
                break
        except:
            break