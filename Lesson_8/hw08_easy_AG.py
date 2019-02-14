# [Андрей Гурьянов]

class MyBuilder:
    def __init__(self, lst_1, lst_2):
        self.keys = lst_1
        self.values = lst_2
        d = dict(zip(self.keys, self.values))
        for key, value in d.items():
            setattr(self, key, value)

class ListWrapper:
    def __init__(self, lst):
        self.lst = lst
    def __getattr__(self, attr):
        return getattr(self.lst, attr)
        

spisok_1 = ['name', 'surname', 'sex', 'position', 'age']
spisok_2 = ['Kventin', 'Tarantino', 'Male', 'Director', '18']
empl = MyBuilder(spisok_1, spisok_2)
print(f'Имя: {empl.name}, Фамилия: {empl.surname}, Пол: {empl.sex}, Должность: {empl.position}, Возраст: {empl.age}')

spisok_3 = ['Albania', 'Armenia', 'Argentina', 'America']
print(spisok_3)
spisok_3.clear()
print(spisok_3)



'''
Задание 1. Реализовать класс-строитель. В его конструктор передать два списка.
Класс должен возвратить python-объект словарь. Проверить, что объект
создается корректно - создать экземпляр класса и обратиться к значению
элемента словаря, как к атрибуту класса.
'''



'''
Задание 2.
Создать класс-обертку для списка. Список передвайте в конструктор класса.
Реализуйте удаление всех элементов из списка через функцию clear.
Но функция должна применяться не к списку, а к экземпляру класса.
Внутри класса должно быть предусмотрено делегирование этой функции методу (clear)
списка.
'''
