class Plant:
    def __init__(self, plant_name: str, height: int, age: int) -> None:
        self.plant_name = plant_name
        self.__height = height
        self.__age = age


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
        self.name = name
        self.owners = []
        self.plants = []
        self.number_of_owners = 0
        self.number_of_plants = 0

    def AddOwner(self, owner: Owner) -> None:
        self.owners.append(owner)
        self.number_of_owners += 1

    def GetNumberOwners(self) -> int:
        return self.number_of_owners

    def AddPlant(self, plant: Plant, owner: Owner) -> None:
        self.plants.append(plant)
        self.number_of_plants += 1
        for self.owner in self.owners:
            if self.owner == Owner:
                Owner.plants.append(Plant)
                Owner.number_of_plants += 1


    # def GardenStats(self) -> None:


    # def create_garden_network(self) -> None:


if __name__ == "__main__":
    My_Garden = GardenManager("My Garden")
    Ronan = Owner("Ronan")
    Jean = Owner("Jean")
    Jacques = Owner("Jacques")
    Lila = Plant("Lila", 10, 5)
    My_Garden.AddOwner(Ronan)
    My_Garden.AddOwner(Jean)
    My_Garden.AddOwner(Jacques)
    My_Garden.AddPlant(Lila, Ronan)
    for My_Garden.owner in My_Garden.owners:
        print(f'{My_Garden.owner}')
        for My_Garden.owners.plants in My_Garden.owners.plants:
            print(f'  --  {My_Garden.owners.plant_name}  --  ')
    print(f'Total gardens managed : {My_Garden.GetNumberOwners()}')
