class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.houses_history.append(args[0])  # Добавление названия в историю
        print(cls.houses_history)
        return instance
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor >= 1 and new_floor <= self.number_of_floors:
            print(f"Мы на этаже {new_floor}")
        else:
            print("Нет такого этажа")
    def __len__(self):
            return Home.number_of_floors

    def __str__(self):
            return str(f"Название:{self.name}, Этажей:{self.number_of_floors}")
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if isinstance(value, House):
            return self.number_of_floors + value.number_of_floors
        elif isinstance(value, int):
            return self.number_of_floors + value
        else:
            return print("Невозможно")
    def __radd__(self, value):
        if isinstance(value, House):
            return self.number_of_floors + value.number_of_floors
        elif isinstance(value, int):
            return self.number_of_floors + value
        else:
            return print("Невозможно")
    def __iadd__(self, value):
        if isinstance(value, House):
            return self.number_of_floors + value.number_of_floors
        elif isinstance(value, int):
            return self.number_of_floors + value
        else:
            return print("Невозможно")
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")



Home = House("Скибиди", 21)
h2 = House("Aboba", 11)

print(Home.number_of_floors, Home.name)
Home.go_to(20)
Home.go_to(23)

print(len(Home))
print(Home)

print(Home > h2) # __gt__
 # __ge__
print(Home < h2) # __lt__
 # __le__
print(Home != h2) # __ne__
print(Home + h2)
print(Home + 2)

print(Home)


print(h2)
