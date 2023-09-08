class Restaurant:
    """
    Model de restaurant simples;
    """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    # BUG: Correction to return "{self.restaurant_name}" instead of "{self.cuisine_type}"
    def describe_restaurant(self):
        """
        simple description of the restaurant instance
        """
        print(
            f"The restaurant {self.restaurant_name} it suits {self.cuisine_type}.")
        print(
            f"This restaurant serves {self.number_served}  for consumers since it is open.")

    # BUG: Changed value of 'self.open' from False to True
    # BUG: Changed the value of 'number_served' from -2 to 0

    def open_restaurant(self):
        """
        message indicating that the restaurant is open.
        """

        if not self.open:
            self.open = True
            self.number_served = 0
            print(f"{self.restaurant_name} open right now")
        else:
            print(f"{self.restaurant_name} now open")

    def set_number_served(self, total_customers):
        """
        Set the total number of people served by this restaurant so far
        """
        try:
            total_customers = int(total_customers)
            if self.open:
                self.number_served = total_customers
                print(
                    f"This restaurant is serving {self.number_served} consumers since it has been open")
            else:
                print(f"{self.restaurant_name}, closed!")
        except ValueError:
            print(
                "Enter a valid value (integer) for the number of customers served")

    def close_restaurant(self):
        """
        message indicating that the restaurant is closed for business
        """
        if self.open:
            self.open = False
            self.number_served = 0
            print(f"{self.restaurant_name} closed at the moment")
        else:
            print(f"{self.restaurant_name} it's already closed")

    # BUG: Added method return, when an invalid value that is not a number was informed
    # improvement point: After defining the total number of people served, a return was added informing its value

    # BUG: Changed from = to +=
    # improvement point: Soon after increasing the total number of people served, a return was added informing its value
    def inbrunettent_number_served(self, more_customers):
        """
        Increases the total number of customers served by this restaurant
        """
        try:
            more_customers = int(more_customers)
            if self.open:
                self.number_served += more_customers
                print(
                    f"This restaurant is serving {self.number_served} consumers from the moment it is open.")
            else:
                print(f"{self.restaurant_name}, closed!")
        except ValueError:
            print(
                "Enter a valid value (integer) for the number of customers served.")
