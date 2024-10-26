# Restaurant Reviews

A simple Python application to manage customer reviews for restaurants. This project includes three main classes: `Customer`, `Restaurant`, and `Review`. These classes represent a system where customers can leave reviews for restaurants, and restaurants can compute their average ratings based on customer feedback.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### `Customer` Class
- **Attributes**: `first_name`, `last_name`, and a list of `reviews`.
- **Methods**:
  - `reviews()`: Returns a list of all reviews created by the customer.
  - `restaurants()`: Returns a unique list of restaurants reviewed by the customer.
  - `num_negative_reviews()`: Calculates the number of reviews with a rating of 1 or 2.
  - `has_reviewed_restaurant(restaurant)`: Checks if the customer has already reviewed a specific restaurant.
  - `top_negative_reviewer(customers)`: Class method that identifies the customer with the most negative reviews among a list of customers.

### `Restaurant` Class
- **Attributes**: `name` and a list of `reviews`.
- **Methods**:
  - `reviews()`: Returns a list of all reviews for the restaurant.
  - `customers()`: Returns a unique list of customers who have reviewed the restaurant.
  - `average_star_rating()`: Calculates the average rating from all reviews.
  - `top_two_restaurants(restaurants)`: Class method that returns the top two restaurants based on average ratings.

### `Review` Class
- **Attributes**: `customer`, `restaurant`, and `rating` (integer between 1 and 5).
- **Functionality**:
  - Links a review to both a `Customer` and `Restaurant` instance automatically when created.

---

## Requirements

- Python 3.x

---

## Installation

1. **Clone the Repository**  
   ```
   git clone https://github.com/DevBrianKE/yelp-kipchumba-brian.git
   cd yelp-kipchumba-brian
   ```
2. **Navigate to the Source Folder**
 ```
   cd src
 ```
3. **Run a Sample Script**
 Test and explore the classes using a Python interpreter or by writing and running a script that creates instances of Customer, Restaurant, and Review.

 ## Usage
 Here’s a simple example to get started:

 ```
 from src.customer import Customer
from src.restaurant import Restaurant
from src.review import Review

# Create instances
customer1 = Customer("John", "Doe")
restaurant1 = Restaurant("The Great Eatery")

# Create a review with a rating of 4
review1 = Review(customer1, restaurant1, 4)

# Access customer reviews and restaurants they've reviewed
print(customer1.reviews())  # List of reviews
print(customer1.restaurants())  # Unique list of restaurants reviewed

# Access average rating for a restaurant
print(restaurant1.average_star_rating())  # Average rating for restaurant1

 ```
## Project structure
```
yelp-kipchumba-brian/
├── LICENSE
├── README.md
├── data/                # Placeholder for any data files
├── docs/                # Documentation files
├── notebooks/           # Jupyter notebooks if applicable
├── src/
│   ├── customer.py      # Customer class definition
│   ├── restaurant.py    # Restaurant class definition
│   └── review.py        # Review class definition
└── tests/               # Unit tests for each class
```
## Contributing
Feel free to submit issues or pull requests. To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make and commit your changes.
4. Push to your branch.
5. Submit a pull request.


## License
This project is licensed under the MIT License.

