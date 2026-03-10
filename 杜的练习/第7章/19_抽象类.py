from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print('汪汪汪！')


class Cat(Animal):
    def speak(self):
        print('喵喵喵！')


d1 = Dog()
c1 = Cat()
d1.speak()
c1.speak()
