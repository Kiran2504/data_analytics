#encapsulation

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # private variable

#     def deposit(self, amount):
#         self.__balance += amount
#         return self.__balance


#Inheritance

# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")

# for animal in [Dog(), Cat()]:
#     animal.sound()

#Polymorpisham

# # Class banayi
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print(f"The name is {name} and mark is {marks}.")
# # Object banaya
# s1 = Student("Kiran", 85)
# s2 = Student("Ravi", 90)

# print(s1.name, s1.marks)  # Kiran 85
# print(s2.name, s2.marks)  # Ravi 90


# # Parent class
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print("Name:", self.name)

# # Child class (inherits Person)
# class Student(Person):
#     def __init__(self, name, marks):
#         super().__init__(name)  # parent init call
#         self.marks = marks

#     def show_marks(self):
#         print("Marks:", self.marks)

# s = Student("Kiran", 90)
# s.show()        # Parent method
# s.show_marks()  # Child method


# class Student:
#     def __init__ (self, name):
#         self.name = name
    
# s1 = Student("kiran")
# print(s1.name)


