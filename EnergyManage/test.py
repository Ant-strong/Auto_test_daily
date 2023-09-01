import schedule
import time
import os
import datetime


file_path = r'D:\Auto_test_daily\EnergyManage\report\test_file.txt'


def abc():
    with open(file_path, 'w') as file:
        file.write('hallo, test pass' + str(datetime.datetime.now()))


schedule.every(1).minutes.do(abc)

while True:
    schedule.run_pending()
    time.sleep(1)
