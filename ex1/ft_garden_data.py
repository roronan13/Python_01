class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("-- My garden --")
    plant_1 = Plant("Rose", 100, 2)
    plant_2 = Plant("Jasmin", 50, 6)
    plant_3 = Plant("Lila", 200, 5)
    plant_1.show()
    plant_2.show()
    plant_3.show()
