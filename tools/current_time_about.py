# -*- coding: utf-8 -*-
import time


class MyTime(object):

    def current_datetime(self):
        a = str(time.time())
        b = a.split(".")[0]
        # 时间元组 time.struct_time(tm_year=2021, tm_mon=2, tm_mday=4, tm_hour=10, tm_min=31, tm_sec=13, tm_wday=3, tm_yday=35, tm_isdst=0)
        # localtime 需整型
        c = time.localtime(int(b))
        # 格式化的时间 类型为str
        d = time.strftime("%Y-%m-%d %H:%M:%S", c)
        e = d.split(" ")[0]  # [0]取年月日 [1]是时分秒
        f = "00:00:00"
        g = "23:59:59"
        start_time = e + " " + f
        end_time = e + " " + g
        # striptime转化为时间元组 time.struct_time(tm_year=2021, tm_mon=2, tm_mday=4, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=35, tm_isdst=-1)
        return start_time, end_time

    def current_timestamp(self):
        a = str(time.time())
        b = a.split(".")[0]
        # 时间元组 time.struct_time(tm_year=2021, tm_mon=2, tm_mday=4, tm_hour=10, tm_min=31, tm_sec=13, tm_wday=3, tm_yday=35, tm_isdst=0)
        # localtime 需整型
        c = time.localtime(int(b))
        # 格式化的时间 类型为str
        d = time.strftime("%Y-%m-%d %H:%M:%S", c)
        e = d.split(" ")[0]  # [0]取年月日 [1]是时分秒
        f = "00:00:00"
        g = "23:59:59"
        start_time = e + " " + f
        end_time = e + " " + g
        # striptime转化为时间元组 time.struct_time(tm_year=2021, tm_mon=2, tm_mday=4, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=35, tm_isdst=-1)
        m = time.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        n = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        # 时间元组转换为时间戳格式为float 我们需要转成str切割 然后取[0]即小数点前面的 再转强转int
        start_snap_time = int(str(time.mktime(m)).split(".")[0])
        end_snap_time = int(str(time.mktime(n)).split(".")[0])
        return start_snap_time, end_snap_time


my_time = MyTime()  # 隐形传参self

if __name__ == '__main__':
    # print(my_time.current_timestamp())
    print(my_time.current_datetime())
