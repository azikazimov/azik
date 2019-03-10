# from test import print_name as pm
#
# pm('Gregory', 15)

# class Dog():
#     """Простая модель собаки"""
#     def __init__(self, name, age):
#         """Инициализирует атрибуты name & age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Собака садиться"""
#         text = self.name.title() + ' is now sitting'
#         return text
#     def roll(self):
#         """Собака перекатывается"""
#         text = self.name.title() + ' is rolling'
#         return text
#
# my_dog = Dog('whille', 16)
# print('My dog name is ' + my_dog.name.title())
# print('My dog is ' + str(my_dog.age) + ' years old')
#
# text = my_dog.sit()
# print(text)
# _text = my_dog.roll()
# print(_text)

class Car():
    def __init__(self, make, model, year):
        """Init make, model and year"""
        self.make = make
        self.model = model
        self.year = year

    def car_prod(self):
        """Return long_text"""
        long_text = str(self.year) + ' ' + self.make.title() + ' ' + self.model.title()
        return long_text

my_car = Car('audi', 'a8', 1987)
print(my_car.car_prod())
