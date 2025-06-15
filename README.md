# Pizza Restaurant API

A RESTful API for a pizza restaurant built with Flask and SQLAlchemy.

## Setup Instructions

1. Clone the repository and cd to it
2. Set up the virtual environment and install dependencies:
pipenv install
pipenv shell

3. Initialize the database:

export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
4. Seed the database with initial data:

python server/seed.py

5. Run the application:

flask run

## API Endpoints
Restaurants
GET /restaurants
Returns a list of all restaurants.

Example Response:

json
[
    {
        "id": 1,
        "name": "Pizza Palace",
        "address": "123 Main St"
    },
    {
        "id": 2,
        "name": "Mario's Pizzeria",
        "address": "456 Oak Ave"
    }
]
GET /restaurants/int:id
Returns details of a single restaurant and its pizzas.

Example Response:

json
{
    "id": 1,
    "name": "Pizza Palace",
    "address": "123 Main St",
    "pizzas": [
        {
            "id": 1,
            "name": "Margherita",
            "ingredients": "Tomato sauce, mozzarella, basil"
        },
        {
            "id": 2,
            "name": "Pepperoni",
            "ingredients": "Tomato sauce, mozzarella, pepperoni"
        }
    ]
}
Error Response (404):

json
{
    "error": "Restaurant not found"
}
DELETE /restaurants/int:id
Deletes a restaurant and all related RestaurantPizzas.

Success Response: 204 No Content

Error Response (404):

json
{
    "error": "Restaurant not found"
}
Pizzas
GET /pizzas
Returns a list of all pizzas.

Example Response:

json
[
    {
        "id": 1,
        "name": "Margherita",
        "ingredients": "Tomato sauce, mozzarella, basil"
    },
    {
        "id": 2,
        "name": "Pepperoni",
        "ingredients": "Tomato sauce, mozzarella, pepperoni"
    }
]
RestaurantPizzas
POST /restaurant_pizzas
Creates a new RestaurantPizza.

Request Body:

json
{
    "price": 5,
    "pizza_id": 1,
    "restaurant_id": 3
}
Success Response (201):

json
{
    "id": 4,
    "price": 5,
    "pizza": {
        "id": 1,
        "name": "Margherita",
        "ingredients": "Tomato sauce, mozzarella, basil"
    },
    "restaurant": {
        "id": 3,
        "name": "Luigi's Pizza",
        "address": "789 Pine Rd"
    }
}
Error Responses:

400 Bad Request for validation errors

json
{
    "errors": ["Price must be between 1 and 30"]
}
404 Not Found if pizza or restaurant doesn't exist

json
{
    "errors": ["Pizza or Restaurant not found"]
}
## Testing with Postman
Import the Postman collection challenge-1-pizzas.postman_collection.json

Start your Flask server

Run the requests in Postman to test all endpoints

## Validation Rules
Restaurant:

Name must be unique

Name and address cannot be empty

Pizza:

Name and ingredients cannot be empty

RestaurantPizza:

Price must be between 1 and 30 (inclusive)

Must reference existing pizza and restaurant