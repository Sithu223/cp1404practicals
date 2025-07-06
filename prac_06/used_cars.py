"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(name="Mercedes", fuel = 42, odometer = 277)
    another_car = Car(name = "BMW", fuel = 50, odometer = 150)
    my_car.drive(30)
    limo = Car("RangeRover", 100)
    limo.add_fuel(20)
    limo.drive(115)
    print(limo)
    print(f"Car has fuel: {my_car.fuel}")
    print(f"Car drove: {limo.drive(115)}km.")
    print(my_car)
    print(another_car)


main()