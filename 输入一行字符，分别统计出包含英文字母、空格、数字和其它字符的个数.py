#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 19:14
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@
# @Site    : 
# @File    : 输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    while True:
        try:
            str_in = input()
            if str_in:
                alpha_count = 0
                space_count = 0
                num_count = 0
                other = 0
                for i in str_in:
                    if 'a'<=i<='z' or 'A'<=i<='Z':
                        alpha_count +=1
                    elif 48<=ord(i)<=57:
                        num_count +=1
                    elif i ==' ':
                        space_count +=1
                    else:
                        other +=1
                print(alpha_count)
                print(space_count)
                print(num_count)
                print(other)
            else:
                break
        except:
            break