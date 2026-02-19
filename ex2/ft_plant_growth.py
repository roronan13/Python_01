class Plant:
    def __init__(self, name, height, plant_age) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self, days) -> None:
        self.height += days

    def age(self, days) -> None:
        self.plant_age += days

    def get_info(self, days) -> None:
        print(f'Growth these last {days} days : +{days}cm')


if __name__ == "__main__":
    print(" -- Day 1 -- ")
    plant_1 = Plant("Rose", 100, 2)
    plant_2 = Plant("Jasmin", 50, 6)
    plant_3 = Plant("Lila", 200, 5)
    print(f'{plant_1.name}: {plant_1.height}cm, {plant_1.plant_age} days old')
    print(f'{plant_2.name}: {plant_2.height}cm, {plant_2.plant_age} days old')
    print(f'{plant_3.name}: {plant_3.height}cm, {plant_3.plant_age} days old')
    days = int(input("How many days spent ? "))
    plant_1.grow(days)
    plant_1.age(days)
    plant_2.grow(days)
    plant_2.age(days)
    plant_3.grow(days)
    plant_3.age(days)
    print(f' -- Day {days + 1} -- ')
    print(f'{plant_1.name}: {plant_1.height}cm, {plant_1.plant_age} days old')
    print(f'{plant_2.name}: {plant_2.height}cm, {plant_2.plant_age} days old')
    print(f'{plant_3.name}: {plant_3.height}cm, {plant_3.plant_age} days old')
    plant_1.get_info(days)
