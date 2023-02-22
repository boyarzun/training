"""
Following ISP
Interface Segregation Principle

In this example, we have three separate interfaces, Appetizers, Entrees, and Desserts, each
containing only the methods necessary for ordering each type of food. The PizzaParlor and
IceCreamShop classes each take only the relevant interface as an argument in their
constructors, and they only contain the methods necessary for ordering pizza or ice cream,
respectively.

By breaking up the menu into smaller, more focused sections, just like breaking up the
interfaces into smaller, more focused ones, we can create a more efficient and effective
system. Customers can now choose only the dishes they want, just like the classes can
implement only the methods they need. This results in simpler, more maintainable code.
"""

from abc import ABC, abstractmethod


class Appetizers(ABC):
    @abstractmethod
    def order_appetizer(self):
        pass


class Entrees(ABC):
    @abstractmethod
    def order_entree(self):
        pass


class Desserts(ABC):
    @abstractmethod
    def order_dessert(self):
        pass


class PizzaParlor:
    def __init__(self, appetizers: Appetizers, entrees: Entrees):
        self.appetizers = appetizers
        self.entrees = entrees

    def order_pizza(self):
        # code to order pizza
        pass


class IceCreamShop:
    def __init__(self, desserts: Desserts):
        self.desserts = desserts

    def order_ice_cream(self):
        # code to order ice cream
        pass


# class EntreesService:
#     def order(pizza_restaurant: ):
#         pass


"""
NOT Following ISP
Interface Segregation Principle

In this example, we have a single large interface, Menu, containing methods for ordering all
three types of food. The Restaurant class takes an instance of this interface as a parameter
in its constructor, and the order_food method calls all three methods in the interface.

This implementation violates the Interface Segregation Principle, because the Restaurant class
is forced to implement methods it does not use. For example, if we have a PizzaParlor that only
serves pizza, it still must implement the order_dessert method, even though it is not used.

By breaking up the menu into smaller, more focused sections, we can create a more efficient
and effective system, as demonstrated in the previous example that adhered to the Interface
Segregation Principle.
"""

from abc import ABC, abstractmethod


class Menu(ABC):
    @abstractmethod
    def order_appetizer(self):
        pass

    @abstractmethod
    def order_entree(self):
        pass

    @abstractmethod
    def order_dessert(self):
        pass


class Restaurant:
    def __init__(self, menu: Menu):
        self.menu = menu

    def order_food(self):
        self.menu.order_appetizer()
        self.menu.order_entree()
        self.menu.order_dessert()


def main():
    pass


if __name__ == "__main__":
    main()
