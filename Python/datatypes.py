#user input

# name = input("Enter your name: ")
# print(name)

#datatypes

# int=(9)
# float=(9.9)

# print(int)
# print(float)

#input for int,string,float, evaluate
# name = (input("Enter your name: "))
# print(name)

# age = int(input("Enter your age: "))
# print(age)

# height = float(input("Enter your height: "))
# print(height)

# eval = eval(input("enter any expression here: "))
# print(eval)

#impicit type conversion
# a = 9
# b = 9.9
# print(type(a))
# print(type(b))

# c = a+b
# print(c)
# print(type(c))

#Explicit type conversion
# a = "9"
# b = 9.9
# print(type(a))
# print(type(b))

# a = float(a)
# print("after conversion" ,type(a))
# c = a+b
# print(c)
# print(type(c))


#swapping two number

# x = 1
# y = 9

# temp = x
# print(temp)

# x = y
# y = temp
# print(x)
# print(y)

# print("The value of x is", x)
# print("The value of y is", y)

# #method 2 

# a = 5
# b = 6

# a,b = b,a
# print(a)
# print(b)

#conversion of floate to intenger

# a = 9.9
# print(a)
# print(type(a))

# a = int(a)
# print("after conversion", type(a))
# print(a)


# #take student details for id card
# name = input("Enter your full name: ")
# age = int(input("Enter your age: "))
# blood_group = input("Enter your blood_group: ")
# classroom = (input("Enter your Classroom: "))
# contact_number = int(input("Enter your Phone Number: "))
# print("Student Identity card")
# print("Student name:",name)
# print("Student age:",age)
# print("Student blood_group:",blood_group)
# print("Student classroom:",classroom)
# print("Phone Number:",contact_number)



#take user input from integer and convert into the float

# a = int(input("Enter your number: "))
# print(a)
# print(type(a))

# a = float(a)
# print("after conversion", a)
# print(type(a))


#Arithamatic operator

# print(1+2) #addition
# print(1-2) #sub
# print(4*2) #multiplication
# print(6%2) #moduls (use for reminder)
# print(8//2) #floor division (quisent not in point)
# print(11/2) #division (in point)
# print(2**2)  #expontation

# #comparision oparator

# print(3>2)
# print(2>6)
# print(2<6)
# print(6<2)
# print(6==6)
# print(6==2)
# print(6!=2)
# print(6!=6)
# print(6>=6)
# print(6>=7)
# print(8<=8)
# print(8<=9)

# #logical operator(and, or, not)

# print(not(3>2 or 3<2))
# print(3>9 or 8<7)
# print(2>1 and 4<7)
# print(not(2>1 and 4<2))

#assignment operator


#identity Operator (is, is not)

# a = 9998
# b = 9998

# print(a is b)
# print(a is not b)

# c = 9998
# d = "9998"

# print(c is d)
# print(c is not d)


#bitwise operator

# print(bin(10))
# print(bin(15))

# #and oper
# print(10 & 8)

# # #or oper
# print(10 | 8)

# #XOR oper
# print(10 ^ 8)

# #zero fill left shift
# print(10>>2)

# #zero fill right shift
# print(10<<2)



#Membership Operator (in , not in)

# a = "Kiran"
# print("a" in a)
# print("s" in a)
# print("n" not in a)
# print("s" not in a)

#conditional statements

#1 if the statement

# marks = 91
# if marks >= 91:
#     print("You win a Prize")
# print("Thank You!!!")

#if-else statement

# speed = 40
# if speed >= 50:
#     print("You are on High speed")
# else:
#     print("you are safe")

# print("Thank You!!!")

#if-elif-else

# car = "BMW"
# if car != "Breza":
#     print("This is BMW")
# elif car != "BMW":
#     print("This is BMW here")
# elif car == "Safari":
#     print("This is BMW")
# else:
#     print("Not my favorite car is here")

# print("thank you sir!!!")


# marks = 50
# if marks >= 90:
#     print("You won a Trip")
# elif marks >= 80 and marks <90:
#     print("you won a phone")
# elif marks >= 70 and marks <80:
#     print("You use a Phone")
# else:
#     print("You not use a phone")

#nestend if statement

# marks = 90
# if marks >= 80:
#     print("we will get a phone")
#     if marks >= 85 and marks <95:
#         print("you will won a trip")
#         if marks >= 95:
#             print("You will won a permanant phone recharge")
# else:
#     print("you not use a phone for a month")

#Short hand if statement

# mark = 97
# if mark >= 97: print("You won the phone")

# #Short hand if-else statement

# mark = 90
# print("You will won a phone") if mark >=90 else print("we will not use a phone for a month")


#Problem solving

#Write a program to check if a number is positive.1
# num = int(input("Enter a number: "))
# if num >= 0:
#     print("Number is positive.")
# else:
#     print("Number is negative.")

#Write a program to check whether a number is odd or even.
# num = int(input("Enter your number: "))
# if num%2==0:
#     print("Number is even.")
# else:
#     print("Number is odd")
#Write a program to create area calculator
# print("                           !!!Area Calculator!!!")
# print("""
# Press 1 to get the area of squre
# Press 2 to get the area of rectangle
# Press 3 to get the area of circle
# Press 4 to get the area of triagnle""")

# choice = int(input("Enter a number between 1 to 4: "))

# if choice == 1:
#     side = float(input("Enter the lenght of the side: "))
#     area = side*side
#     print("The area of the squre", area)

# elif choice == 2:
#     length = float(input("Enter the lenght of rectangle: "))
#     widht = float(input("Enter the widht of rectangle: "))
#     area = length*widht
#     print("The area of the rectangle is", area)

# elif choice == 3:
#     radius = float(input("Enter radius of circle: "))
#     area = ((22/7)*(radius**2))
#     print("Area of the circle ", area)

# elif choice == 4:
#     base = float(input("Enter the base of triangle: "))
#     height = float(input("enter the height of the triangle: "))
#     area = 0.5*base*height
#     print("The area of the triangle", area)

# else:
#     print("Invalid Statement!!!")


# # #Write a program check whether the passed letter is a vowel or not.
# letter = input("Enter your letter: ")
# if letter in "aeiou" or "AEIOU":
#     print("Letter is vowel")
# else:
#     print("letter is not vowel")

# #Write a program to check if a number is a single digit number,
# #2-digit number and so on... up to 5 digits.

# num = int(input("Enter your number upto 5 digit: "))
# if num>=0 and num<=9:
#     print("Number is single digit.")
# elif num>=10 and num<=99:
#     print("number is double digit.")
# elif num>=100 and num<=999:
#     print("number is three digit.")
# elif num>=1000 and num<=9999:
#     print("number is four digit.")
# # elif num>=100000 and num<=999999:
# #     print("number is five digit")
# else:
#     print("number is five digit.")



# Loop in python:

#1) For loop:

# for i in range(1,6):
#     print(i)

# n = int(input("Enter a number here: "))
# for i in range(1,11):
#     print(n,"X",i,"=", n*i)

#2) While loop:

# n = 1
# i = int(input("Enter your number here: "))
# while n<=10:
#     print(i,"X",n,"=",i*n)
#     n +=1

#3) While True:

# while True:
#     print("true")

# while True:
#     num1 = int(input("enter your first number: "))
#     num2 = int(input("enter your second number: "))
#     print(num1+num2)

#     repeat = input("Do you want to stop the program: ")
#     if repeat == "yes":
#         break



# n = 1
# while True:
#     print (n)
#     n +=
    


#Nested Loop:

# for i in range(1,4):
#     for j in range(1,11):
#         print(j, end = "")
#     print()


# for i in range (1,42):
#     for j in range(1, i+1):
#         print(j, end = " ")
#     print()


#for loop with conditional statement

# for i in range(1,11):
#     if i == 3:
#         print("add this song in fave")
#     print(i)


# for i in range (1,101):
#     if i%8 == 0 and i%12 == 0:
#         print(i)
# print("This num divided by 8 and 12")

# for i in range (1,100):
#     if i % 2 == 0:
#         print(i)

#while loop with cs

# n = 0 

# while n <= 10:
#     if n == 3:
#         print("add this in fave.")
#     else:
#         print(n)
#     n +=1


#Break and continue statement


# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)



# for i in range(1,11):
#     if i == 7:
#         break
#     print(i)
# print("This loop is break here!!!")



#Problem Solving

#write a program to find a sum of all the even number upto 50

# sum = 0 

# for i in range(1,51):
#     if i % 2 == 0:
#         sum += i
#         # print(sum)
#     # print(i)
#     # print(sum)

# print("The sum of the all the even number upto 50 is", sum)


#write a program to write a first 20 number and their squred number

# for i in range(1,21):
#     print(i,i**2)

#write a program to find sum of first 10 odd numbers using while loop


# sum = 0
# n = 0
# while n <= 20:
#     if n % 2 != 0:
#         sum += n
#     n += 1
# print("the sum of 1st 10 odd number is", sum)

# count = 1        # how many odd numbers we have added so far
# num = 1          # current odd number
# sum = 0        # to store the sum

# while count <= 10:  # loop runs until 10 odd numbers are added
#     sum += num    # add the current odd number
#     num += 2      # move to the next odd number
#     count += 1    # increase the count

# print("The sum of 1st 10 odd number is", sum)


#write a program to check if number is divisible by 8 and 12 upto 100 numbers

# for i in range(1, 101):
#     if i % 8 == 0 and i % 12 == 0:
#         print(i)
# print("This numbers are divisible by both 8 and 12")

#write a program to create a billing system for supermarket

# while True:
#     name = input("Enter customer name: ")
#     total = 0

#     while True:
#         quntity = float(input("Enter a quntity here: "))
#         amount = float(input("Enter a amount here: "))
#         total += quntity*amount
#         repeat = input("Do you wnat to add more item? (Yes/no): ")
#         if repeat == "no" or repeat == "No":
#             break

#     print("-"*50)
#     print("Name: ", name)
#     print("Amount to be paid: ", total)
#     print("-"*50)
#     print("*********VISIT AGAIN*********")

#     repeat1 = input("Do you want to go next customer? (Yes/No): ")
#     if repeat1 == "no" or repeat1 == "No":
#         break


# A = "Why fit in, When you are Born to Stand Out!"
# # 1. Write a program to find the length of the following string.

# print(len(A))


# # 2. Write a program to check how many time alphabet o is occurring.

# print(A.count("o"))
# # 3. Write a program to convert the whole string into lower and upper cases.

# b = A.upper()
# print(b)

# c = A.lower()
# print(c)
# # 4. Write a program to convert the following string into a title.
# d = A.title()
# print(d)
# # 5. Write a program to find the index number of "fit in".

# print(A.find("fit in"))



#Problem Solvong on logical 

#1)
# for i in range(1,6):          #rows
#     for j in range(1,i-1):    #column
#         print(j, end=" ")
#     print()


# #2)
# for i in range(1,6):          #rows
#     for j in range(1,i+1):    #column
#         print(i, end=" ")
#     print()


# #3)
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print(i, end=" ")
#     print()

#4)
# for i in range(1,6):
#     for j in range(5,i,-1):
#         print(" ", end=" ")
#     for k in range (i):
#         print("*", end=" ")
#     print()

# #5)
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()

#6)
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()
# for i in range(5,0,-1):
#     for k in range(0,i-1):
#         print("*", end=" ")
#     print()


# #7)
# for i in range(1,11):
#     for j in range(1,i+1):
#         print(i*j, end = " ")
#     print()







#SRING MANIPULATION

# a = "hello word"
# print(type(a))
# print(a.index("llo"))
# print(a.upper())
# print(a.lower())
# print(len(a))
# print(a.count("l"))
# print(a.capitalize())
# print(a.find("w"))

# name = "Kiran"
# a = 'my name is {}'
# print(a.format(name))
# print(name.center(100, "_"))


#or many function


# a = "hello"
# b= "123Hello"
# c = "123456"
# d = "HELLO"
# e = " "
# f = "Hello 123"
# g = "1.234"
# #isalnum -Returns True if all characters in the string are alphanumeric
# print(a, a.isalnum())
# print(b, b.isalnum())
# print(c, c.isalnum())
# print(d, d.isalnum())
# print(e, e.isalnum())
# print(f, f.isalnum())
# print(g, g.isalnum())
# print("*"*40)
# #isalpha Returns True if all characters in the string are in the alphabet
# print(a, a.isalpha())
# print(b, b.isalpha())
# print(c, c.isalpha())
# print(d, d.isalpha())
# print(e, e.isalpha())
# print(f, f.isalpha())
# print(g, g.isalpha())
#isdecimal Returns True if all characters in the string are decimals
#isdigit -Returns True if all characters in the string are digits
#isnumeric -Returns True if all characters in the string are numeric
#islower -Converts a string into lower case
#isupper Returns True if all characters in the string are upper case
#isspace -Returns True if all characters in the string are whitespaces
#istitle -Returns True if the string follows the rules of a title



# capitalize() – Capitalizes first character of string.

# casefold() – Lowercases string more aggressively (for caseless matching).
# a = "kiran Is A boy"
# print(a.casefold())

# center(width, fillchar) – Returns a centered string.
# l = "Kiran is bad boy"
# print(l.center())
# count(substring) – Counts occurrences of a substring.

# encode() – Returns encoded version of string.

# endswith(suffix) – Checks if string ends with suffix.

# expandtabs(tabsize) – Replaces tabs with spaces.

# find(substring) – Returns lowest index of substring, else -1.

# format() – Formats string.

# format_map(mapping) – Formats string using a dictionary.

# index(substring) – Like find() but raises error if not found.

# isalnum() – True if all characters are alphanumeric.

# isalpha() – True if all characters are alphabetic.

# isascii() – True if all characters are ASCII.

# isdecimal() – True if all characters are decimal numbers.

# isdigit() – True if all characters are digits.

# isidentifier() – True if string is a valid Python identifier.

# islower() – True if all characters are lowercase.

# isnumeric() – True if all characters are numeric.

# isprintable() – True if all characters are printable.

# isspace() – True if string contains only whitespace.

# istitle() – True if string is title-cased.

# isupper() – True if all characters are uppercase.

# join(iterable) – Joins elements of iterable with the string.

# ljust(width, fillchar) – Left-justifies string.

# lower() – Converts to lowercase.

# lstrip() – Removes leading whitespace/characters.

# maketrans() – Returns translation table for translate().

# partition(sep) – Splits into 3 parts (before, sep, after).

# removeprefix(prefix) – Removes prefix if present.

# removesuffix(suffix) – Removes suffix if present.

# replace(old, new) – Replaces substring.

# rfind(substring) – Returns highest index of substring.

# rindex(substring) – Like rfind() but raises error if not found.

# rjust(width, fillchar) – Right-justifies string.

# rpartition(sep) – Like partition() but from right side.

# rsplit(sep, maxsplit) – Splits from right.

# rstrip() – Removes trailing whitespace/characters.

# split(sep, maxsplit) – Splits into list.

# splitlines() – Splits by line breaks.

# startswith(prefix) – Checks if string starts with prefix.

# strip() – Removes leading/trailing whitespace/characters.

# swapcase() – Swaps case (upper <-> lower).

# title() – Converts string to title case.

# translate(table) – Translates using maketrans() table.

# upper() – Converts to uppercase.

# zfill(width) – Pads string with zeros on the left.



#slicing in string

# a = "Now focus on the your goal."

# print(a)
# print(a[0:4])
# print(a[4:9])
# print(a[:4]) # FROM THE STARTING VALUE
# print(a[6:8])
# print(a[-5:])
# print(a[6::-1])  #negative 
# print(a[::2]) #2 gap per number
# print(a[::-1])


# 1. Write a program to get Fibonacci series up to 10 numbers.
# a = 0
# b = 1
# n = int(input("enter number here: "))
# if n == 1:
#     print(1)

# else:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c = a + b
#         a = b
#         b = c
#         print(c)



# 2. Write a program to check if a number is prime or not.

# num = int(input("enter your number: "))

# if num <= 1:
#     print("It is not a prime number.")
# else:
#     for i in range(2,num):
#         if num % i == 0:
#             print("It is not a prime number.")
#             break

#         else:
#             print("It is a prime number.")



# 3. Write a program to find a palindrome of integers.
#palindrome numbre means number is same both side




# # 4. Write a program to create an area calculator.

# print("                           !!!Area Calculator!!!")
# while True:
#     print("""
#     Press 1 to get the area of squre
#     Press 2 to get the area of rectangle
#     Press 3 to get the area of circle
#     Press 4 to get the area of triagnle""")

#     choice = int(input("Enter a number between 1 to 4: "))

#     if choice == 1:
#         while True:
#             side = float(input("Enter the lenght of the side: "))
#             area = side*side
#             print("The area of the squre", area)

#             repeat = input("Dp you wnat to repaet for squre?")
#             if repeat == "no":
#                 break

#     elif choice == 2:
#         while True:
#             length = float(input("Enter the lenght of rectangle: "))
#             widht = float(input("Enter the widht of rectangle: "))
#             area = length*widht
#             print("The area of the rectangle is", area)

#             repeat = input("Dp you wnat to repaet for rectangle?")
#             if repeat == "no":
#                 break


#     elif choice == 3:
#         while True:
#             radius = float(input("Enter radius of circle: "))
#             area = ((22/7)*(radius**2))
#             print("Area of the circle ", area)

#             repeat = input("Dp you wnat to repaet for circle?")
#             if repeat == "no":
#                 break

#     elif choice == 4:
#         while True:
#             base = float(input("Enter the base of triangle: "))
#             height = float(input("enter the height of the triangle: "))
#             area = 0.5*base*height
#             print("The area of the triangle", area)

#             repeat = input("Dp you wnat to repaet for triangle?")
#             if repeat == "no":
#                 break

#     else:
#         print("Invalid Statement!!!")
    
#     repeat1 = input("Do you want repaet a menu? ")
#     if repeat1 == "no":
#         break



#lists 
#lists slicing:

# a = ["Ironman", "Thor", "Captain America", "Hulk"]
# # print (a[1])
# # print (a[1:3])
# # print (a[:2])
# # print (a[1:])
# # print (a[::2])
# print (a[-3:-1])
# print (a[::-1])



# lists iteration


# a = ["Ironman","captain america", "Thor", "Hulk"]
# print(a)
# a.append("starloard")
# print(a)





#Tuples

# a = "Ironman", "captain america", "thor", "hulk", 1, 4, 5 
# print(type(a))
# print(a)
# a.append("Steve")    # it does not have any attribute to edit the tuple
# print(a)

#slicing in tuple

# a = ("vivo", "apple", "redmi", "samsung", "onplus", "releme")
# print(type(a))

# print(a[1:4])
# print(a[:4])
# print(a[0:])
# print(a[::2])
# print(a[1::2])
# print(a[-1:])
# print(a[::-1])
# print(a[-2::-2])
# print(a[3::-1])


# a = ("vivo", "apple", "redmi", "samsung", "onplus", "releme")

# # using loop slicing

# #with for loop
# # for i in a:
# #     print(i)

# # #with while loop

# # i = 0 
# # while i < len(a):
# #     print(a)
# #     i+=1


# #conversion of tuples and tuples function

# z = ("BMW", "ODI", "TESLA", "MRUTI", "SUZUKI", "RR")

# print("before conversion type", type(z))

# z = list(z)
# print("After conversion", type(z))
# z.append("Tata")
# print(z)

# z = tuple(z)
# print("After adding convert in tuple", type(z))

# print(z.count(""))

# print(z.index("TESLA"))



#Problem solving


# 1. Convert the following dictionary into JSON format.

# import json
# Student_data = {"name": "David", "age":13, "marks":87}
# print(type(Student_data))
# data = json.dumps(Student_data)
# print(data)
# print(type(data))



# 2. Access the value of age from the given data.
# import json
# Student_data = """{"name": "David", "age":13, "marks":87}"""
# data = json.loads(Student_data)
# print(data["age"])


# 3. Pretty Print following JSON data.
# Student_data = {"name": "David", "age":13, "marks":87}




# # 4. Sort the following JSON keys and write them into a file.
# # Student data = {"name": "David", "age":13, "marks":8


# #Introduction to dictionaries

# school = {"name":"Kiran", "rollnumber":"4", "age":"21", "gender":"Male"}
# print(school)
# print(school["name"])
# print(school["gender"])


#Iteration in dictionaries

#Iteration in Dictionaries
Student={"name":"John","class":"6th", "roll_no":23}

#printing all the key names one by one

# for x in Student:
#     print(x)

#printing all the value names one by one

# for x in Student:
#     print(Student[x])


#using value function
# for x in Student.values():
#     print(x)


# #using item function
# for x,y in Student.items():
#     print(x,"-", y)


#nested dictinories

# students = {
#     "student1": {"name": "Alice", "age": 20},
#     "student2": {"name": "Bob", "age": 22},
#     "student3": {"name": "Charlie", "age": 19}
# }
# print(students["student1"])
# print(students["student2"]["name"])


# Write a python program to sort a dictionary by value.
# a = {"a":12,"b":23,"c":6,"d":91,"e":45}
# a = sorted(a.values())
# print(a)

# Write a python script to print a dictionary
# where the keys are numbers between 1 and 15 and the # values are square of keys.

# a = {}
# for i in range(1,16):
#     a[i] = i**2
    
# print(a)


# # Write a program to multiply all the items in a dictionar
# a = {"a":12,"b":23,"c":6,"d":91,"e":45}

# product = 1
# for i in a:
#     product *= a[i]

# print(product)


#Sets

# a = {"Kiran", "Ram", "Om", "Sham", "lakhan"}
# print(a)
# print(type(a))
# for x in a:               #iteration i sets
#     print(x)

# #Function in sets

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# print(a.union(b))

# a.add(10)
# print(a)

# a.remove(10)
# print(a)    # Error if not found
# a.discard(20)   # No error if not found

# print(a.pop())

# a.clear()
# print(a)   # set()

# c = {9, 10}
# print(a.isdisjoint(c))   # True

# print(a.issuperset(b))   # True

# x = {1, 2}
# print(x.issubset(a))   # True


# #Function

# def hello():
#     print("hello world")
# hello()


# def add():
#     x = 2
#     y = 4
#     print(x + y)
# add()


# #Parameters and arguments
# def add(x,y):
#     print(x + y)
# add(2,4)

# #arbitary arguments

# def king(*name):
#     print("my name is", name[0])
# king("Kiran", "Om", "Sham")


#return function

# def add(a,b):
#     return "The addition of two number is", a + b
# print(add(12,11))


#recursion function




# #lambda function

# a = lambda b : b*5
# print(a(3))

# c = lambda x,y,z : (x*y)+z
# # print(c)

#local and global variable

# x = 2
# print("variable x is", x)
# def hello():
#     x = 1
#     return x
# print(hello())

# print(x)


#global variable

# x = 2
# print("variable x is", x)
# def hello():
#     global
#     x = 1
#     return x
# print(hello())

# print(x)



# def create_list():
#     l = []
#     for i in range(1,31):
#         l.append(i**2)
#     return l
# print(create_list())



# squares = create_list()
# print(squares)

# squares = create_list()
# print("Sum of squares:", sum(squares))





#Modules

# import datetime

# # x = datetime.datetime.now()
# # print(x)

# y = datetime.datetime(2025,5,6)
# print(y)
# print(y.strftime("%y,%m,%M,%Y,%a,%A"))


# import random

# x = random.randint(1,10)
# print(x)


import math

x = max(99,88,77)
print("The maximim valeu is",x)

x = min(99,88,77)
print("The minimum valeu is",x)

a = pow(2,4)
print(a)

b = math.sqrt(49)
print(b)

c = abs(-79898)
print(c)