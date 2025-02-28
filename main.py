from data_loader import DataLoader
from data_cleaner import DataCleaner
from database import Database
from gsudater import GoogleSheetsUpdater

#1️ Extrair dados
dataset_name = "karthikbhandary2/boat-sales"
loader = DataLoader(dataset_name)
csv_path = loader.download_dataset()

#2️ Limpar dados
cleaner = DataCleaner(csv_path)
df_cleaned = cleaner.clean_data()

#3️ Carregar dados
db = Database()
db.create_table()
db.insert_data(df_cleaned)
db.export_to_csv("boat_sales.csv")
db.close_connection()

#4️ Enviar dados para o Google 
credentials_file = 'credentials.json'
spreadsheet_id = '1r88W57Xp0QKSridTViy2QNU_-jG-XPNnZ9pHT1XTyWY'
range_name = 'boat!A1' 
csv_file_path = "boat_sales.csv"
updater = GoogleSheetsUpdater(credentials_file)
updater.update_sheet_with_csv(spreadsheet_id, range_name, csv_file_path)

print("Pipeline concluído com sucesso!")
