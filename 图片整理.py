#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 19:40
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 图片整理.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    while True:
        try:
            lsin = list(input()) # 将输入字符串存放到list
            if lsin:
                lsin.sort() # list排序，按照ascii码值从小到大
                # print(lsin)
                outls = ''.join(lsin) # list元素转字符串输出
                print(outls)
            else:
                break
        except:
            break