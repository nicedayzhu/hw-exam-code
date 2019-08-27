#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 18:47
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 矩阵乘法.py
# @Software: PyCharm
# @Describe: 

def iniialMatrix(hang,lie):
    matrix = [[0 for x in range(lie)] for y in range(hang)]
    return matrix

def martixMulti(hang1,lie_hang,lie2):
    result = iniialMatrix(hang1, lie2)
    for p in range(lie2):
        for i in range(hang1):
            for j in range(lie_hang):
                result[i][p] += matrix1[i][j]*matrix2[j][p]
    return  result

if __name__ == '__main__':
    while True:
        try:
            hang1 = int(input()) # 第一个矩阵的行
            lie_hang = int(input()) # 第一个矩阵的列，第二个矩阵的行
            lie2 = int(input()) # 第二个矩阵的列

            matrix1 = iniialMatrix(hang1,lie_hang)
            matrix2 = iniialMatrix(lie_hang,lie2)


            for i in range(hang1):
                matrix1[i] = [int(x) for x in input().split()]
                # for j in range(lie_hang):
                #     matrix1[i][j] = int(matrix1[i][j]) # 讲输入的字符转为整型数字
                #                                        # [int(x) for x in input().split()]
            for i in range(lie_hang):
                matrix2[i] = [int(x) for x in input().split()]
                # for j in range(lie2):
                #     matrix2[i][j] = int(matrix2[i][j]) # 讲输入的字符转为整型数字

            result = martixMulti(hang1,lie_hang,lie2)

            for i in range(hang1):
                for j in range(lie2):
                    result[i][j] = str(result[i][j])
            for i in range(hang1):
                print(" ".join(result[i]))
        except:
            break



