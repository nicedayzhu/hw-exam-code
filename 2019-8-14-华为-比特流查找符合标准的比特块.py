#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 19:16
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 比特流查找符合标准的比特块.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    flag = 0
    while True:
        try:
            n = int(input())
            sbit = bin(n)
            sbit = sbit[2:] # 输出不含"0b"的二进制字符串
            reverse_sbit = sbit[::-1] # 逆序输出
            cut_ls = []
            for i in range(len(reverse_sbit)):
                block = reverse_sbit[i:i+3]
                cut_ls.append(block)
            print(cut_ls.count('101'),end=' ')
            for xuhao in range(len(cut_ls)):
                if cut_ls[xuhao] =="101":
                    print(xuhao)
                    flag = 1
                    break
            if flag == 0:
                print("-1")
            flag = 0
        except:
            break