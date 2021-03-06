'''
Задание_1. Создать класс. В конструктор передать два параметра - два числа.
Создать второй класс. В конструкторе первого предусмотреть создание
объекта второго класса. Кроме того, в первом классе предусмотреть три метода,
в которых делегировать получение остатка от деления, результата деления и целой
части от деления в методы второго класса (предусмотреть вычисление в соотв. методах
второго класса).
'''
# [Андрей Гурьянов]

class MyClass1: # Создаём класс
    def __init__(self, num_1, num_2):  # В конструктор передаём два параметра - два числа
        self.num_1 = num_1
        self.num_2 = num_2
        self.data = MyClass2(self.num_1, self.num_2) #Создаём объект второго класса

    def ostatok(self): # Метод для получения остатка от деления 
        return self.data.mod # делегируем операцию не существующему методу mod класса MyClass2
    
    def __str__(self):
        print(self.num_1, self.num_2)

class MyClass2: # Создаём второй класс
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2 

    def __getattr__(self, attr): # перехватываем атрибут (есуществующий метод mod)
        print(attr)
        return getattr(self.data, attr)
# К сожалению, дальше сообразить не могу - как правильно перехватить атрибут и выполнить неоьходимые операции...



numbers = MyClass1(5, 3)
print(numbers.ostatok)
