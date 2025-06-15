from server import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
   
    db.drop_all()
    db.create_all()
    
   
    restaurants = [
        Restaurant(name="Pizza Palace", address="123 Main St"),
        Restaurant(name="Mario's Pizzeria", address="456 Oak Ave"),
        Restaurant(name="Luigi's Pizza", address="789 Pine Rd")
    ]
    
    for restaurant in restaurants:
        db.session.add(restaurant)
    
   
    pizzas = [
        Pizza(name="Margherita", ingredients="Tomato sauce, mozzarella, basil"),
        Pizza(name="Pepperoni", ingredients="Tomato sauce, mozzarella, pepperoni"),
        Pizza(name="Vegetarian", ingredients="Tomato sauce, mozzarella, mushrooms, onions, peppers")
    ]
    
    for pizza in pizzas:
        db.session.add(pizza)
    
    db.session.commit()
    
   
    restaurant_pizzas = [
        RestaurantPizza(price=10, pizza_id=1, restaurant_id=1),
        RestaurantPizza(price=12, pizza_id=2, restaurant_id=1),
        RestaurantPizza(price=9, pizza_id=1, restaurant_id=2),
        RestaurantPizza(price=15, pizza_id=3, restaurant_id=3)
    ]
    
    for rp in restaurant_pizzas:
        db.session.add(rp)
    
    db.session.commit()

if __name__ == '__main__':
    seed_data()