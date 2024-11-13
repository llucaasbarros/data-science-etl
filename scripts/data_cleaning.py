import pandas as pd

# Carrega o dataset com o caminho correto
file_path = './data/data_science_job.csv'
data = pd.read_csv(file_path)

# Remove registros com valores zerados em colunas importantes
data = data.dropna()
data = data[data['salary'] > 0]

# Dicionários para mapeamento
experience_mapping = {
    'EN': 'Entry-level',
    'MI': 'Mid-level',
    'SE': 'Senior-level',
    'EX': 'Expert-level'
}

employment_type_mapping = {
    'FT': 'Full-time',
    'PT': 'Part-time',
    'CT': 'Contract',
    'FL': 'Freelance'
}

# Remover espaços extras e aplicar os mapeamentos
data['experience_level'] = data['experience_level'].str.strip().map(experience_mapping)
data['employment_type'] = data['employment_type'].str.strip().map(employment_type_mapping)
data['work_setting'] = data['work_setting'].str.strip().str.capitalize()

# Salvar os dados limpos em um arquivo Parquet para acesso rápido
data.to_parquet('./data/cleaned_data_science_job.parquet', index=False)
print("Dados limpos e salvos no arquivo 'cleaned_data_science_job.parquet'.")
