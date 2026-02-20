class Plant:
    def __init__(self, name, strt_h, strt_a) -> None:
        self.name = name
        self.strt_h = strt_h
        self.strt_a = strt_a


if __name__ == "__main__":
    print(" -- Plant factory output -- ")
    plant1 = Plant("Rose", 10, 5)
    plant2 = Plant("Tulipe", 20, 10)
    plant3 = Plant("Jacinthe", 50, 20)
    plant4 = Plant("Chrysalide", 80, 50)
    plant5 = Plant("Begonia", 100, 100)
    print(f'Created : {plant1.name} ({plant1.strt_h}cm, {plant1.strt_a} days)')
    print(f'Created : {plant2.name} ({plant2.strt_h}cm, {plant2.strt_a} days)')
    print(f'Created : {plant3.name} ({plant3.strt_h}cm, {plant3.strt_a} days)')
    print(f'Created : {plant4.name} ({plant4.strt_h}cm, {plant4.strt_a} days)')
    print(f'Created : {plant5.name} ({plant5.strt_h}cm, {plant5.strt_a} days)')
    print("Total plants created : 5")
