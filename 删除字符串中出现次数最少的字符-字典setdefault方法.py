#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 16:34
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@
# @Site    : 
# @File    : 删除字符串中出现次数最少的字符.py
# @Software: PyCharm
# @Describe: 

if __name__ == '__main__':
    while True:
        try:
            mystr = input()
            if mystr:
                myls = list(mystr)
                del_i = []
                dic = {}
                for i in mystr: # 把字符串中的每个字符以及该字符的个数存到字典中
                    i_count = mystr.count(i)
                    dic[i] = dic.setdefault(i,i_count) # 如果 key不存在，则将存入key和value；如果存在则返回该key的值
                # print(dic)

                min_val = min(dic.values()) #找到个数最少的字符，并将其个数的值赋给min_val
                for k,v in dic.items(): # 遍历字典，找到所有value为min_val的key，将key存到del_列表
                    if v ==min_val:
                        del_i.append(k)

                # print(del_i)

                for i in del_i: # 遍历del_i 列表，将 myls中所有与del_i列表中元素相同的元素删除
                    for j in myls:
                        if j ==i:
                            myls.remove(j)
                            # mystr = mystr.replace(j,'')
                print(''.join(myls))
                # print(mystr)
            else:
                break
        except:
            break
