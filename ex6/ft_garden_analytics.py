class Plant:
    def __init__(self, name: str, height: int, age: int, owner: str) -> None:
        self.name = name
        self.__height = height
        self.__age = age
        self.owner = owner


class FloweringPlant(Plant):
    def __int__(self, name: str, height: int, age: int, flowered: bool):
        super().__init__(name, height, age)


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, flowered: bool,
                 prize: int):
        super().__init__(name, height, age, flowered)


class GardenManager:
    def __init__(self, name: str) -> None:
        self.owners = []
        self.number_of_owners = 0

    def AddOwner(self, owner: str) -> None:
        self.owners.append(owner)
        self.number_of_owners += 1

    def GetNumber(self) -> int:
        return self.number_of_owners


    # def GardenStats(self) -> None:


    # def create_garden_network(self) -> None:


if __name__ == "__main__":
    My_Garden = GardenManager("My Garden")
    My_Garden.AddOwner("Ronan")
    My_Garden.AddOwner("Jean")
    for My_Garden.owner in My_Garden.owners:
        print(f'{My_Garden.owner}')
    print(f'Total gardens managed : {My_Garden.GetNumber()}')
