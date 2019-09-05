#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/5 16:36
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@
# @Site    : 
# @File    : 字符串排序.py
# @Software: PyCharm
# @Describe:
#     输入：
#
#     A Famous Saying: Much Ado About Nothing(2012/8).
#
#     输出：
#
#     A  aaAAbc   dFgghh :  iimM   nNn   oooos   Sttuuuy  (2012/8).

# https://www.runoob.com/python3/python3-func-filter.html
# https://www.runoob.com/python/python-func-filter.html
# http://dmcoders.com/2017/07/16/python-lamba/

while True:
    try:
        s=input()
        temp=list(s)
        str1=list(filter(lambda x:x.isalpha(),list(s))) # 将列表中的字母字符都过滤出来生成str1列表
        # print(str1)
        str1.sort(key=str.upper) # 按照大写字符规则排序，返回值为原来的字符
        # print(str1)
        j=0
        for i in range(len(temp)):
            if temp[i].isalpha():
                temp[i]=str1[j]
                j+=1
        print(''.join(temp))
    except:
        break