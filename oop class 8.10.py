# class Person:
# # =заглушка=
# #     pass
# # создаем конструктор
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# # он будет вызываться при каждом создании объекта класса
#
# person1 = Person(name='EDI',age=22)
# # мы создали объект (условно) он создан по шаблону класса Person, ему присвоен уникальный адрес
# print(f'{person1.name}: {person1.age}')



# практика
# class Automobile:
#
#     def __init__(self,label,price):
#         self.label=label
#         self.price=price

#     def drive(self):
#         print(f'{self.label} поехала')
#
# auto=[]
# auto.append(Automobile(label='dodge',price='33000'))
# auto.append(Automobile(label='maybach',price='103000'))
# auto.append(Automobile(label='bmw',price='53000'))
# auto.append(Automobile(label='toyota',price='43000'))
# auto.append(Automobile(label='lada',price='3000'))
#
# for i in auto:
#     i.drive()



# auto1=Automobile(label='dodge',price=33000)
# auto2=Automobile(label='maybach',price=120000)

# print(f'{auto1.label}: {auto1.price}')
# print(f'{auto2.label}: {auto2.price}')

# чтобы не дублировать код с принтом:
# def show(self):
#     print(f'label: {self.label}, price: {self.price}')
# show(auto1)


class  Human:

    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def show(self):
        print(f'имя:{self.name},'
              f'возраст:{self.__age}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age<0 or age>150:
            raise ValueError('некорректное значение')
        self.__age=age

hum1=Human('petr',23)
hum2=Human('masha',160)
print(hum1.show())
try:
    hum1.age=-3
except ValueError as ex:
    print(ex)
print(hum1.show())