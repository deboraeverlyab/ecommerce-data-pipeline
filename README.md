# 🚀 E-commerce Data Pipeline (Boat Sales)
Este projeto é um pipeline ETL que extrai dados de vendas de barcos do Kaggle, transforma e carrega em um Banco de Dados SQL, para depois criar uma planilha Google com os dados desse banco,  possibilitando a análise no Looker.

## 📌 1. Pré-requisitos
Antes de executar o projeto, instale os seguintes softwares:

Python 3.8+ (Certifique-se de ter o Python instalado)

## 🔧 2. Configuração do Ambiente
### 2.1. Clone o repositório
Abra o terminal e execute:

```
git clone https://github.com/seu-usuario/ecommerce-data-pipeline.git
cd ecommerce-data-pipeline
```

### 2.2. Instale as dependências

```
pip install -r requirements.txt
```

### 2.3. Configure suas credenciais do google

Configure o arquivo credentials.json.

Coloque o arquivo credentials.json no diretório do projeto.

O script irá utilizá-lo para fazer o processo de autenticação OAuth, para envio dos dados a Planilha Google.


## 🚀 3. Como Executar o Pipeline
Agora que tudo está configurado, execute:

```
python main.py
```

Este script fará: 

✅ Baixar os dados do Kaggle

✅ Fazer a limpeza e transformação dos dados

✅ Adiciona dados ao Banco SQL

✅ Inserir os dados na Planilha Google

## 📊 4. Visualização dos Dados no Looker
Depois que os dados estiverem na planilha: 

```https://docs.google.com/spreadsheets/d/1r88W57Xp0QKSridTViy2QNU_-jG-XPNnZ9pHT1XTyWY/edit?usp=sharing```


Abra o Looker: 

```https://lookerstudio.google.com/reporting/560a3e75-6806-42d4-bd2f-bd6ae0a2a7ae```

![image](https://github.com/user-attachments/assets/a153c8fe-b61d-4582-9154-c4f950a66cda)



## 🔍 5. Estrutura do Projeto

ecommerce-data-pipeline/

│── data_loader.py       # Faz o download dos dados do Kaggle

│── data_cleaner.py      # Realiza a limpeza e padronização dos dados

│── database.py          # Conecta ao SQLite e carrega os dados

│── gsupdater.py         # Carrega os dados do banco SQL para a planilha Google

│── main.py              # Orquestra todo o pipeline

│── requirements.txt     # Lista de pacotes necessários

│── README.md            # Documentação do projeto


## Contatos:


📧 Email: deboraeverly@hotmail.com

🔗 LinkedIn: https://www.linkedin.com/in/debora-everly/
