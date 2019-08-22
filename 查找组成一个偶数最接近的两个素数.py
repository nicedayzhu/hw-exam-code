#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 19:56
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 查找组成一个偶数最接近的两个素数.py
# @Software: PyCharm
# @Describe: 


def findSushu(num):
    """
    找出所有质数
    :param num:
    :return:
    """
    sushu_ls = []
    for i in range(2,num):
        if i == 2:
            sushu_ls.append(i)
            continue
        for j in range(2,i+1):
            if j == i:
                sushu_ls.append(i)
            if i % j ==0: # 如果能在 i一下的所有数中找到一个除了1和i本身之外，能够整除i的数，则跳出
                break
    return sushu_ls

if __name__ == '__main__':
    while True:
        try:
            even_num = int(input())
            if even_num:
                sushu_ls = findSushu(even_num)
                # print(sushu_ls)
                min_cha = even_num # 初始化差值为输入的数本身
                out_1 = 0 #初始化输出默认值
                out_2 = 0
                for i in range(len(sushu_ls)-1): # 遍历所有求出的质数，找出两个相加之和等于输入值的质数(两个数可以相同)
                    for j in range(i,len(sushu_ls)):
                        if sushu_ls[i]+sushu_ls[j] ==even_num:
                            # print(sushu_ls[i],sushu_ls[j])
                            cha = sushu_ls[j] - sushu_ls[i]
                            if cha<min_cha: # 如果两个符合要求的两质数之差小于默认的差值，则将两个数分别赋给输出值
                                min_cha = cha
                                out_1 = sushu_ls[i]
                                out_2 = sushu_ls[j]
                print(out_1)
                print(out_2)
            else:
                break
        except:
            break


