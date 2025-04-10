
# This code checks if the list name has any name starting with 'J' and prints it.
# If no name is found, it prints "No name found".
# names = ["pohn", "pane", "Doe"]

# found = False
# for name in names:
#     if name[0] == 'J':
#         print(name)
#         found = True
#         break
# if not found:
#     print("No name found")

# another way
# names = ["pohn", "aane", "Doe"]

# for name in names:
#     if name.startswith('J'):
#         print(name)
#         break
# else:
#     print("No name found")

# Program that takes input until 5 is entered from user
# guess = None

# while guess != 5:
#     guess = int(input("num : "))
# else:
#     print("You entered 5")


# def increment(number, by):
#     return number + by


# # here by is a keyword argument and it helps to understand the arguement being passed
# # to the function
# print(increment(5, by=2))

# passing variable number of arguments to a function
# when we add aestrisk python will automatically pack the arguments into a tuple
# def multiply(*lists):
#     product = 1
#     for list in lists:
#         product *= list
#     print(product)


# multiply(1, 2, 3, 4, 5)


# Variation of multiple arguments
def user(**User):
    # this will pack the arguments into a dictionary
    # and we can access the values using the keys
    print(User)
    print(User["name"])


user(name="John", age=30, city="New York")
