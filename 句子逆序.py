#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/24 20:34
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 句子逆序.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    while True:
        try:
            strIn = input()
            if strIn:
                ls = strIn.split(" ")
                ls.reverse()
                print(' '.join(ls))
            else:
                break
        except:
            break