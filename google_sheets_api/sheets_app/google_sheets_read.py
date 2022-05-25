import datetime

import gspread

from google.oauth2 import service_account


def get_records_from_gsheets():
    records = worksheet.get_all_records()
    try:
        for i_row_dict in records:
            date = i_row_dict['срок поставки'].split('.')
            date_object = datetime.date(
                int(date[2]),
                int(date[1]),
                int(date[0])
            )
            i_row_dict['срок поставки'] = date_object
        return records
    except Exception as Ex:
        print('Некорректно заполнена таблица в GoogleSheets:', Ex)
        exit(1)


SERVICE_ACCOUNT_FILE = 'sheets_app/keys.json'  # Путь до файла keys.json
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

gc = gspread.authorize(creds)
sht1 = gc.open_by_key('1blj8SJGzGrHoB-5jTQ9-wgu1qIiHZjxMTlVidwT_UcI')

worksheet = sht1.worksheet('sales')
