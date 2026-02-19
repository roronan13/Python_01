class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("-- My garden : --")
    plant_1 = Plant("Rose", 100, 2)
    plant_2 = Plant("Jasmin", 50, 6)
    plant_3 = Plant("Lila", 200, 5)
    