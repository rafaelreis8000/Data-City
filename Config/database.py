
import os

from dotenv import load_dotenv
from pymongo import MongoClient

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configurações do MongoDB
MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("MONGODB_DATABASE")

# Cria o cliente MongoDB
client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=5000
)

# Seleciona o banco de dados
db = client[DATABASE_NAME]


def verificar_conexao():
    """Verifica a comunicação com o servidor MongoDB."""

    client.admin.command("ping")

    return True