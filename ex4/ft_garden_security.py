#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = height if height >= 0 else 0
        self._age = age if age >= 0 else 0

    def set_height(self, height: int):
        if height >= 0:
            self._height = height
            print(f"Height updated : {height}cm")
        else:
            print(f"{self.name} : This size can't be reached !")
            print("Height update rejected")

    def set_age(self, age: int):
        if age >= 0:
            self._age = age
            print(f"Age updated : {age}cm\n")
        else:
            print(f"{self.name} : It can't be that age !")
            print("Age update rejected")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> str:
        return f"{self.name} : {self.get_height()}cm, {self.get_age()} \
days old"


if __name__ == "__main__":
    print(" === Garden Security System === \n")
    Bambou = Plant("Bambou", -50, 40)
    print(f"Plant created : {Bambou.show()}\n")
    Bambou.set_height(100)
    Bambou.set_age(80)
    Bambou.set_height(-100)
    Bambou.set_age(-80)
    print(f"\nCurrent state : {Bambou.show()}")
