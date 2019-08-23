#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 20:14
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : （练习用）挑7.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    while True:
        try:
            num = int(input())
            ls = []
            count = 0
            if num<7:
                print(0)
            else:
                if num:
                    for i in range(1,num+1):
                        if ('7' in str(i)) or (i%7 ==0): # 如果字符串i包含7，或者数i 能被7整除，则进行计数
                            ls.append(i)
                            count+=1
                    # print(ls)
                    print(count)
                else:
                    break
        except:
            break