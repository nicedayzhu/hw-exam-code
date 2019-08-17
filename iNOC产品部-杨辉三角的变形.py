#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 20:19
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : iNOC产品部-杨辉三角的变形.py
# @Software: PyCharm
# @Describe: 

# 生成杨辉三角形
# 第 n 行有 2*n-1 个数
def createMatrix(n):
    matrix = [[0 for j in range(2 * n - 1)] for i in range(n)]
    matrix[0][n - 1] = 1
    for i in range(1, n):
        for j in range(1, 2 * n - 2):
            # 本行的第 j 个元素，是上一行的第 j-1 ,j ,j+1 个元素的和，j从 1 开始
            matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i - 1][j + 1]
    matrix[n - 1][0] = 1
    matrix[n - 1][2 * n - 2] = 1
    return  matrix

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            if n:
                yanghuiMatrix = createMatrix(n)
                # print(yanghuiMatrix)
                for k in range(n): # 第 n 行只需要比到第 n-1 个数即可，因为后面的数就是回文数
                    if yanghuiMatrix[n-1][k] % 2 == 0:
                        print(k+1)
                        break
                    else:
                        if k == n-1:
                            print(-1)
            else:
                break
        except:
            break