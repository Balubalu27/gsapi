import datetime
import xml.etree.ElementTree as ET

import requests


class ConvertDollarToRuble:
    def __init__(self, dollar_amount):
        self.ruble_amount = self.convert_dollar_to_ruble(dollar_amount)

    @staticmethod
    def get_dollar_exchange_rate_from_xml_response(xml_response):
        """ Парсит полученный xml файл и возвращает актуальный курс доллара по отношению к рублю """

        root = ET.fromstring(xml_response.content)
        for i_elem in root:
            if i_elem.attrib == {'ID': 'R01235'}:
                dollar_object = i_elem.find('Value')
                ruble_in_one_dollar = dollar_object.text
                dollar_exchange_rate = float(ruble_in_one_dollar.replace(',', '.'))
                return dollar_exchange_rate

    def convert_dollar_to_ruble(self, count_dollars):
        """ Конвертирует доллары в рубли по актуальнмоу курсу"""

        xml_response = XML_RESPONSE
        dollar_exchange_rate = self.get_dollar_exchange_rate_from_xml_response(xml_response)
        ruble_amount = round(count_dollars * dollar_exchange_rate, 3)
        return ruble_amount


def get_xml_response_from_bank_valutes():
    """ Функция возвращает актуальный курс валют с сайта ЦБ РФ в формате xml """

    date_now = datetime.date.today().strftime('%d/%m/%Y')
    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_now}'
    xml_response = requests.get(url)
    return xml_response


XML_RESPONSE = get_xml_response_from_bank_valutes()
