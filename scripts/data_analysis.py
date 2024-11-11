import pandas as pd

# Carregar o arquivo Parquet com os dados limpos
file_path = './data/cleaned_data_science_job.parquet'
data = pd.read_parquet(file_path)

# Dicionário de mapeamento para expandir os níveis de experiência
experience_mapping = {
    'EN': 'Entry-level',
    'MI': 'Mid-level',
    'SE': 'Senior-level',
    'EX': 'Expert-level'
}

# Dicionário de mapeamento para expandir os tipos de contrato
employment_type_mapping = {
    'FT': 'Full-time',
    'PT': 'Part-time',
    'CT': 'Contract',
    'FL': 'Freelance'
}

# Substituir as abreviações na coluna 'experience_level' pelo texto completo
data['experience_level'] = data['experience_level'].map(experience_mapping)

# Substituir as abreviações na coluna 'employment_type' pelo texto completo
data['employment_type'] = data['employment_type'].map(employment_type_mapping)

# Contagem de candidatos por nível de experiência (ignora o tipo de emprego)
experience_counts_no_employment_type = data.groupby('experience_level').size()
print("\nContagem de Candidatos por Nível de Experiência (Ignorando Tipo de Emprego):")
print(experience_counts_no_employment_type)

# Análise adicional - Contagem de candidatos por localização e nível de experiência
grouped_data_no_employment_type = data.groupby(['employee_residence', 'experience_level']).size().reset_index(name='count')
print("\nDistribuição de Candidatos por Localização e Nível de Experiência (Ignorando Tipo de Emprego):")
print(grouped_data_no_employment_type)

# Salvar os resultados da análise em CSV para referência futura
experience_counts_no_employment_type.to_csv('./data/experience_counts.csv', header=True)
grouped_data_no_employment_type.to_csv('./data/grouped_data_no_employment_type.csv', index=False)
print("Análises salvas nos arquivos 'experience_counts.csv' e 'grouped_data_no_employment_type.csv'.")
