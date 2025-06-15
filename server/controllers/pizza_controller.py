from flask import jsonify
from server.models.pizza import Pizza

def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([pizza.to_dict() for pizza in pizzas])