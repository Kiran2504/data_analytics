#check even odd

# a = int(input("Enter your number: "))
# b = int(input("enter your number: "))


while True:
    c = int(input("Enter your number: "))
    if c % 2 == 0:
        print("Number is even.")
    else:
        print("number is odd.")
    repeat = input("Do you want to stop the program: ")
    if repeat == "yes":
        break
