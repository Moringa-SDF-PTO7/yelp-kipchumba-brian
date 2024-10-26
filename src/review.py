class Review:
    # Initialize a new Review instance with customer, restaurant, and rating
    # Automatically adds this review to both the customer's and restaurant's review lists
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.customer.reviews_list.append(self)  # Link review to the customer's review list
        self.restaurant.reviews_list.append(self)  # Link review to the restaurant's review list

    # Property to get the customer associated with the review
    @property
    def customer(self):
        return self._customer

    # Setter for customer with validation (must be an instance of the Customer class)
    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("Customer must be an instance of the Customer class.")

    # Property to get the restaurant associated with the review
    @property
    def restaurant(self):
        return self._restaurant

    # Setter for restaurant with validation (must be an instance of the Restaurant class)
    @restaurant.setter
    def restaurant(self, value):
        if isinstance(value, Restaurant):
            self._restaurant = value
        else:
            raise ValueError("Restaurant must be an instance of the Restaurant class.")

    # Property to get the rating of the review
    @property
    def rating(self):
        return self._rating

    # Setter for rating with validation (must be an integer between 1 and 5)
    @rating.setter
    def rating(self, value):
        if isinstance(value, int) and 1 <= value <= 5:
            self._rating = value
        else:
            raise ValueError("Rating must be an integer between 1 and 5.")
