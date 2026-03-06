class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> int:
        shade = self.height * 2
        return shade


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: int,
                 bloomed: bool = False) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> bool:
        if self.age > 5:
            self.bloomed = True
        else:
            self.bloomed = False

    def is_bloomed(self) -> None:
        if self.bloomed:
            print(f'{self.name} is blooming beautifully !')
        else:
            print(f'{self.name} is not blooming yet !')


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    print(" -- Garden Plant Types --  ")
    Lila = Flower("Lila", 10, 6, "purple")
    Lila.bloom()
    print(f'{Lila.name} (Flower) : {Lila.height}cm, {Lila.age} days, {Lila.color} color')
    Lila.is_bloomed()
    Rose = Flower("Rose", 20, 3, "rose")
    Rose.bloom()
    print(f'{Rose.name} (Flower) : {Rose.height}cm, {Rose.age} days, {Rose.color} color')
    Rose.is_bloomed()
    Oak = Tree("Oak", 3000, 50, 20)
    