# 题目：输入某年某月某日，判断这一天是这一年的第几天？
#
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
#

year = int(input("请输入年份:"))
month = int(input("请输入月份:"))
day = int(input("请输入日期:"))

#非闰年
months = (0,31,59,90,120,151,181,212,243,273,304,334)

if 0 < month <= 12 :
    sum = months[month - 1]
else:
    print("date format err")

sum += day

##闰年 大于2月的天数 +1
if (year % 4 == 0) and month > 2 :
    sum += 1


print ('it is the %dth day.' % sum)





