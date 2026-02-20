class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, height) -> None:
        if height <= 200 and height >= 1:
            self.__height = height
        else:
            print("This size can't be reached !")

    def get_height(self) -> int:
        return self.__height

    def set_age(self, age) -> None:
        if age <= 50 and age >= 1:
            self.__age = age
        else:
            print("It can't be that age !")

    def get_age(self) -> int:
        return self.__age


if __name__ == "__main__":
    plant1 = Plant("Rose", 10, 5)
    plant2 = Plant("Tulipe", 20, 10)
    plant3 = Plant("Jacinthe", 50, 20)
    plant4 = Plant("Chrysalide", 80, 50)
    plant5 = Plant("Begonia", 100, 300)
