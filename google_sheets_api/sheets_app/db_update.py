import requests
import schedule
import time


def get_request():
    try:
        response = requests.get('http://127.0.0.1:8000')
    except Exception as ex:
        print('Сервер недоступен:', ex)


schedule.every(5).seconds.do(get_request)

while True:
    schedule.run_pending()
    time.sleep(1)
