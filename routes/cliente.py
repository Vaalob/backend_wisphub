from flask import Blueprint, jsonify, request
from services.wisphub_service import obtener_cliente, obtener_facturas
from utils.formatter import formatear_cliente

cliente_bp = Blueprint("cliente", __name__)

@cliente_bp.route("/cliente")
def get_cliente():
    cliente_id = request.args.get("id")

    cliente = obtener_cliente(cliente_id)
    facturas = obtener_facturas(cliente_id)

    data = formatear_cliente(cliente, facturas)

    return jsonify(data)