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

    def bloom(self) -> None:
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
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    print(" -- Garden Plant Types --  ")
    Lila = Flower("Lila", 10, 6, "purple")
    Lila.bloom()
    print(f'{Lila.name} (Flower) : {Lila.height}cm, {Lila.age} days, {Lila.color} color')
    Lila.is_bloomed()
    Rose = Flower("Rose", 20, 5, "rose")
    Rose.bloom()
    print(f'{Rose.name} (Flower) : {Rose.height}cm, {Rose.age} days, {Rose.color} color')
    Rose.is_bloomed()
    Oak = Tree("Oak", 3000, 50, 20)
    print(f'{Oak.name} (Tree) : {Oak.height}cm, {Oak.age} days, {Oak.trunk_diameter}cm diameter')
    print(f'{Oak.name} provides {Oak.produce_shade()} square meters of shade')
    Birch = Tree("Birch", 2000, 40, 15)
    print(f'{Birch.name} (Tree) : {Birch.height}cm, {Birch.age} days, {Birch.trunk_diameter}cm diameter')
    print(f'{Birch.name} provides {Birch.produce_shade()} square meters of shade')
    Tomato = Vegetable("Tomato", 20, 3, "winter", "proteins")
    print(f'{Tomato.name} (Vegetable) : {Tomato.height}cm, {Tomato.age}days, {Tomato.harvest_season} harvest')
    print(f'{Tomato.name} is rich in {Tomato.nutritional_value}')
    Carot = Vegetable("Carot", 35, 7, "summer", "calcium")
    print(f'{Carot.name} (Vegetable) : {Carot.height}cm, {Carot.age}days, {Carot.harvest_season} harvest')
    print(f'{Carot.name} is rich in {Carot.nutritional_value}')
