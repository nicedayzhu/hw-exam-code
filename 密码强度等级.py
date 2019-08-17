#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 10:07
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 密码强度等级.py
# @Software: PyCharm
# @Describe: 

def calPwdLen(ls):
    lenPwd = len(ls)
    point_len = 0
    if lenPwd<=4:
        point_len = 5
    elif lenPwd<=7:
        point_len = 10
    else:
        point_len = 25
    return point_len

def calAlpha(ls):
    """判断是否拥有字母，判断大小写，并且得出得分"""
    point_alpha_lw = 0  # 默认小写得分
    point_alpha_up = 0  # 默认大写得分

    for item in ls:
        if (ord(item)>64) and (ord(item)<91):
            point_alpha_lw  = 10
        elif (ord(item)>96) and (ord(item)<123):
            point_alpha_up = 10

    return point_alpha_lw + point_alpha_up # 返回大小写总分

def calNum(ls):
    num_count_flag = 0 # 默认当前数字个数为0
    point_num = 0
    for item in ls:
        if not num_count_flag:
            if (ord(item)>47) and (ord(item)<58):
                point_num = 10
                num_count_flag = 1 # 当前已存在一个数字
        else:
            # 判断数字个数是否大于1个，如果是，得分为20
            if (ord(item)>47) and (ord(item)<58):
                point_num = 20
    return point_num

def calSymbol(ls):
    symbol_count_flag = 0
    point_symbol = 0
    for item in ls:
        if not symbol_count_flag:
            if ((ord(item)>32) and (ord(item)<48) or
                (ord(item) > 57) and (ord(item) < 97) or
                (ord(item) > 122)):
                point_symbol = 10
                symbol_count_flag = 1 # 当前已存在一个符号
        else:
            # 判断数字个数是否大于1个，如果是，得分为20
            if ((ord(item)>32) and (ord(item)<48) or
                (ord(item) > 57) and (ord(item) < 97) or
                (ord(item) > 122)):
                point_symbol = 25
    return point_symbol

def getPoints(ls):
    """获取总得分"""
    point_len = calPwdLen(pwdls)
    point_alpha = calAlpha(pwdls)
    point_num = calNum(pwdls)
    point_symbol = calSymbol(pwdls)
    point_bonus = 0 # 附加分
    if (point_num == 10) and point_alpha:
        # 2 分: 字母和数字
        point_bonus = 2
    if (point_num == 10) and point_alpha and point_symbol:
        # 3 分: 字母、数字和符号
        point_bonus = 3
    if (point_num == 20) and point_alpha and point_symbol:
        # 5 分: 大小写字母、数字和符号
        point_bonus = 5
    points = point_len + point_alpha+ point_num +point_symbol + point_bonus
    return points

def printLevel(points):
    if 0<=points<25:
        print("VERY_WEAK")
    elif points<50:
        print("WEAK")
    elif points<60:
        print("Average")
    elif points<70:
        print("Strong")
    elif points<80:
        print("VERY_STRONG")
    elif points<90:
        print("SECURE")
    else:
        print("VERY_SECURE")

if __name__ == '__main__':
    while True:
        try:
            pwdls = list(input())
            # print(calPwdLen(pwdls))
            if pwdls:
                points = getPoints(pwdls)
                printLevel(points)
            else:
                break
        except:
            break
