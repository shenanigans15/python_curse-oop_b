class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"{self.name} está durmiendo")


class Dog(Animal):
    def sound(self):
        print(f"{self.name} dice: Guau!")


class Cat(Animal):
    def sound(self):
        print(f"{self.name} dice: Miau!")


firulais = Dog("Firulais")
firulais.sleep()
firulais.sound()

michi = Cat("Michifus")
michi.sleep()
michi.sound()
