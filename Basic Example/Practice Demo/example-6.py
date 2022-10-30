# 题目：斐波那契数列。
#
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
#
# 在数学上，费波那契数列是以递归的方法来定义：
#
# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)

count = int(input("请输入斐波那契数列长度:"))
def FibonacciSeq(count):
    x,y = 0,1
    for i in range(2, count):
       x,y = y,x+y
    return y
print("第",count,"个斐波那契数列是: ", FibonacciSeq(count))