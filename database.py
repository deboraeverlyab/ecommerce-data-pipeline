import sqlite3
import pandas as pd
import numpy as np

class Database:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)  
        self.cursor = self.conn.cursor()

    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS boat_sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            price REAL,
            boat_type TEXT,
            manufacturer TEXT,
            type TEXT,
            year_built INTEGER,
            length REAL,
            width REAL,
            material TEXT,
            views_last_7_days INTEGER,
            eur_price REAL,
            currency TEXT,  -- Nova coluna para Currency
            country TEXT,
            city TEXT
        )
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()
        print("Tabela criada com sucesso!")

    def insert_data(self, df):
        insert_query = """
        INSERT INTO boat_sales (price, boat_type, manufacturer, type, year_built, length, width, material, views_last_7_days, eur_price, currency, country, city)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        df = df.replace({np.nan: None})
        data_tuples = [
            (
                row["Price"],  
                row.get("Boat Type", None),  
                row.get("Manufacturer", None),
                row.get("Type", None),
                row.get("Year Built", None),
                row.get("Length", None),
                row.get("Width", None),
                row.get("Material", None),
                row.get("Number of views last 7 days", None),  
                row["EUR_price"],  
                row.get("Currency", None),  
                row.get("Country", None),
                row.get("City", None),
            )
            for _, row in df.iterrows()
        ]
        self.cursor.executemany(insert_query, data_tuples)
        self.conn.commit()
        print(f"{self.cursor.rowcount} registros inseridos no SQLite!")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    def export_to_csv(self, file_path="boat_sales.csv"):
        df = pd.read_sql_query("SELECT * FROM boat_sales", self.conn)
        df.to_csv(file_path, index=False)
        print(f"Dados exportados para {file_path}")
