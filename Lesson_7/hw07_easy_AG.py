# [Андрей Гурьянов]

'''
Задача-1: Реализовать индексацию элементов списка не с нуля, а с 5, т.е. 5, 6, 7
и т.д.
'''
class MyList(list):
    def __getitem__(self, start):
        # Изменяем индексацию
        return list.__getitem__(self, start-5)

    
print('\n\nЗадача 1\n')
lst = MyList([32, 23, 65, 34, 654, 12, 7, 56, 43, 6, 34, 2, 7])
print(lst)
for el in lst:
    print(el)
print(lst[5])



'''
Задача-2: Придумать любу структуру данных. Она должна содержать два атрибута.
Значение одного атрибута передается в конструктор, а значение другого - определяетсяъ
прямо в конструкторе класса. Для этой структуры данных написать метод,
который должен выполнять какой-то функционал. Создать экземпляр класса, передать
данные. Вызывать метод. Проверить, что находится в переменной-экземпляре класса.
Переопределить метод __str__. Этот метод должен возвращать тот результат,
который вы захотите. Проверить еще раз. В комментарии написать, в чем разница
между подходом с использованием метода __str__ и без него.
'''
print('\n\nЗадача 2\n')
class MyData:
    def __init__(self, name):
        self.name = name
        self.company = 'Рога и копыта'
    def __str__(self):
        # без переопределения данного метода при выполнении print будет печататься тип объекта и его адрес (ссылка)
        return f'Имя: {self.name}, Компания: {self.company}'
    def add(self, value):
        # добавляет значение значение value к 1-ому атрибуту
        self.name = self.name + '-' + value

    @staticmethod
    def company_change(new_comp):
        # меняем значение  
        return 'Новая контора - ' + new_comp[:3] + '-' + new_comp[2:]
        
        

person1 = MyData('Немирович')
person2 = MyData('Бонч')
person1.add('Данченко')
person2.add('Бруевич')
print(person1)
print(person2)

new_company = person1.company_change('Ромашка')
print(new_company)


'''
Задача-3: Продолжить работу над задачей 2. Добавить еще один метод. Он должен
вывзваться из экземпляра класса. В этот метод нужно передать некое значение.
Сам метод должен ловить значение и что-то с ним делать и возвращать результат.
Реализовать для этого метода декоратор @staticmethod
'''



