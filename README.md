Data Analysis Pipeline
Este projeto é uma pipeline de análise de dados projetada para coletar, processar e armazenar dados de mercado de trabalho, especificamente na área de ciência de dados. Utilizando Python e MongoDB, o pipeline faz uma análise dos dados a partir de um arquivo Parquet, gera insights e armazena os resultados em um banco de dados para consultas futuras.

Principais Arquivos e Diretórios
data/: Diretório onde os arquivos de dados estão armazenados, incluindo os arquivos Parquet e CSV.
scripts/data_cleaning.py: Script para realizar a limpeza dos dados e salvar o resultado em um arquivo Parquet.
scripts/data_analysis.py: Script para carregar dados limpos e realizar análises exploratórias, como contagens de experiência e tipos de contrato.
scripts/parquet_to_mongodb.py: Script para carregar dados de um arquivo Parquet e inseri-los no MongoDB.
.env: Arquivo que armazena variáveis sensíveis (ex. URL de conexão com MongoDB), que não é incluído no repositório.
README.md: Arquivo de documentação do projeto.
Funcionalidades
Limpeza de Dados: Carrega dados de um arquivo CSV, limpa e padroniza, e armazena o resultado em formato Parquet para facilitar o acesso e a análise.
Análise de Dados: Realiza uma análise exploratória para contar candidatos por localização, nível de experiência e tipo de contrato. Salva os resultados em arquivos CSV para referência futura.
Integração com MongoDB: Conecta-se ao MongoDB usando a biblioteca pymongo e insere os dados do arquivo Parquet em uma coleção específica para armazenamento e consulta.
Pré-requisitos
Python 3.x
MongoDB
Bibliotecas Python:
pandas
pymongo
python-dotenv
Para instalar as bibliotecas necessárias, você pode usar:

bash
Copy code
pip install pandas pymongo python-dotenv
Configuração do Projeto
Configurar o Arquivo .env:

Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
ruby
Copy code
MONGODB_URL=mongodb+srv://usuario:senha@cluster0.ahm53kz.mongodb.net/?retryWrites=true&w=majority
Substitua usuario, senha, e cluster0.ahm53kz.mongodb.net com suas credenciais MongoDB.
Adicionar .env ao .gitignore:

Garanta que o .env está listado no .gitignore para manter as credenciais seguras.
Uso
1. Limpeza de Dados
Execute o script data_cleaning.py para limpar e preparar os dados:

2. Análise de Dados
Execute data_analysis.py para gerar contagens de candidatos por nível de experiência e localização:

3. Inserção no MongoDB
Execute parquet_to_mongodb.py para inserir os dados limpos no MongoDB:

Exemplos de Saída
experience_counts.csv: Contém a contagem de candidatos por nível de experiência.
grouped_data_no_employment_type.csv: Mostra a distribuição de candidatos por localização e nível de experiência.
