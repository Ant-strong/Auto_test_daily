# 存放URL/密码/json文件
import json
import os


class NameWord(object):

    username = 'xx'
    password = 'xxx'


class ApiUrl(object):

    login_url = 'http://192.168.42.245/tool/api/login'  # 登录API
    day_total_energy_url = 'http://192.168.42.245/tool/api/site/component/energy/statistics/total'  # 今日总计用能API
    energy_analysis_url = 'http://192.168.42.245/tool/api/site/energy/networkGraph/data/time/analysis'  # 分时/日/年能耗分析URL


class JsonFile(object):

    json_base_path = os.getcwd() + os.sep + "JsonFile" + os.sep

    # 登录post请求发送的数据
    login_data = {
        'username': NameWord.username,
        'password': NameWord.password
    }
    json_login = json.dumps(login_data)

    # 获取今日总计用能post请求发送的数据
    with open(json_base_path + 'day_total_energy_data.json', "r") as file:
        day_total_energy_data = json.load(file)
    json_day_total_energy = json.dumps(day_total_energy_data)

    # 获取分时模式下能耗
    with open(json_base_path + 'times_pattern_analysis.json', 'r') as file1:
        times_pattern_analysis_data = json.load(file1)
    json_times_pattern_analysis = json.dumps(times_pattern_analysis_data)

    # 获取日模式下能耗
    with open(json_base_path + 'daily_pattern_analysis.json', 'r') as file2:
        daily_pattern_analysis_data = json.load(file2)
    json_daily_pattern_analysis = json.dumps(daily_pattern_analysis_data)

    # 获取月模式下能耗
    with open(json_base_path + 'month_pattern_analysis.json', 'r') as file3:
        month_pattern_analysis_data = json.load(file3)
    json_month_pattern_analysis = json.dumps(month_pattern_analysis_data)
