class Plant:
    def __init__(self, plant_name: str, height: int, age: int) -> None:
        self.plant_name = plant_name
        self.__height = height
        self.__age = age

    def GetHeight(self) -> int:
        return self.__height
    
    def PrintInfo(self) -> str:
        return (f"- {self.plant_name} : {self.GetHeight()}cm")
    
    def GetSpecificType(self) -> str:
        return ("regular")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, flowered: bool,
                 color: str):
        super().__init__(name, height, age)
        self.flowered = flowered
        self.color = color

    def PrintInfo(self) -> str:
        return (f"- {self.plant_name} : {self.GetHeight()}cm, {self.color} "
                f"flowers {self.PrintFlowered()}")
        
    def PrintFlowered(self) -> str:
        if self.flowered:
            return ("(blooming)")
        else:
            return ("(not blooming)")
        
    def GetSpecificType(self) -> str:
        return ("flowering")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, flowered: bool,
                 color: str, prize: int):
        super().__init__(name, height, age, flowered, color)
        self.prize = prize

    def PrintInfo(self) -> str:
        return (f"- {self.plant_name} : {self.GetHeight()}cm, {self.color} "
                f"flowers {self.PrintFlowered()}, Prize points : {self.prize}")
    
    def GetSpecificType(self) -> str:
        return ("prize")


class Owner:
    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name
        self.plants = []
        self.number_of_plants = 0
        self.regular = 0
        self.flowering = 0
        self.prize = 0

    def PrintSpecificNumber(self) -> str:
        return (f"Plant types : {self.regular} regular, {self.flowering} flowering, {self.prize} prize flowers")


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
        self.specific_type = plant.GetSpecificType()
        for self.owner in self.owners:
            if self.owner == owner:
                owner.plants.append(plant)
                owner.number_of_plants += 1
                if self.specific_type == "regular":
                    owner.regular += 1
                if self.specific_type == "flowering":
                    owner.flowering += 1
                if self.specific_type == "prize":
                    owner.prize += 1
        print(f'Added {plant.plant_name} to {owner.owner_name}\'s garden')


    # def GardenStats(self) -> None:


if __name__ == "__main__":
    My_Garden = GardenManager("My Garden")
    Ronan = Owner("Ronan")
    Jean = Owner("Jean")
    Jacques = Owner("Jacques")
    Lila = Plant("Lila", 10, 5)
    Rose = FloweringPlant("Rose", 20, 10, True, "red")
    Tulipe = PrizeFlower("Tulipe", 50, 50, False, "blue", 10)
    My_Garden.create_garden_network(Ronan)
    My_Garden.create_garden_network(Jean)
    My_Garden.create_garden_network(Jacques)
    My_Garden.AddPlant(Lila, Ronan)
    My_Garden.AddPlant(Rose, Jacques)
    My_Garden.AddPlant(Tulipe, Ronan)
    for owner in My_Garden.owners:
        print(f'\n=== {owner.owner_name}\'s Garden Report ===')
        print("Plants in garden:")
        for plant in owner.plants:
            print(plant.PrintInfo())
        print(owner.PrintSpecificNumber())
    print(f'\nTotal gardens managed : {My_Garden.GetNumberOwners()}')
