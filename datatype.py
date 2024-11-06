
number = 67  #interger#
second = 45.98 #float
greetings = "Hello there" #string
isPthonInteresting = True #Boolean

#Data structures-Multiple values stored in a single variable
cars = ["toyota","nissan","vw"] #list-Ordered and changeable
fruits = ("banana","apple","mango") #ordered but unchangeable
countries = {"Kenya","Tunisia","Algeria"} #set -elements are unordered and unchangeable
student = {
    "firstname" : "jane",
    "age" : 25,
    "course":"web Development",
    "gender" :"female",

}#dictionary - key-value pair

print(cars)
print(fruits)
print(countries)
print(student)
print(student["gender"])


print(number)
print(second)
print(isPthonInteresting)

#determining a datatype
print(type(countries))
print(type(student))

#Typecasting - converting from one data type to another
print(float(number))
print(int(second))
