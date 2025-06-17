
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent))

from server import create_app, db
from server.models import Restaurant, Pizza, RestaurantPizza

def seed_data():
    app = create_app()
    
    with app.app_context():
        print(" Dropping all tables...")
        db.drop_all()
        
        print(" Creating tables...")
        db.create_all()
        
        print(" Adding restaurants...")
        restaurants = [
            Restaurant(name="Mario's Pizza", address="123 Main St"),
            Restaurant(name="Luigi's Place", address="456 Oak Ave")
        ]
        db.session.add_all(restaurants)
        
        print(" Adding pizzas...")
        pizzas = [
            Pizza(name="Margherita", ingredients="Tomato, Mozzarella"),
            Pizza(name="Pepperoni", ingredients="Tomato, Pepperoni")
        ]
        db.session.add_all(pizzas)
        
        db.session.commit()
        
        print(" Creating associations...")
        rps = [
            RestaurantPizza(price=10, pizza_id=1, restaurant_id=1),
            RestaurantPizza(price=12, pizza_id=2, restaurant_id=1)
        ]
        db.session.add_all(rps)
        
        db.session.commit()
        print(" Seeded 2 restaurants, 2 pizzas, and 2 associations!")

if __name__ == '__main__':
    seed_data()