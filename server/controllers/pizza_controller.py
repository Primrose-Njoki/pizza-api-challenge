from flask import Blueprint, jsonify
from server.models import Pizza

pizza_bp = Blueprint('pizza', __name__, url_prefix='/pizzas')

@pizza_bp.route('/', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([p.to_dict() for p in pizzas])