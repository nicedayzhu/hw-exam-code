#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 20:27
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 2019-8-14-华为-字符串拆分.py
# @Software: PyCharm
# @Describe: a,,"b,"""
if __name__ == '__main__':
    while True:
        try:
            mystr = input()
            newls = []
            if mystr:
                ls = mystr.split(',')
                print(ls)
                for i in range(len(ls)-1):
                    if ls[i].count('"')>0 and ls[i+1].count('"')>0:
                        single = ls[i] + ls[i+1]
                        print(single)
                        if single[0] == single[-1] =='"':
                            print(single[1:-1])
                            strange = single[1:-1]
                            # for v in range(len(strange)):
                            #     if strange[v] =
                    else:
                        newls.append(ls[i])
                print(newls)
            else:
                break
        except:
            break