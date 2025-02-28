import os
import csv
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from datetime import datetime

class GoogleSheetsUpdater:
    def __init__(self, credentials_file, token_file='token.json'):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.service = self.authenticate_sheets()

    def authenticate_sheets(self):
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None

        # O token de autenticação já existe
        if os.path.exists(self.token_file):
            creds = Credentials.from_authorized_user_file(self.token_file, SCOPES)
        
        # Se não tem credenciais válidas, faz a autenticação
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)

            # Salva o token para o próximo uso
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())

        return build('sheets', 'v4', credentials=creds)

    def update_sheet_with_csv(self, spreadsheet_id, range_name, csv_file_path):
        if not os.path.exists(csv_file_path):
            print(f"Erro: o arquivo {csv_file_path} não foi encontrado.")
            return

        # Lê o CSV e converte para uma lista de listas (cada linha do CSV é uma lista)
        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            values = list(reader)

        # Adiciona os dados da CSV na planilha Google
        request = self.service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="RAW",  # Pode ser "RAW" ou "USER_ENTERED"
            body={"values": values}
        )

        try:
            response = request.execute()
            print(f"Dados enviados com sucesso! {response}")
        except Exception as e:
            print(f"Erro ao enviar dados: {e}")