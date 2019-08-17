#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 17:42
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : printf用法.py
# @Software: PyCharm
# @Describe: 

print(*objects, sep=' ', end='\n', file=sys.stdout)
参数
objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
sep -- 用来间隔多个对象，默认值是一个空格。
end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
file -- 要写入的文件对象。