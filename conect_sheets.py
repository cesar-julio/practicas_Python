"""
Librerias

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
"""


from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
KEY = "key.json"

SPREADSHEET_ID = "1WLrMsZ1Z86muodKdBA8c1I2ayzZHP9u1ymy0MJx53tY"

creds = None

creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build("sheets", "v4", credentials=creds)
sheet = service.spreadsheets()

#Llamar a la API
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range="Hoja 1!C4:C15").execute()

values = result.get("values", [])
print(values)

#Escribir datos
add_values = [["Colores"]]
add_result = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range="A1", valueInputOption="USER_ENTERED", 
                                   body={"values":add_values}).execute()
print("Los datos enviados fueron inserdados correctamente")
