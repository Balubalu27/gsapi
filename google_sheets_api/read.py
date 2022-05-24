import gspread
import datetime

from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'  # Путь до файла keys.json
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

gc = gspread.authorize(creds)
sht1 = gc.open_by_key('1blj8SJGzGrHoB-5jTQ9-wgu1qIiHZjxMTlVidwT_UcI')

worksheet = sht1.worksheet('sales')
# get_all_values gives a list of rows.
# rows = worksheet.get_all_values()
# print(rows)

def test():
    x = worksheet.get_all_records()
    for i in x:
        date = i['срок поставки']  # 24.05.2022
        i['срок поставки'] = datetime.date.today()
    return x
