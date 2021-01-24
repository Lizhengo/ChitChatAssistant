# -*- coding: utf-8 -*-

import time
import random

a1=(2021,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（2021-01-01 00：00：00）
a2=(2022,12,31,23,59,59,0,0,0)    #设置结束日期时间元组（2022-12-31 23：59：59）

start=time.mktime(a1)    #生成开始时间戳
end=time.mktime(a2)      #生成结束时间戳

# date_format_type
# 1：6月9号(日)
# 2: 6.9
# 3: 6-9
# 4：2020年6月9号(日)
# 5: 2020.6.9
# 6: 2020-6-9

date_format_type = 6
is_slot = True

#随机生成10个日期字符串
for i in range(100):
    t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    year = str(date_touple.tm_year)
    mon = str(date_touple.tm_mon)
    day = str(date_touple.tm_mday)
    
    if date_format_type == 1:
        if random.random() < 0.5:
            date = mon + "月" + day + "日"
        else:
            date = mon + "月" + day + "号"
    elif date_format_type == 2:
        date = mon + "." + day
    elif date_format_type == 3:
        date = mon + "-" + day
    elif date_format_type == 4:
        if random.random() < 0.5:
            date = year + "年" + mon + "月" + day + "日"
        else:
            date = year + "年" + mon + "月" + day + "号"
    elif date_format_type == 5:
        date = year + "." + mon + "." + day
    elif date_format_type == 6:
        date = year + "-" +mon + "-" + day
    else:
        print("error date format type")
        break
        
    if is_slot:
        print("    ~[" + date + "]")
    else:
        print("    " + date)

    