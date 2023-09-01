#  执行巡检主程序

import requests
from Data import *  # 导入Data中的方法
import datetime
import os

headers = {'Content-Type': 'application/json;charset=UTF-8'}
response = requests.post(ApiUrl.login_url, data=JsonFile.json_login, headers=headers)
token_data = 'Bearer ' + response.json()['token']
report_path = os.getcwd() + os.sep + 'report' + os.sep + '{}巡检报告.txt'.format(datetime.date.today())


class KunShangProject(object):

    @staticmethod
    def daily_check_get_data(way):

        headers_check = {'Content-Type': 'application/json;charset=UTF-8', 'Authorization': token_data}

        # 获取今日总计用能
        if way == 1:
            response_check = requests.post(ApiUrl.day_total_energy_url,
                                           data=JsonFile.json_day_total_energy, headers=headers_check)
            x = response_check.json()
            return x['data']['total']

        # daily_energy_total = '今日总计用能：' + str(x['data']['total']) + x['data']['dimension']

        # 获取分时模式下各时段值
        if way == 2:
            times_response = requests.post(ApiUrl.energy_analysis_url,
                                           data=JsonFile.json_times_pattern_analysis, headers=headers_check)
            times_analysis = times_response.json()
            return times_analysis['data']['analysisList'][0]

    @staticmethod
    def daily_check_data_analysis():

        # 今日总能耗分析
        daily_energy_total = KunShangProject.daily_check_get_data(1)
        if daily_energy_total == 0.0:
            result = '今日总能耗异常 \n' \
                     '总能耗为：{} kw'.format(daily_energy_total)
            return result
        else:
            result1 = '今日总能耗正常 \n' \
                     '总能耗为：{} kw'.format(daily_energy_total)
            return result1

    @staticmethod
    def times_energy_analysis():

        # 分时能耗分析
        times_energy_total = KunShangProject.daily_check_get_data(2)
        curtimes = times_energy_total['curTimes']
        current_time = datetime.datetime.now().hour + 1
        print(curtimes)
        print(len(curtimes))
        print(current_time)

        if len(curtimes) == current_time:
            print('44444444444444444444')
            result = '分时能耗异常 \n' \
                     '当前存在分时能耗数：{} \n'.format(len(curtimes))
            return result
        elif len(curtimes) == 0:
            print('111111111111111111')
            result3 = 0
            return result3
        else:
            print('33333333333333')
            result1 = []
            pass_count = 0
            for i in range(len(curtimes)):
                metering_value = curtimes[i]['meteringValue']
                if metering_value == 0:
                    j = {'{}'.format(i + 1): metering_value}
                    result1.append(j)
                else:
                    pass_count += 1
            if pass_count == len(curtimes):
                result2 = '分时能耗正常'
                return result2
            else:
                return result1

    @staticmethod
    def edit_report():

        report_context = '分时能耗异常： \n' \
                         '第{}小时异常，异常值为{}kw'
        report_context1 = '分时能耗正常，和小时详细能耗如下： \n' \
                          '第{}小时正常，正常值为{}kw'

        print("times_energy_analysis() type:", type(KunShangProject.times_energy_analysis()))

        if isinstance(KunShangProject.times_energy_analysis(), list):
            print("Entering the list branch")  # 添加调试输出

            for i in range(len(KunShangProject.times_energy_analysis())):
                for key, value in KunShangProject.times_energy_analysis()[i].items():
                    report_context = report_context.format(key, value)
                    return report_context

        elif isinstance(KunShangProject.times_energy_analysis(), str):
            print("Entering the string branch")  # 添加调试输出
            times_energy_total = KunShangProject.daily_check_get_data(2)
            curtimes = times_energy_total['curTimes']

            for i in range(len(curtimes)):
                for key, value in curtimes[i].items():
                    report_context1 = report_context1.format(key, value)
                    return report_context1
        elif isinstance(KunShangProject.times_energy_analysis(), int):
            print('000000000000000000000000000')
            report_context2 = '分时能耗异常： \n' \
                              '所有分时能耗都为0'
            return report_context2

    @staticmethod
    def putout_report():
        with open(report_path, 'w') as my_report:
            my_report.write('{} \n'.format(KunShangProject.daily_check_data_analysis()))
            my_report.write(KunShangProject.edit_report())


if __name__ == "__main__":
    KunShangProject.putout_report()
