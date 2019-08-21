#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 20:56
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 质数因子-分解质因数.py
# @Software: PyCharm
# @Describe: https://www.nowcoder.com/questionTerminal/196534628ca6490ebce2e336b47b3607
# 华科平凡


if __name__ == '__main__':
    a, res = int(input()), []
    for i in range(2, a // 2 + 1):
        while a % i == 0:
            a = a / i
            res.append(i)
    # print(" ".join(map(str, res)) + " " if res else str(a) + " ")
    if res:
        print(" ".join(map(str, res)) + " " )
    else:
        print(str(a) + " ")
    # 作者：华科平凡
    # 链接：https: // www.nowcoder.com / questionTerminal / 196534628
    # ca6490ebce2e336b47b3607
    # 来源：牛客网
    #
    # print(" ".join(map(str, res)) + " " if res else str(a) + " ")
    # 1.
    # 如果res不为空，输出
    # " ".join(map(str, res)) + " "。 2.
    # 如果res为空，则输出
    # str(a) + " "。3.
    # 这种语法是将if
    # else语句写成一行，也可以单独拆开写