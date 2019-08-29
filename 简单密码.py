#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 17:22
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 简单密码.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    while True:
        try:
            str_in = list(input())
            if str_in:
                for i in range(len(str_in)):
                    if 'A'<=str_in[i]<='Z':
                        if str_in[i] =='Z':
                            str_in[i] = 'a'
                        else:
                            str_in[i] = chr(ord(str_in[i].lower())+1)
                        # print(str_in[i])
                    elif 'a'<=str_in[i]<='c':
                        str_in[i] = '2'
                    elif 'd'<=str_in[i]<='f':
                        str_in[i] = '3'
                    elif 'g'<=str_in[i]<='i':
                        str_in[i] = '4'
                    elif 'j'<=str_in[i]<='l':
                        str_in[i] = '5'
                    elif 'm'<=str_in[i]<='o':
                        str_in[i] = '6'
                    elif 'p'<=str_in[i]<='s':
                        str_in[i] = '7'
                    elif 't'<=str_in[i]<='v':
                        str_in[i] = '8'
                    elif 'w'<=str_in[i]<='z':
                        str_in[i] = '9'
                print(''.join(str_in))
            else:
                break
        except:
            break