# №1
class Animal:

    def __init__(self, name: str, species: str):
        self._name = name
        self._species = species

    def make_sound(self):
        print("Animal Sound")


class Dog(Animal):

    def __init__(self, name: str, species: str):
        Animal.__init__(self, name, species)

    def make_sound(self):
        print("Woof")


class Cat(Animal):

    def __init__(self, name: str, species: str):
        Animal.__init__(self, name, species)


    def make_sound(self):
        print("Meow")



class Bird(Animal):

    def __init__(self, name: str, species: str):
        Animal.__init__(self, name, species)



    def make_sound(self):
        print("tweet")




# №2
class Person:

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age


    def introduce_yourself(self):
        print(f"меня зовут - {self._name}\n"
              f"мой возраст состовляет - {self._age}")




class Doctor(Person):

    def __init__(self, name: str, age: int, experience:
                int, post, taken_patient: int ):

        self._experience = experience
        self._post = post
        self._taken_patient = taken_patient
        Person.__init__(self, name, age)


    def introduce_yourself(self):

        Person.introduce_yourself(self)
        print(f"стаж - {self._experience}\n"
              f"должность - {self._post}\n"
              f"принятых пациентов - {self._taken_patient}")





class Engineer(Person):

    def __init__(self, name: str, age: int, post: str,
                 experience: int, fix_machine: int):

        self._post = post
        self._experience = experience
        self._fix_machine = fix_machine
        Person.__init__(self, name, age)



    def introduce_yourself(self):

        Person.introduce_yourself(self)
        print(f"должность - {self._post}\n"
              f"стаж - {self._experience}\n"
              f"починеные машины - {self._fix_machine}")




class Artist:

    def __init__(self, name: str, age: int, post: str,
                 experience: int, success_performance: int):

        self._post = post
        self._experience = experience
        self._success_perfomance = success_performance
        Person.__init__(self, name, age)



    def introduce_yourself(self):

        Person.introduce_yourself(self)
        print(f"должность - {self._post}\n"
              f"стаж - {self._experience}\n"
              f"успешные выступления - {self._success_perfomance}")











# №3
class Vehicle:
    pass

class Car(Vehicle):
    pass

class Train(Vehicle):
    pass

class Express(Vehicle):
    pass









# №4

class Animal:
    pass


class Mammals(Animal):
    pass

class Dog(Mammals):
    pass

class Cat(Mammals):
    pass


class Fish(Animal):
    pass


class Shark(Fish):
    pass

class Carp(Fish):
    pass





class Programm:

    @staticmethod

    def main():
        dog = Dog("Bob", "dog")
        cat = Cat("Barsik", "cat")
        bird = Bird("Kesha", "bird")

        dog.make_sound()
        cat.make_sound()
        bird.make_sound()


        doctor = Doctor("Oleg", 50, 29, "doctor", 1000)
        enginerr = Engineer("Valera", 40, "enginer", 20, 100)
        atrist = Artist("Vasa", 20, "artist", 5, 10)

        doctor.introduce_yourself()
        enginerr.introduce_yourself()
        atrist.introduce_yourself()



Programm.main()



