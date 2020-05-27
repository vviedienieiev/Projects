import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import time

CONFIG = {"KEY_FILE_LOCATION":'FILE PATH',
          "SERVICE_ACCOUNT_EMAIL": 'bot.email@gmail.com'}


def main():
    df = [[1,2],[3,4]]
    Sheets_actions = {
            'Action_1': {'spreadsheetId': '129NJOwlFKdworLrO6dxvzVJeKq74G6BFLzl8qrChceQ',
                         'range1': "Sheet1!A1:B2",
                         'data': df},
            # 'Action_2': {'spreadsheetId': 'GS_id_2',
            #                'range1': "Sheet1!A1:B2",
            #                'data': df},
        }

    sheets = google_sheets()

    for action in Sheets_actions:
        sheets.clear_range(Sheets_actions[action]["spreadsheetId"],
                           Sheets_actions[action]["range1"])
        sheets.insert_values(Sheets_actions[action]["spreadsheetId"],
                             Sheets_actions[action]["range1"],
                             df)


class google_sheets:
    def __init__(self):
        self.sheets = build('sheets',
                            'v4',
                            http=ServiceAccountCredentials.from_p12_keyfile(
                                CONFIG["SERVICE_ACCOUNT_EMAIL"],
                                CONFIG["KEY_FILE_LOCATION"],
                                scopes=['https://www.googleapis.com/auth/spreadsheets']).authorize(httplib2.Http()),
                            discoveryServiceUrl='https://sheets.googleapis.com/$discovery/rest?version=v4')

    def clear_range(self, file_id, range):
        try:
            result = self.sheets.spreadsheets().values().clear(spreadsheetId=file_id,
                                                      range=range).execute()
        except Exception as e:
            print(e)

    def insert_values(self, file_id, range, values):
        try:
            result = self.sheets.spreadsheets().values().update(spreadsheetId=file_id,
                                                           range=range,
                                                           valueInputOption='USER_ENTERED',
                                                           body={'values': values}).execute()
        except Exception as e:
            print(e)
