class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("-- My garden --")
    plant_1 = Plant("Rose", 100, 2)
    plant_2 = Plant("Jasmin", 50, 6)
    plant_3 = Plant("Lila", 200, 5)
    print(f'{plant_1.name}: {plant_1.height}cm, {plant_1.age} days old')
    print(f'{plant_2.name}: {plant_2.height}cm, {plant_2.age} days old')
    print(f'{plant_3.name}: {plant_3.height}cm, {plant_3.age} days old')
