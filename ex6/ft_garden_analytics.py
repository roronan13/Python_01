class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.__height = height
        self.__age = age


class GardenManager():
    def __init__(self, owner: str, total_gardens: int = 0) -> None:
        self.owner = owner
        self.total_gardens += 1

    def GardenStats(self) -> None:

    def create_garden_network(self) -> None:


if __name__ == "__main__":
    