#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 21:30
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : Python创建二维数组.py
# @Software: PyCharm
# @Describe: 

# 列表生成式法
m = 2
n = 3
# 创建三行两列的数组，初始值为0
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017317609699776
test = [[0 for i in range(m)] for j in range(n)]
print(test)