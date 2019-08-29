#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 13:32
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 字符串加密.py
# @Software: PyCharm
# @Describe:

if __name__ == '__main__':
    while True:
        try:
            alpha_ls = []
            encry_ls = []
            out_ls = []
            str_ls = list(input())
            code = input().split(" ")
            # print(code) # 输出输入字符串
            if str_ls:
                set_ls = list(set(str_ls))
                set_ls.sort(key=str_ls.index)
                for item in set_ls:
                    encry_ls.append(item.upper()) # 将密钥去重，添加到encry_ls中
                # print(encry_ls) # 输出加密表

                for i in range(65,91):
                    alpha_ls.append(chr(i)) # 生成大小26个字母表
                    if chr(i) in encry_ls: # 将不包含在密钥中的26个字母中的其他字母按顺序加入到encry_ls
                        pass
                    else:
                        encry_ls.append(chr(i))
                # print(alpha_ls) # 输出大小26字母表

                for item in code:  # 遍历输入字符串中每一个单词
                    new_str = ""
                    for i in range(len(item)): # 遍历每一个单词中的每个字符是否能在大写26个字母表中找到
                        if item[i].upper() in alpha_ls: # 如果单词中的字符能在26个字母表中找到，那么输出加密表中对应位置的字符
                            # print(alpha_ls.index(item[i].upper()))
                            if ord(item[i])>90: # 如果输入的单词中的字符是小写字符，那么对应输入加密表中字符的小写形式
                                new_str += encry_ls[alpha_ls.index(item[i].upper())].lower()
                            else:
                                new_str += encry_ls[alpha_ls.index(item[i].upper())]

                    out_ls.append(new_str)

                print(" ".join(out_ls))
            else:
                break
        except:
            break


