# l=[['v1',1.23],['v2',1.60],['v3',1.60],['o1',1.90],['o2',1.14],['a1',1.21],['a2',1.72]]
# # for i in range(0,len(l)):
# #
# # for i in range(0,len(l)):
# #     for j in range(i,len(l)):
# #         if l[i][1]<l[j][1]:
# #             t=l[i]
# #             l[i]=l[j]
# #             l[j]=t
# # print(l)
#
# a=sorted(l,key=lambda x:x[1], reverse=True)
# print(a)
import pandas as pd
import os
import numpy
# df = pd.read_csv('violation.txt')
# f = open("violation.txt")
# d = open("violations.txt", "w")
# d.write("Hello Rishit ")
# d.close()
# d = open("violations.txt")
# # print(f.read())
# print(d.read())
os.remove("os_examples.py")