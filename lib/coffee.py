#!/usr/bin/env python3

class Coffee:
    """
    Represents a coffee order with a size and price.
    """

    def __init__(self, size, price):
        """
        Initialize a new Coffee instance.
        """
        self.size = size
        self.price = price

    @property
    def size(self):
        """
        Getter for coffee size.
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Validates that size is Small, Medium, or Large.
        """
        if size in ["Small", "Medium", "Large"]:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        """
        Adds a $1 tip to the coffee price.
        """
        print("This coffee is great, here’s a tip!")
        self.price += 1