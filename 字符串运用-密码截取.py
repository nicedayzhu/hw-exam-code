#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 19:48
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : 字符串运用-密码截取.py
# @Software: PyCharm
# @Describe:

# 48-57(0-9), 97-122(a-z),65-90(A-Z)
def check(str):
    str_len = len(str)
    if str_len == 1:
        return str
    else:
        flag = False
        for loop in range(str_len // 2):
            if(str[loop] == str[str_len-1-loop]):
                flag = True
            else:
                flag = False
                # 只要检测到头尾不相等，就跳出，意味着该字符串不是回文
                break
        if flag:
            return str
        else:
            pass


def cutstr(ls):
    """
    分割字符串
    :param ls:
    :return:
    """
    cut_lst = []
    cut_str_len =[]
    for i in range(len(ls)): # 从第 i 个作为首位开始
        t = i+1 # 下一个元素的索引
        for loop in range(len(ls) -i): # 轮询次数
            # print(ls[i:t]) # 打印第 i 到 t 之间的元素组成的str
            cut_lst.append(ls[i:t])
            len_cutstr = len(ls[i:t])
            cut_str_len.append(len_cutstr)
            # print("长度为 ",len_cutstr)
            if(t<=len(ls)):
                t+=1
            else:
                pass
    # print(cut_lst)
    # print(cut_str_len)
    return cut_lst





if __name__ == '__main__':
    while True:
        try:
            ls = input()
            if ls: # 如果为空，则跳出程序break
                tar_len = []
                cut_lst = cutstr(ls)
                for item in cut_lst:
                    str = check(item)
                    if str:
                        # print(str, "是回文", "长度为", len(str))
                        tar_len.append(len(str))
                    else:
                        pass
                tar_len = list(set(tar_len))
                # print(tar_len)
                print(tar_len[-1])
            else:
                break
        except:
            break