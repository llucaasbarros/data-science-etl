import pandas as pd

# Carrega o dataset com o caminho correto
file_path = './data/data_science_job.csv'
data = pd.read_csv(file_path)

# 1. Limpeza dos Dados

# Remover registros com valores ausentes em colunas importantes
data = data.dropna()

# Tratar valores para a coluna salário
data = data[data['salary'] > 0]

# Padronizar colunas removendo espaços em branco
data['experience_level'] = data['experience_level'].str.strip().str.upper()
data['employment_type'] = data['employment_type'].str.strip().str.upper()
data['work_setting'] = data['work_setting'].str.strip().str.capitalize()

# Salvar os dados limpos em um arquivo Parquet para acesso rápido
data.to_parquet('./data/cleaned_data_science_job.parquet', index=False)
print("Dados limpos e salvos no arquivo 'cleaned_data_science_job.parquet'.")
