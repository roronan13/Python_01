#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} \
days old")


class Tree(Plant):
    def __init__(self, name: str, height: int, plant_age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"   [Asking the {self.name} to produce shade...]")
        print(f"{self.name} now produces a shade of {self.height}cm long \
and {self.trunk_diameter}cm wide")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter : {self.trunk_diameter}cm")


class Flower(Plant):
    def __init__(self, name: str, height: int, plant_age: int, color: str,
                 bloomed: bool = False) -> None:
        super().__init__(name, height, plant_age)
        self.color = color
        self.bloomed = bloomed

    def bloom(self) -> None:
        print(f"   [Asking the {self.name} to bloom...]")
        self.bloomed = True

    def is_bloomed(self) -> None:
        if self.bloomed:
            print(f'{self.name} is blooming beautifully !')
        else:
            print(f'{self.name} is not blooming yet !')

    def show(self) -> None:
        super().show()
        print(f"Color : {self.color}")
        self.is_bloomed()


class Vegetable(Plant):
    def __init__(self, name: str, height: int, plant_age: int,
                 harvest_season: str, nutritional_value: int = 0) -> None:
        super().__init__(name, height, plant_age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season : {self.harvest_season}")
        print(f"Nutritional value : {self.nutritional_value}")

    def grow(self, days: int) -> None:
        self.height += (days * 2)

    def age(self, days: int) -> None:
        self.plant_age += days

    def grow_and_age(self, days: int) -> None:
        print(f"   [Make {self.name} grow and age for {days} days...]")
        self.grow(days)
        self.age(days)
        self.nutritional_value += days


if __name__ == "__main__":
    print(" === Garden Plant Types === ")
    Lila = Flower("Lila", 10, 6, "purple")
    Oak = Tree("Oak", 500, 10, 20)
    Tomato = Vegetable("Tomato", 20, 3, "spring")
    print("\n === Flower === ")
    Lila.show()
    Lila.bloom()
    Lila.show()
    print("\n === Tree === ")
    Oak.show()
    Oak.produce_shade()
    print("\n === Vegetable === ")
    Tomato.show()
    Tomato.grow_and_age(10)
    Tomato.show()
