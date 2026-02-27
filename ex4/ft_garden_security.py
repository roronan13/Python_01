class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, height) -> int:
        if height <= 200 and height >= 0:
            self.__height = height
            return 0
        else:
            print("This size can't be reached !")
            return -1

    def get_height(self) -> int:
        return self.__height

    def set_age(self, age) -> int:
        if age <= 50 and age >= 0:
            self.__age = age
            return 0
        else:
            print("It can't be that age !")
            return -1

    def get_age(self) -> int:
        return self.__age

    def SecurePlant(self, height, age) -> None:
        self.set_height(self, height)
        self.set_age(self, age)


if __name__ == "__main__":
    plant1 = Plant("Rose", 0, 0)
    plant1.SecurePlant(int(input("Height : ")), int(input("Age : ")))
    print(f'Plant created : {plant1.name}')
