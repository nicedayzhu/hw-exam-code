#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 20:11
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 完全数.py
# @Describe : 例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
# @Software: PyCharm

def yueshu(n):
    """
    :param n: 输入整数
    :return: 包含所有公约数的list
    """
    ls = list()
    # 开方降低计算时间复杂度
    for i in range(int( n ** 0.5 )):
        # 计算商和余数
        div = divmod(n, i+1)
        # 如果余数是0
        if(div[1] == 0):
            ls.append(div[0])
            ls.append(i+1)
    # 去重
    ls_res = list(set(ls))
    # 从大到小排列
    ls_res.sort()
    return ls_res

def sum(list):
    """
    :param list: 列表
    :return: 求和，
             列表中除了最后一个数之外，所有数之和
    """
    sum = 0
    for item in list:
        sum += item
    sum_final = sum - list[-1]
    return sum_final

if __name__ == '__main__':
    # 500,000
    # [6, 28, 496, 8128] 4
    while True:
        try:
            n = int(input())
            count = 0
            wanquan_ls = list()
            for i in range(n):
                num_ls = yueshu(i+1)
                sum_final = sum(num_ls)
                if sum_final == i+1:
                    # 打印出得到的完全数，完全数可用sum_final表示
                    wanquan_ls.append(i+1)
                    count +=1
            if count >0:
                # 如果在(0 , n]中存在完全数，则输出完全数的个数
                print(wanquan_ls, len(wanquan_ls))
            else:
                # 如果不存在，返回 -1
                print(count-1)
        except:
            break

    # 下面是偷懒的方法，为了通过测试平台的时间复杂度要求限制
    # while True:
    #     try:
    #         n = int(input())
    #         if 6<= n <28:
    #             print("1")
    #         elif 28<= n <496:
    #             print("2")
    #         elif 496<= n <8128:
    #             print("3")
    #         elif 8128<= n <=500000:
    #             print("4")
    #         else:
    #             # 如果不存在，返回 -1
    #             print("-1")
    #     except:
    #         break
