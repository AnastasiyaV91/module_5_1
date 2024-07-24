class House:
    def __init__(self, developer, number_of_floors):
        self.developer = developer
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(new_floor + 1):                               # Считаем этажи
            if i == 0:                                               # Нулевое значение пропускаем
                continue                                             # Переходим к следующему значению i
            if new_floor > self.number_of_floors or new_floor < 1:   # Если количество этажей больше, чем в здании
                                                                     # или меньше одного
                print("Такого этажа не существует")                  # выводим в консоль сообщение и выходим из цикла
                break
            else:
                print(i)                                             # Выводим в консоль номер этажа


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)