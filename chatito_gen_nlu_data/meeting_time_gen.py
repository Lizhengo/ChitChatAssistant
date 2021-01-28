# -*- coding: utf-8 -*-

import time
import random
from random import choice

a1=(2021,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（2021-01-01 00：00：00）
a2=(2022,12,31,23,59,59,0,0,0)    #设置结束日期时间元组（2022-12-31 23：59：59）

start=time.mktime(a1)    #生成开始时间戳
end=time.mktime(a2)      #生成结束时间戳

# date_format_type
# 1：(今天/明天/后天/星期x/x月x号/x月x日)（早上/下午/None）x点(半)（到/-）x点（半）
# 2:  (今天/明天/后天/星期x/x月x号/x月x日)（早上/下午/None）x点（半）
# 3:  (今天/明天/后天/星期x/x月x号/x月x日)（早上/下午/None）

is_slot = True

date_list = ["今天", "明天", "后天", "星期"]
week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
time_list = ["早上", "下午", ""]
time_conj = ["到", "-"]
type_list = [1,2,3]

def random_date():
    if random.random() < 0.5:
        t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t)          #将时间戳生成时间元组
        year = str(date_touple.tm_year)
        mon = str(date_touple.tm_mon)
        day = str(date_touple.tm_mday)
        if random.random() < 0.5:
            date = mon + "月" + day + "日"
        else:
            date = mon + "月" + day + "号"
    else:
        date = choice(date_list)
        if date == "星期":
            date = choice(week_list)
    return date

def random_time():
    t = []
    while(len(t) < 2):
        x = random.randint(8, 21)
        if x not in t:
            t.append(x)
    t = sorted(t)
    
    start_time = str(t[0])
    end_time = str(t[1])
    
    if random.random() < 0.5:
        start_time = start_time + choice(["点","点半"])
        end_time = end_time + choice(["点","点半"])
    else:
        start_time = start_time + choice([":00",":30", "：00","：30"])
        end_time = end_time + choice([":00",":30", "：00","：30"])
    return start_time, end_time


#随机生成日期字符串
for i in range(1000):
    date = random_date()
    start_time, end_time = random_time()
    date_format_type = choice(type_list)

    if date_format_type == 1:
       schedule_date = date + choice(time_list) + start_time + choice(time_conj) + end_time
    elif date_format_type == 2:
        schedule_date = date + choice(time_list) + start_time
    elif date_format_type == 3:
         schedule_date = date + choice(time_list)
    else:
        print("error date format type")
        break
        
    if is_slot:
        print("    ~[" + schedule_date + "]")
    else:
        print("    " + schedule_date)

    