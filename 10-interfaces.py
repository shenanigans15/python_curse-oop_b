from abc import ABC, abstractmethod


# Clase abstracta
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof woof!"

    def sleep(self):
        return "Zzz..."


class Cat(Animal):
    def sound(self):
        return "Meow meow!"

    def sleep(self):
        return "Zzz..."


taquito = Dog()
minino = Cat()
print(taquito.sound())
print(taquito.sleep())
print(minino.sound())
print(minino.sleep())
