#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self, days: int) -> None:
        self.height += days * 2

    def age(self, days: int) -> None:
        self.plant_age += days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


if __name__ == "__main__":
    plant = Plant("Rose", 10, 5)
    print(" === Garden Plant Growth === ")
    print("\n = Day 1 = ")
    plant.show()
    days = int(input("How many days spent ? "))
    i = 1
    for i in range(i, days + 1):
        print(" = Day", i + 1, "= ")
        plant.grow(1)
        plant.age(1)
        plant.show()
    print(f"\nGrowth this week : {days * 2}cm")
