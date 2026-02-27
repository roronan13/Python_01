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

    def SecurePlant(self, height, age) -> int:
        if self.set_height(height) < 0:
            print("Security : wrong height !")
            return -1
        if self.set_age(age) < 0:
            print("Security : wrong age !")
            return -1
        return 0


if __name__ == "__main__":
    plant1 = Plant("Rose", -1, -1)
    if plant1.SecurePlant(int(input("Height : ")), int(input("Age : "))) >= 0:
        print(f'Plant created : {plant1.name}')
        print(f'Height updated : {plant1.get_height()}cm [OK]')
        print(f'Age updated : {plant1.get_age()}days [OK]')
    plant2 = Plant("Lila", -1, -1)
    if plant2.SecurePlant(int(input("Height : ")), int(input("Age : "))) >= 0:
        print(f'Plant created : {plant2.name}')
        print(f'Height updated : {plant2.get_height()}cm [OK]')
        print(f'Age updated : {plant2.get_age()}days [OK]')
    print("Current plants : ")
    if plant1.get_height() > -1 and plant1.get_age() > -1:
        print(f'{plant1.name} ({plant1.get_height()}cm, {plant1.get_age()}days)')
    if plant2.get_height() > -1 and plant2.get_age() > -1:
        print(f'{plant2.name} ({plant2.get_height()}cm, {plant2.get_age()}days)')
