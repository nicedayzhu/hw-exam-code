#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 16:45
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 明明的随机数.py
# @Software: PyCharm
# @Describe: 
if __name__ == '__main__':
    while True:
        try:
            count = int(input()) # 记录下要输入的整数的个数
            ls_num = []
            while count:
                num = int(input())
                ls_num.append(num)
                count -=1
            res_ls = list(set(ls_num)) #去重后的列表
            res_ls.sort() # 排序
            ls_num.clear()
            for i in range(len(res_ls)): # 输出去重后列表的元素
                print(res_ls[i])
            res_ls.clear()
        except:
            break