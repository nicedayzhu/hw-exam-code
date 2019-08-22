#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 21:09
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 字符个数统计(ASCII).py
# @Software: PyCharm
# @Describe: 编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)。不在范围内的不作统计。

if __name__ == '__main__':
    while True:
        try:
            str_ls = list(input())
            count = 0
            if str_ls:
                str_ls = set(str_ls)
                print(str_ls)
                for item in str_ls:
                    if 0<=ord(item)<127:
                        count +=1
                print(count)
            else:
                break
        except:
            break
