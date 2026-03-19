class Plant:
    def __init__(self, plant_name: str, height: int, age: int) -> None:
        self.plant_name = plant_name
        self.__height = height
        self.__age = age

    def GetHeight(self) -> int:
        return self.__height

    def PrintInfo(self) -> str:
        return (f"- {self.plant_name} : {self.GetHeight()}cm")

    @staticmethod
    def GetSpecificType() -> str:
        return ("regular")

    def Grow(self) -> None:
        self.__height += 1

    @staticmethod
    def GetPrizePoints() -> int:
        return 0


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

    @staticmethod
    def GetSpecificType() -> str:
        return ("flowering")

    @staticmethod
    def GetPrizePoints() -> int:
        return 0


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, flowered: bool,
                 color: str, prize: int):
        super().__init__(name, height, age, flowered, color)
        self.prize = prize

    def PrintInfo(self) -> str:
        return (f"- {self.plant_name} : {self.GetHeight()}cm, {self.color} "
                f"flowers {self.PrintFlowered()}, Prize points : {self.prize}")

    @staticmethod
    def GetSpecificType() -> str:
        return ("prize")

    def GetPrizePoints(self) -> int:
        return self.prize


class Owner:
    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name
        self.plants = []
        self.number_of_plants = 0
        self.regular = 0
        self.flowering = 0
        self.prize = 0
        self.total_prize = 0

    def PrintSpecificNumber(self) -> str:
        return (f"Plant types : {self.regular} regular, {self.flowering} "
                f"flowering, {self.prize} prize flowers")

    def PrintReport(self) -> str:
        return (f"\nPlants added : {self.number_of_plants}, Total growth : "
                f"{self.number_of_plants}cm")


class GardenManager:
    plants = []
    owners = []
    number_of_owners = 0
    number_of_plants = 0

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def create_garden_network(cls, owner: Owner) -> None:
        cls.owners.append(owner)
        cls.number_of_owners += 1

    def AddPlant(cls, plant: Plant, owner: Owner) -> None:
        cls.plants.append(plant)
        cls.number_of_plants += 1
        specific_type = plant.GetSpecificType()
        for owners in cls.owners:
            if owners == owner:
                owners.plants.append(plant)
                owners.number_of_plants += 1
                owners.total_prize += plant.GetPrizePoints()
                if specific_type == "regular":
                    owners.regular += 1
                if specific_type == "flowering":
                    owners.flowering += 1
                if specific_type == "prize":
                    owners.prize += 1
        print(f'Added {plant.plant_name} to {owner.owner_name}\'s garden')

    def PrintGrow(cls) -> None:
        for owner in cls.owners:
            print(f"\n{owner.owner_name} is helping all plants grow...")
            for plant in owner.plants:
                print(f"{plant.plant_name} grew 1cm")
                plant.Grow()

    class GardenStats:
        def __init__(self, manager) -> None:
            self.manager = manager

        def HeightTest(self) -> bool:
            is_okay = True
            for plant in self.manager.plants:
                if plant.GetHeight() < 0 or plant.GetHeight() > 100:
                    is_okay = False
            return is_okay

        def PrintPrizes(self) -> None:
            i = 0
            print("Garden scores - ", end="")
            for owner in self.manager.owners:
                if i < self.manager.number_of_owners - 1:
                    print(f"{owner.owner_name}: {owner.total_prize}, ", end="")
                else:
                    print(f"{owner.owner_name}: {owner.total_prize}", end="")
                i += 1
            print("")

        def GetNumberOwners(self) -> int:
            return self.manager.number_of_owners


if __name__ == "__main__":
    My_Garden = GardenManager("My Garden")
    print("=== Garden Management System Demo ===\n")
    Ronan = Owner("Ronan")
    Jean = Owner("Jean")
    Jacques = Owner("Jacques")
    Lila = Plant("Lila", 10, 5)
    Rose = FloweringPlant("Rose", 20, 10, True, "red")
    Tulipe = PrizeFlower("Tulipe", 50, 50, False, "blue", 10)
    Jasmin = FloweringPlant("Jasmin", 90, 80, False, "yellow")
    Oui = PrizeFlower("Oui", 10, 5, True, "grey", 15)
    My_Garden.create_garden_network(Ronan)
    My_Garden.create_garden_network(Jean)
    My_Garden.create_garden_network(Jacques)
    My_Garden.AddPlant(Lila, Ronan)
    My_Garden.AddPlant(Rose, Jacques)
    My_Garden.AddPlant(Tulipe, Ronan)
    My_Garden.AddPlant(Jasmin, Jacques)
    My_Garden.AddPlant(Oui, Jacques)
    My_Garden.PrintGrow()
    for owner in My_Garden.owners:
        print(f'\n    === {owner.owner_name}\'s Garden Report ===')
        print("Plants in garden:")
        for plant in owner.plants:
            print(plant.PrintInfo())
        print(owner.PrintReport())
        print(owner.PrintSpecificNumber())
    Stats = My_Garden.GardenStats(My_Garden)
    print(f"\nHeight validation test : {Stats.HeightTest()}")
    Stats.PrintPrizes()
    print(f'Total gardens managed : {Stats.GetNumberOwners()}')
