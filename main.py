class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.nuber_of_floors = number_of_floors

    def go_to(self,new_floor):
        if new_floor > self.nuber_of_floors or new_floor < 1:
            print("Такого этажа не существует.")
        else:
            for new_floor in range(new_floor + 1):
                if new_floor < 1:
                    continue
                print(new_floor)
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.nuber_of_floors}'

    def __len__(self):
        return self.nuber_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))