from datatype import student


class Person:
    #properties/variable/Attribute/Characteristics
    def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

#Behaviour/method/Function
def study(self):
    print("student is studying")











    #creating an object

student1 = Person("hussein",23,"male")

student2 = Person("alex",21,"male")
print(student1.name,student1.age,student1.gender)

student3 = Person("beatrice",25,"female")
