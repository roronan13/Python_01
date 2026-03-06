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


class Owner:
    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name
        self.plants = []
        self.number_of_plants = 0


class GardenManager:
    def __init__(self, name: str) -> None:
        self.owners = []
        self.plants = []
        self.number_of_owners = 0
        self.number_of_plants = 0

    def AddOwner(self, owner: Owner) -> None:
        self.owners.append(owner_name)
        self.number_of_owners += 1
        self.owners.owner_name.owner_plants = []

    def GetNumberOwners(self) -> int:
        return self.number_of_owners

    def AddPlant(self, plant_name: str, owner_name: str) -> None:
        self.plants.append(plant_name)
        self.number_of_plants += 1
        for self.owner_name in self.owners:
            if self.owner_name == owner_name:
                self.owner_name.owner_plants.append(plant_name)


class Owner:
    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name
        self.plants = []
        self.number_of_plants = 0


    # def GardenStats(self) -> None:


    # def create_garden_network(self) -> None:


if __name__ == "__main__":
    My_Garden = GardenManager("My Garden")
    My_Garden.AddOwner("Ronan")
    My_Garden.AddOwner("Jean")
    My_Garden.AddOwner("Jacques")
    for My_Garden.owner in My_Garden.owners:
        print(f'{My_Garden.owner}')
        for My_Garden.owner.name in My_Garden.owners:
            print(f'  --  {My_Garden.owner.name}')
    print(f'Total gardens managed : {My_Garden.GetNumberOwners()}')
    My_Garden.AddPlant("Lila", "Ronan")
