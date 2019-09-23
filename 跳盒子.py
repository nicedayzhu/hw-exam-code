#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 16:50
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@
# @Site    : 
# @File    : 跳盒子.py
# @Software: PyCharm
# @Describe: 

'''
 Welcome to vivo !
'''

def solution(step_list):

    if(step_list ==[] or len(step_list)==0):
        return -1
    reach = 0
    last = 0
    count = 0
    for i in range(len(step_list)):
        if i>reach:
            return -1
        if i>last:
            count +=1
            last = reach
        if((i+step_list[i]) >reach):
            reach = i+step_list[i]
    return count

if __name__ == '__main__':
    while True:
        try:
            step_list = [int(i) for i in input().split()]
            print(solution(step_list))
        except:
            break