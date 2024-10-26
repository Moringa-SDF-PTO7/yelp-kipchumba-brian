class Customer:
    # Initialize a new Customer object with first and last names, and an empty list for reviews
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews_list = []  # Initialize an empty list to store customer's reviews

    # Property for getting first name
    @property
    def first_name(self):
        return self._first_name

    # Setter for first name with validation (1-25 characters)
    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._first_name = value
        else:
            raise ValueError("First name must be a string between 1 and 25 characters.")

    # Property for getting last name
    @property
    def last_name(self):
        return self._last_name

    # Setter for last name with validation (1-25 characters)
    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._last_name = value
        else:
            raise ValueError("Last name must be a string between 1 and 25 characters.")

    # Method to return the list of reviews associated with the customer
    def reviews(self):
        return self.reviews_list

    # Method to return a list of unique restaurants the customer has reviewed
    def restaurants(self):
        return list(set(review.restaurant for review in self.reviews_list))

    # Method to calculate the number of negative reviews (ratings 1 or 2) by the customer
    def num_negative_reviews(self):
        return sum(1 for review in self.reviews_list if review.rating in [1, 2])

    # Method to check if the customer has reviewed a specific restaurant
    def has_reviewed_restaurant(self, restaurant):
        return any(review.restaurant == restaurant for review in self.reviews_list)

    # Class method to find the customer with the most negative reviews from a list of customers
    @classmethod
    def top_negative_reviewer(cls, customers):
        return max(customers, key=lambda customer: customer.num_negative_reviews(), default=None)
