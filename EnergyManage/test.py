import datetime

# 获取当前日期和时间
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

# 创建指定日期时间对象
custom_datetime = datetime.datetime(2023, 8, 21, 12, 30, 0)
print("Custom Date and Time:", custom_datetime)

# 解析日期时间字符串
date_string = "2023-08-21 15:45:00"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Date and Time:", parsed_datetime)

# 获取当前日期
current_date = datetime.date.today()
print("Current Date:", current_date)

# 创建指定日期对象
custom_date = datetime.date(2023, 8, 21)
print("Custom Date:", custom_date)

# 创建指定时间对象
custom_time = datetime.time(15, 45, 0)
print("Custom Time:", custom_time)

# 时间戳和时间间隔
timestamp = current_datetime.timestamp()

print("Timestamp:", timestamp)

time_delta = datetime.timedelta(days=5, hours=3)
print("Time Delta:", time_delta)

result = '今日总能耗异常 \n' \
         '总能耗为：{} kw'
print(result)
