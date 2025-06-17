from flask import Blueprint, request, jsonify
from server.models import RestaurantPizza, Restaurant, Pizza
from server import db

rp_bp = Blueprint('restaurant_pizza', __name__, url_prefix='/restaurant_pizzas')

@rp_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    required_fields = ['price', 'pizza_id', 'restaurant_id']
    if not all(field in data for field in required_fields):
        return jsonify({"errors": ["Missing required fields"]}), 400
    
    if not 1 <= data['price'] <= 30:
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
    
    pizza = Pizza.query.get(data['pizza_id'])
    restaurant = Restaurant.query.get(data['restaurant_id'])
    
    if not pizza or not restaurant:
        return jsonify({"errors": ["Pizza or Restaurant not found"]}), 404
    
    try:
        rp = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        
        db.session.add(rp)
        db.session.commit()
        
        return jsonify(rp.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400