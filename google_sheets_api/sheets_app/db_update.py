import requests
import schedule
import time


def get_request():
    """ Функция запускается из schedule, каждые 5 секунд выполняет гет запрос """

    resp = True
    try:
        response = requests.get('http://127.0.0.1:8000')
        if not resp:
            print('++Соединение восстановлено++')
        resp = True
    except Exception as ex:
        print('**Сервер недоступен:**', ex)
        resp = False


schedule.every(5).seconds.do(get_request)

while True:
    schedule.run_pending()
    time.sleep(1)
