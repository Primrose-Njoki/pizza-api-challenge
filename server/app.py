from server import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from flask import jsonify
from server.controllers.restaurant_controller import get_restaurants, get_restaurant_by_id, delete_restaurant
from server.controllers.pizza_controller import get_pizzas
from server.controllers.restaurant_pizza_controller import create_restaurant_pizza

app = create_app()


@app.route('/restaurants', methods=['GET'])
def restaurants():
    return get_restaurants()

@app.route('/restaurants/<int:id>', methods=['GET'])
def restaurant(id):
    return get_restaurant_by_id(id)

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant_route(id):
    return delete_restaurant(id)


@app.route('/pizzas', methods=['GET'])
def pizzas():
    return get_pizzas()


@app.route('/restaurant_pizzas', methods=['POST'])
def restaurant_pizzas():
    return create_restaurant_pizza()

@app.cli.command("seed")
def seed_db():
    """Seed the database with initial data."""
    from server.seed import seed_data
    seed_data()
    print("Database seeded!")

if __name__ == '__main__':
    app.run(debug=True)