#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 17:09
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : ASCII码与字符相互转换.py
# @Software: PyCharm
# @Describe: 
if __name__ == '__main__':
    while True:
        try:
            c = input("请输入一个字符: ")

            # 用户输入ASCII码，并将输入的数字转为整型
            a = int(input("请输入一个ASCII码: "))

            print(c + " 的ASCII 码为", ord(c))
            print(a, " 对应的字符为", chr(a))
        # 下面的except异常是由print抛出的，而不是input，因为input没有输入的话，是 None （合法）
        except:
            break