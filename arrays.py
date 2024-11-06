courses = ["MIT","Cybersecurity","datascience"]
print(courses)

#Accessing an element in array
print(courses[1])

#looping through an element
for  y in courses:
    print("courses is",y)

#Adding a new element
courses.append("web Development")
print(courses)

#deleting an element
courses.remove("MIT")
print(courses)