# class Dog:
#     # instantiates the objects
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # # def bark(self):
#     # #     print("bark")
#     # #
#     # # def add_one(self, x):
#     #     return x + 1
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         self.age = age
#
#
# d = Dog("Max", 10)
# # print(type(d))
# print(d.get_age())
# d.set_age(20)
# print(d.get_age())


# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade # 0 - 100
#
#     def get_grade(self):
#         return self.grade
#
# class Course:
#     def __init__(self, name, max_students):
#         self.name=name
#         self.max_students = max_students
#         self.students = []
#
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)
#
#
# s1 = Student("Max", 15, 100)
# s2 = Student("Bill", 16, 50)
# s3 = Student("sj", 15, 67)
#
# course = Course("Math", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.add_student(s3))
# print(course.get_average_grade())

# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old")
#
#     def speak(self):
#         print("I don't know what to say")
#
# class Cat(Pet): # inherits the Pet class
#     def __init__(self, name, age, color):
#         super().__init__(name, age) # super is the class we inherited from
#         self.color = color
#
#     def speak(self): # overides the parent class's speak method
#         print("Meow")
#
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
#
#
# class Dog(Pet): # inherits the Pet class
#     def speak(self):
#         print("Woof")

# p = Pet("Max", 10)
# p.show()
# p.speak()
# c = Cat("Steve", 5, "brown")
# c.show()
# c.speak()
#d = Dog("Jill", 25)
# d.show()
# d.speak()

# class Person:
#     number_of_people = 0
#
#     def __init__(self, name):
#         self.name = name
#         Person.add_person()
#
#     @classmethod
#     def number_of_people_(cls): #not going be called with an object. Called on the class itself, Person
#         return cls.number_of_people
#
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1
#
# p1 = Person("Max")
# p2 = Person("Bob")

class Math:

    @staticmethod # not changing; has no access to the object. Call the class itself to access the method
    def add5(x):
       return x + 5



print(Math.add5(5))