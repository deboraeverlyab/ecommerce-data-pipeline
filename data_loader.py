import kagglehub
import pandas as pd
import os

class DataLoader:
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        self.file_path = None

    def download_dataset(self):
        path = kagglehub.dataset_download(self.dataset_name)
        print(f"Dataset baixado em: {path}")

        files = os.listdir(path)
        csv_files = [f for f in files if f.endswith(".csv")]

        if not csv_files:
            raise FileNotFoundError("Nenhum arquivo CSV encontrado no dataset!")

        self.file_path = os.path.join(path, csv_files[0])
        print(f"Arquivo CSV encontrado: {self.file_path}")
        return self.file_path

