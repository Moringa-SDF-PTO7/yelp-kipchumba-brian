class Restaurant:
    # Initialize a new Restaurant object with a name and an empty list for reviews
    def __init__(self, name):
        self.name = name
        self.reviews_list = []  # Initialize an empty list to store restaurant reviews

    # Property for getting the restaurant's name
    @property
    def name(self):
        return self._name

    # Setter for restaurant name with validation (must be a non-empty string)
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Restaurant name must be a string with at least 1 character.")

    # Method to return the list of reviews associated with the restaurant
    def reviews(self):
        return self.reviews_list

    # Method to return a list of unique customers who reviewed the restaurant
    def customers(self):
        return list(set(review.customer for review in self.reviews_list))

    # Method to calculate the average star rating from all reviews (rounded to 1 decimal place)
    # Returns 0.0 if there are no reviews
    def average_star_rating(self):
        if not self.reviews_list:
            return 0.0
        return round(sum(review.rating for review in self.reviews_list) / len(self.reviews_list), 1)

    # Class method to find the top two restaurants by average star rating from a list of restaurants
    # Sorts restaurants in descending order by average star rating and returns the top two
    @classmethod
    def top_two_restaurants(cls, restaurants):
        return sorted(restaurants, key=lambda restaurant: restaurant.average_star_rating(), reverse=True)[:2]
