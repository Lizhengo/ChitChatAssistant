# -*- coding: utf-8 -*-

import time
import datetime
 
def time_finder(str_date):
    '''判断是否是一个有效的日期字符串并返回统一格式'''
    year_month_day_pattern_list = ["%Y-%m-%d",
                                   "%Y年%m月%d日",
                                   "%Y年%m月%d号",
                                   "%Y.%m.%d"]
    month_day_pattern_list = ["%m-%d",
                              "%m月%d日",
                              "%m月%d号",
                              "%m.%d"]
    
    ymd_date, md_date = None, None
    
    for year_month_day_pattern in year_month_day_pattern_list:
        try:
            ymd_date = time.strptime(str_date, year_month_day_pattern)
        except:
            continue
    if ymd_date is not None:
        return str(ymd_date.tm_year) + "-" + str(ymd_date.tm_mon) + "-" + str(ymd_date.tm_mday)
    
    for month_day_pattern in month_day_pattern_list:
        try:
            md_date = time.strptime(str_date, month_day_pattern)
        except:
            continue
    if md_date is not None:
        return str(datetime.datetime.now().year) + "-" + str(md_date.tm_mon) + "-" + str(md_date.tm_mday)
    
    return None
 
 
if __name__ == "__main__":
    date = '2022.10.31'
    match_date = time_finder(date)
    print(match_date)
    