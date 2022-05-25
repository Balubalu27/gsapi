import requests
import schedule
import time


def get_request():
    response = requests.get('http://127.0.0.1:8000')


schedule.every(5).seconds.do(get_request)

while True:
    schedule.run_pending()
    time.sleep(1)
