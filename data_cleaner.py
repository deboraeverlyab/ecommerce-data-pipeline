import pandas as pd

class DataCleaner:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)


    def eurprice(price, currency):  # Ajuste de valores para as correspondências de EURO
        conversion_rates = {
            'EUR': 1,
            'CHF': 1.02,
            'DKK': 0.13,
            'GBP': 1.17,
            'Â£': 1.17,
        }
        return float(price) * conversion_rates.get(currency, 1) 

    def clean_data(self):
        self.df.columns = [col.strip() for col in self.df.columns]  
        self.df[['Currency', 'Price']] = self.df['Price'].str.split(' ', n=1, expand=True)
        self.df['EUR_price'] = self.df.apply(lambda x: DataCleaner.eurprice(x['Price'], x['Currency']), axis=1)
        self.df[['Country', 'City']] = self.df['Location'].str.split('Â»', n=1, expand=True)
        self.df[['City', 'Other']] = self.df['City'].str.split('Â»', n=1, expand=True)
        self.df['City'] = self.df['City'].str.replace('Â»', '', regex=True)
        self.df['City'] = self.df['City'].str.replace('¶', '', regex=True)
        self.df["Year Built"] = pd.to_numeric(self.df["Year Built"], errors='coerce')
        self.df.loc[self.df["Year Built"] == 0, "Year Built"] = None  # Substituindo 0 por None
        df_Structuring = self.df.drop(['Location', 'Other'], axis=1)

        return df_Structuring
