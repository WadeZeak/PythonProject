# 题目：暂停一秒输出。
#
# 程序分析：使用 time 模块的 sleep() 函数。

import time
dicts = {1: 'a', 2: 'b' , 3: 'c'}
for key,value in dicts.items():
    print(key,value)
    time.sleep(1) #暂停1s

