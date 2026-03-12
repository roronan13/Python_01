class Plant:
    def __init__(self, plant_name: str, height: int, age: int) -> None:
        self.plant_name = plant_name
        self.__height = height
        self.__age = age

    def GetHeight(self) -> int:
        return self.__height


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, flowered: bool):
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

    def create_garden_network(self, owner: Owner) -> None:
        self.owners.append(owner)
        self.number_of_owners += 1

    def GetNumberOwners(self) -> int:
        return self.number_of_owners

    def AddPlant(self, plant: Plant, owner: Owner) -> None:
        self.plants.append(plant)
        self.number_of_plants += 1
        for self.owner in self.owners:
            if self.owner == owner:
                owner.plants.append(plant)
                owner.number_of_plants += 1
        print(f'Added {plant.plant_name} to {owner.owner_name}\'s garden')


    # def GardenStats(self) -> None:


    # def create_garden_network(self) -> None:


if __name__ == "__main__":
    My_Garden = GardenManager("My Garden")
    Ronan = Owner("Ronan")
    Jean = Owner("Jean")
    Jacques = Owner("Jacques")
    Lila = Plant("Lila", 10, 5)
    Rose = Plant("Rose", 20, 10)
    Tulipe = Plant("Tulipe", 50, 50)
    My_Garden.create_garden_network(Ronan)
    My_Garden.create_garden_network(Jean)
    My_Garden.create_garden_network(Jacques)
    My_Garden.AddPlant(Lila, Ronan)
    My_Garden.AddPlant(Rose, Jacques)
    My_Garden.AddPlant(Tulipe, Ronan)
    for owner in My_Garden.owners:
        print(f'{owner.owner_name}\'s Garden Report')
        print("Plants in garden:")
        for plant in owner.plants:
            print(f'  --  {plant.plant_name}  --  {plant.GetHeight()}cm')
    print(f'Total gardens managed : {My_Garden.GetNumberOwners()}')
