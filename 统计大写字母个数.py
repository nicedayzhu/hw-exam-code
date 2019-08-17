#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 18:50
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 统计大写字母个数.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    count = 0
    while True:
        try:
            ls = input()
            if ls:
                for i in ls:
                    if 64<ord(i)<91:
                        count +=1
                print(count)
                count = 0
            else:
                break
        except:
            break