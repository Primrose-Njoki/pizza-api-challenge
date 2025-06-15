from flask import request, jsonify
from server import db
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
 
    restaurant_pizzas = RestaurantPizza.query.filter_by(restaurant_id=id).all()
    pizzas = [rp.pizza.to_dict() for rp in restaurant_pizzas]
    
    response = restaurant.to_dict()
    response['pizzas'] = pizzas
    return jsonify(response)

def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204