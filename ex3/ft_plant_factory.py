#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.plant_age} \
days old")


if __name__ == "__main__":
    print(" -- Plant factory output -- \n")
    plant1 = Plant("Rose", 10, 5)
    plant2 = Plant("Tulipe", 20, 10)
    plant3 = Plant("Jacinthe", 50, 20)
    plant4 = Plant("Chrysalide", 80, 50)
    plant5 = Plant("Begonia", 100, 100)
    plant1.show()
    plant2.show()
    plant3.show()
    plant4.show()
    plant5.show()
