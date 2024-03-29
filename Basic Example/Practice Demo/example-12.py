# 题目：判断101-200之间有多少个素数，并输出所有素数。
#
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　

from math import sqrt
from sys import stdout
leap = 1 ##素数的标记
h = 0 #素数的个数
for i in range(101,201):
    k = int(sqrt(i)) +1
    for j in  range(2,k): #判断是否是素数
        if i%j == 0:
            leap = 0
            break
    if leap :
        h += 1
        print('%-4d' %i)
    if h % 10 == 0: ##每10个数字 输出空白行
        print('')
    leap = 1

print('The total is %d' %h)
