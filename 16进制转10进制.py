#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 21:07
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 16进制转10进制.py
# @Software: PyCharm
# @Describe: 
# python常用的十进制、16进制、字符串、字节串之间的转换
# https://blog.csdn.net/crylearner/article/details/38521685

if __name__ == '__main__':
    while True:
        try:
            num = input()
            if num:
                print(int(num, 16))
            else:
                break
        except:
            break
