#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 16:50
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 计算日期到天数.py
# @Software: PyCharm
# @Describe: 

# 判断是否是闰年
def runNianDays(year):
    flag = 0
    if year % 100 == 0:
        if year % 400 == 0:
            flag = 1
        else:
            flag = 0
    elif year % 4 == 0:
        flag = 1
    else:
        flag = 0
    if flag:
        return 366
    else:
        return 365

if __name__ == '__main__':
    output = 0
    while True:
        try:
            # y = int(input())
            # m = input()
            # d = int(input())
            y, m, d = map(int, input().split())
            if y and m and d:
                month_days_p = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                month_days_r = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                days = runNianDays(y)
                if days == 365:
                    for i in range(m-1):
                        output +=month_days_p[i]
                    output_all = output + d
                else:
                    for i in range(m-1):
                        output += month_days_r[i]
                    output_all = output + d
                print(output_all)
                output = 0
            else:
                break
        except:
            break
