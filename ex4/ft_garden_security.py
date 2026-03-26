#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, height: int) -> int:
        if height >= 0:
            self.__height = height
            return 0
        else:
            print("This size can't be reached !")
            return -1

    def set_age(self, age: int) -> int:
        if age >= 0:
            self.__age = age
            return 0
        else:
            print("It can't be that age !")
            return -1

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def secure_plant(self, height: int, age: int) -> int:
        is_valid = 0
        if self.set_height(height) < 0:
            print("Security : wrong height !")
            is_valid = -1
        if self.set_age(age) < 0:
            print("Security : wrong age !")
            is_valid = -1
        return is_valid


if __name__ == "__main__":
    print(" === Garden Security System === \n")
    plant1 = Plant("Rose", -1, -1)
    print(f"{plant1.name} :")
    if plant1.secure_plant(int(input("Height : ")), int(input("Age : "))) >= 0:
        print(f'\nPlant created : {plant1.name}')
        print(f'Height updated : {plant1.get_height()}cm [OK]')
        print(f'Age updated : {plant1.get_age()}days [OK]')
    plant2 = Plant("Lila", -1, -1)
    print(f"\n{plant2.name} :")
    if plant2.secure_plant(int(input("Height : ")), int(input("Age : "))) >= 0:
        print(f'\nPlant created : {plant2.name}')
        print(f'Height updated : {plant2.get_height()}cm [OK]')
        print(f'Age updated : {plant2.get_age()}days [OK]')
    print("\nCurrent plants : ")
    if plant1.get_height() > -1 and plant1.get_age() > -1:
        print(f'{plant1.name} ({plant1.get_height()}cm, '
              f'{plant1.get_age()}days)')
    if plant2.get_height() > -1 and plant2.get_age() > -1:
        print(f'{plant2.name} ({plant2.get_height()}cm, '
              f'{plant2.get_age()}days)')
