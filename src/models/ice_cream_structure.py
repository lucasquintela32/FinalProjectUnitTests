from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """
    A specialized type of restaurant.
    """

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Get attributes from the parent class.
        initialize the specific attributes of an ice cream shop.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    # first checking if there is a stock, if there is, display the list of flavors
    # improvement point: Change order of method evaluations.
    def flavors_available(self):
        """
        Interact the list of available flavors and print
        """
        if not self.flavors:
            print("No stock at the moment!")
        else:
            print("These flavors are currently unavailable:")
            for flavor in self.flavors:
                print(f"\t-{flavor}")

    # BUG: Add method return, when an empty string was informed.
    # BUG: Fix the method return, so that it reports the flavor and not the list of flavors.
    # improvement point: Make the correction in the order of the method evaluations.
    # Validate if it is in stock first, check if you are looking for a valid flavor and whether or not it has the flavor.

    def find_flavor(self, flavor):
        """
        validate if the informed flavor is available.
        """
        if not self.flavors:
            print("Out of stock at the moment")
        elif not isinstance(flavor, str) or flavor == '':
            print("Invalid flavor, please provide a valid flavor")
        elif flavor in self.flavors:
            print(f"valid flavor {flavor}")
        else:
            print(f"Not in stock {flavor}")

    # BUG: Removed from the method the unnecessary return "The flavor is currently available!"
    # BUG: Added method return when an empty string is informed
    def add_flavor(self, flavor):
        """
        inform the flavor in stock
        """
        if flavor == '':
            print("Invalid flavor, enter a valid flavor")
        elif flavor in self.flavors:
            print(f"{flavor} available in stock")
        else:
            self.flavors.append(flavor)
            print(f"{flavor} added to stock")
