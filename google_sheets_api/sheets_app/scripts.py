import requests
import datetime
import xml.etree.ElementTree as ET


def get_xml_from_bank_valutes():
    """ Функция возвращает актуальный курс валют с сайта ЦБ РФ в формате xml """

    date_now = datetime.date.today().strftime('%d/%m/%Y')
    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_now}'
    response = requests.get(url)
    return response


def get_dollar_exchange_rate_from_xml(xml_response):
    """ Парсит полученный xml файл и возвращает актуальный курс доллара по отношению к рублю """

    root = ET.fromstring(xml_response.content)
    for i_elem in root:
        if i_elem.attrib == {'ID': 'R01235'}:
            dollar_object = i_elem.find('Value')
            ruble_in_one_dollar = dollar_object.text
            convert_to_float = float(ruble_in_one_dollar.replace(',', '.'))
            return convert_to_float


def convert_dollar_to_ruble(dollar_amount):
    """ Конвертирует доллары в рубли по актуальнмоу курсу"""

    xml_result = get_xml_from_bank_valutes()
    one_dollar_price_in_ruble = get_dollar_exchange_rate_from_xml(xml_result)
    ruble_amount = dollar_amount * one_dollar_price_in_ruble
    return ruble_amount


print(convert_dollar_to_ruble(200))


