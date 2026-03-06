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
                 bloomed: bool = false) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> bool:
        if self.age > 5:
            self.bloomed = true


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int):
        super().__init__(name, height, age)