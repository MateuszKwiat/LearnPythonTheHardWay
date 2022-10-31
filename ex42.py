class Animal(object):
    pass

# is_a
class Dog(Animal):

    def __init__(self, name):
        #has_a
        self.name = name

#is_a
class Cat(Animal):
    def __init__(self, name):
        #has_a
        self.name = name

#is_a
class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None

#is_a
class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        #has_a
        self.salary = salary

#is_a
class Fish(object):
    pass

#is_a
class Salmon(Fish):
    pass

#is_a
class Halibut(Fish):
    pass

rover = Dog("Rover")

#is_a
satan = Cat("Satan")

#is_a
mary = Person("Mary")

#has_a
mary.pet = satan

#is_a
frank = Employee("Frank", 120000)

#has_a
frank.pet = rover

#is_a
flipper = Fish()

#is_a
crouse = Salmon()

#is_a
harry = Halibut()


