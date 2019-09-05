#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 20:22
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@
# @Site    : 
# @File    : 坐标移动.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    while True:
        try:
            x = 0
            y = 0
            ls = input().split(';')
            for i in range(len(ls)):
                if 'A' in ls[i]:
                    try:
                        num_left = int(ls[i][1:])
                        x -=num_left
                    except:
                        pass

                elif 'S' in ls[i]:
                    try:
                        num_down = int(ls[i][1:])
                        y -= num_down
                    except:
                        pass

                elif 'D' in ls[i]:
                    try:
                        num_right = int(ls[i][1:])
                        x += num_right
                    except:
                        pass

                elif 'W' in ls[i]:
                    try:
                        num_up = int(ls[i][1:])
                        y += num_up
                    except:
                        pass
            print(str(x) + ',' + str(y))
        except:
            break