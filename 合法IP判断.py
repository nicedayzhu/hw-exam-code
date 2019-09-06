#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/5 20:00
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@
# @Site    : 
# @File    : 合法IP判断.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    while True:
        try:
            myls = [int(x) for x in input().split('.')]
            if myls:
                flag = 0
                for i in range(len(myls)):
                    if i== 0:
                        if 1<=myls[i]<=255:
                            flag = 1
                        else:
                            flag = 0
                            break
                    else:
                        if 0<=myls[i]<=255:
                            flag = 1
                        else:
                            flag = 0
                            break
                if flag:
                    print("YES")
                else:
                    print("NO")
            else:
                break
        except:
            break