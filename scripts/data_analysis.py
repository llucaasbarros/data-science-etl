import pandas as pd

# Carregar o arquivo Parquet com os dados limpos
file_path = './data/cleaned_data_science_job.parquet'
data = pd.read_parquet(file_path)


# Contagem de candidatos por nível de experiência (ignora o tipo de emprego)
experience_counts_no_employment_type = data.groupby('experience_level').size()
print("\nContagem de Candidatos por Nível de Experiência (Ignorando Tipo de Emprego):")
print(experience_counts_no_employment_type)

# Contagem de candidatos por localização e nível de experiência
grouped_data_no_employment_type = data.groupby(['employee_residence', 'experience_level']).size().reset_index(name='count')
print("\nDistribuição de Candidatos por Localização e Nível de Experiência (Ignorando Tipo de Emprego):")
print(grouped_data_no_employment_type)

# Análise da média salarial em dólar.
salary_in_usd_mean = data['salary_in_usd'].mean()
formatted_salary_mean = f"${salary_in_usd_mean:,.2f}"
print('A média dos salários de todos os empregos na área de dados pagos em dólar é:', formatted_salary_mean, 'por ano.')

# Salvar os resultados da análise em CSV para referência futura
experience_counts_no_employment_type.to_csv('./data/experience_counts.csv', header=True)
grouped_data_no_employment_type.to_csv('./data/grouped_data_no_employment_type.csv', index=False)
print("Análises salvas nos arquivos 'experience_counts.csv' e 'grouped_data_no_employment_type.csv'.")


