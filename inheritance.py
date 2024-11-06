#parent class

class Animal:
    def move ( self):
        print("Animal ss walking")

class Dog(Animal):
     def bark(self):
         print("Dog is barking")

#child class
a = Animal()
d = Dog()

#csalling methods
d.move()
d.bark()