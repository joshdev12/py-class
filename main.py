# # name = "Vic"

# # print(name)

# # print(dir(name))
# # print()
# # print(type(name))
# # print()
# # print(name.upper())
# # print(len(name))


# # print("my name is {1} {0}".format("Adesanmi", "PG"))

# name = "PraiseGod"

# print(name[6:9])
# a


# """
# ARITHMETIC OP -> //
# COMPARISON OP
# LOGICAL
# MEMBERSHIP



# """


# print(10 % 3)
# print(10 // 3)

# from re import A
# from tkinter import N


# jos = 34

# d = float(jos)
# # x = complex(jos)s

# print(d)
# print("\n")
# a = "Anime, Peace"
# print( a[0:5])
# print(len(a))

# print("\n")
# for u in "island":
#     print(u)


# names = ["Abe", "Vic", "Grandpa", "Check"]
# print("Joshua" not in names)
# print("Jos" in names)



# person = {
#     "name": "Ade",
#     "age": 23,
#     "is_tall": False
# }

# value = person.get("is_tal", None)

# print(value)

# print(type(something))
# print(dir(something))
# print(help(something))





# something = person.items()
# for k, v in something:
#     print("Key: ", k)
#     print("Value: ", v)

# print(type(something))
# print(something)
# print(dir(person))

# FUNCTION IN PYTHON

# def add(x, y):
#     z = x + y
#     return z

# def sayHello(name, age=20):
#     message = f"Good Morning {name}, you're {age} years old!"
#     print(message)


# sayHello("Mariam", 27)


# # print(name())
# result = add(2, 5) # z -> 5

# print(result)

# def factorial(n):
#     result = n
#     temp = n
#     if n == 0:
#         return 1

#     while n > 1:
#         result *= n - 1
#         n -= 1

#     final = result

#     if temp < 0:
#         final *= -1
        
#     return final


def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))

value = factorial(num)
print(value)


