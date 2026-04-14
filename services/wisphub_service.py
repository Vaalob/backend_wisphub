import requests
from config import Config

headers = {
    "Authorization": f"Bearer {Config.WISPHUB_API_KEY}",
    "Content-Type": "application/json"
}

def obtener_cliente(cliente_id):
    url = f"{Config.WISPHUB_BASE_URL}/customers/{cliente_id}"
    response = requests.get(url, headers=headers)
    return response.json()

def obtener_facturas(cliente_id):
    url = f"{Config.WISPHUB_BASE_URL}/customers/{cliente_id}/invoices"
    response = requests.get(url, headers=headers)
    return response.json()