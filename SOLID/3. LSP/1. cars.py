"""
Following LSP
Liskov Substitution Principle

In this example, the Drivable class defines an interface with the drive() method that both
the Sedan and SportsCar classes implement. The SportsCar class also has an additional
race_mode() method that is not part of the Drivable interface.

The simulate_driving() function takes an argument of type Drivable and calls its drive()
method. This function can accept instances of both the Sedan and SportsCar classes since
they both implement the Drivable interface.

However, if we were to call the simulate_driving() function with an instance of the
SportsCar class and then try to call its race_mode() method, we would get an
AttributeError, because the Drivable interface does not include a race_mode() method.
This demonstrates the violation of the Liskov Substitution Principle.
"""

from abc import ABC, abstractmethod


class IStartEngine(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class IRaceMode(ABC):
    @abstractmethod
    def race_mode(self):
        pass


class SportsCar(IStartEngine, IRaceMode):
    def start_engine(self):
        pass

    def race_mode(self):
        pass


class Sedan(IStartEngine):
    def start_engine(self):
        pass


"""
NOT Following LSP
Liskov Substitution Principle

In this example, the SportsCar class overrides the drive() method inherited from the Drivable
class, and adds a new race_mode() method that is not part of the Drivable interface.

When the simulate_driving() function is called with an instance of the SportsCar class, the
output is "Driving a sports car", indicating that the drive() method of the SportsCar class
is called. However, if we were to call the simulate_driving() function with an instance of the
SportsCar class and then try to call its race_mode() method, we would get the correct output,
"Entering race mode...".

However, when we try to call the simulate_driving() function with an instance of the SportsCar
class, we get the wrong output, "Driving a car". This is because the SportsCar class does not
behave like a Sedan class, which is what the simulate_driving() function expects. This
demonstrates a violation of the Liskov Substitution Principle.
"""


class Drivable:
    def drive(self):
        print("Driving a car")


class Sedan(Drivable):
    pass


class SportsCar(Drivable):
    def drive(self):
        print("Driving a sports car")

    def race_mode(self):
        print("Entering race mode...")


def simulate_driving(car: Drivable):
    car.drive()


sedan = Sedan()
sports_car = SportsCar()

simulate_driving(sedan)  # Output: "Driving a car"
simulate_driving(sports_car)  # Output: "Driving a sports car"

sports_car.race_mode()  # Output: "Entering race mode..."

# The following line would produce the wrong output, since the SportsCar class does not behave like a Sedan:
# simulate_driving(sports_car) # Output: "Driving a car"
