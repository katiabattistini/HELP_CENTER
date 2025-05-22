import requests
import pandas as pd
from dotenv import load_dotenv
import os
from datetime import datetime

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter credenciais do arquivo .env
API_KEY = os.getenv('API_KEY')
URL = os.getenv('API_URL')

# Verifica se as credenciais foram carregadas corretamente
if not API_KEY or not URL:
    raise ValueError("Verifique se API_KEY e API_URL estão configuradas no arquivo .env.")

# Calcula a data atual no formato ISO
current_date_iso = datetime.utcnow().isoformat()

def get_safe_value(data, keys, default="vazio"):
    """Extrai um valor do dicionário de dados."""
    try:
        for key in keys:
            if data is None:
                return default
            if isinstance(data, list) and key.isdigit() and int(key) < len(data):
                data = data[int(key)]
            else:
                data = data.get(key, {})
            if data is None:
                return default
        return data if data is not None else default
    except Exception as e:
        print(f"Error: {e}")
        return default

# Configura URL da API com parâmetros de filtro
url = f"{URL}?query={{\"attributes\":[\"id\",\"protocol\",\"userId\",\"departmentId\",\"updatedAt\",\"startedAt\",\"endedAt\",\"comments\",\"metrics\"],\"distinct\":true,\"order\":[[\"startedAt\",\"DESC\"]],\"where\":{\"$or\":{\"startedAt\":{\"$gte\":\"2023-10-01T00:00:00.000Z\",\"$lte\":\"%s\"},\"endedAt\":{\"$gte\":\"2023-10-01T00:00:00.000Z\",\"$lte\":\"%s\"}}},\"include\":[{\"model\":\"contact\",\"attributes\":[\"id\",\"name\",\"data\",\"serviceId\"],\"where\":{\"visible\":true},\"include\":[{\"model\":\"service\",\"attributes\":[\"id\",\"name\"]},{\"model\":\"tags\",\"attributes\":[\"id\",\"label\"]},{\"model\":\"customFieldValues\",\"attributes\":[\"value\",\"relatedType\"],\"include\":[{\"model\":\"customField\",\"attributes\":[\"name\"]}]}]},{\"model\":\"user\",\"attributes\":[\"id\",\"name\",\"email\"]},{\"model\":\"department\",\"attributes\":[\"id\",\"name\"]},{\"model\":\"ticketTopics\",\"attributes\":[\"id\",\"name\"]}],\"page\":1,\"perPage\":20000}" % (
current_date_iso, current_date_iso)}" # parâmetros de acordo com domuentação da plataforma de atendimento

# Configura o cabeçalho da requisição
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Fazer a solicitação à API
response = requests.get(url, headers=headers)

# Verifica se a resposta da API foi bem-sucedida
if response.status_code == 200:
    data = response.json()
else:
    print(f"Erro na requisição: {response.status_code}")
    exit()

# Inicializar listas vazias para cada coluna esperada
columns = ["protocol", "updatedAt", "startedAt", "endedAt", "contact_name", "user_name", "department_name",
           "ticket_topic_name", "contact_tags_label", "contact_customFieldValues_customField_name", "user_email"]

data_list = []

# Processa cada ticket obtido
for ticket in data.get('data', []):
    row_data = {}
    for col in columns:
        keys = col.split("_")
        value = get_safe_value(ticket, keys)
        row_data[col] = value

    # Adiciona os dados da linha à lista
    data_list.append(row_data)

# Cria um DataFrame usando pandas
df = pd.DataFrame(data_list)

# Preenche valores nulos com "vazio"
df.fillna("vazio", inplace=True)

# Salva o DataFrame em um arquivo CSV
output_file_path = 'help_center_file.csv'
df.to_csv(output_file_path, index=False)
print(f'O arquivo CSV foi salvo em: {output_file_path}')