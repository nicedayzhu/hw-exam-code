#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 18:02
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 字符串分割.py
# @Software: PyCharm
# @Describe: •连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
# •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
if __name__ == '__main__':
    ls_str = []
    str1 = input()
    ls_str.append(str1)
    str2 = input()
    ls_str.append(str2)
    # print(ls_str)
    for i in range(len(ls_str)):
        if len(ls_str[i])<8: # 如果元素的字符串个数小于8，那么直接追加0后输出
            ls_str[i] +='0'*(8-len(ls_str[i]))
            print(ls_str[i])
        else:
            group = 0
            if len(ls_str[i]) % 8 ==0:
                group = len(ls_str[i]) // 8
            if len(ls_str[i]) % 8 !=0:
                group = len(ls_str[i]) // 8 + 1 # 字符串8个一组，共 group +1 组
            for g in range(group):
                group_ls = ls_str[i][0+8*g:8*(g+1)] # 每一组按元素个数是否小于8进行追加 0 ，然后输出
                len_group_ls = len(group_ls)
                if len_group_ls <8:
                    add0_str = group_ls + '0'*(8-len(group_ls))
                    print(add0_str)
                else:
                    print(group_ls)
                # s1 = ls_str[i][8*group:len(ls_str[i])] # 如果元素字符长度大于8，将大于的部分取出
                # split_ls =s1 + '0'*(8-len(s1)) # 取出的部分再添加0，直至该部分字符长度达到8
                # ls_str[i] = ls_str[i][:8] # 将列表中的后一个元素缩减到8个字符
                # ls_str.append(split_ls) # 将分割出的新字符串追加到列表
                # print(split_ls,len(split_ls))
