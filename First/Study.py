# # Truthy and Falsy -> basically is that a value can be true or false
# is_old = bool("hi")
# is_licenced = bool(2)
# print (bool(""))
# print (bool(134))

# a = True 
# b = "yes sir" if a else "no sir"
# print(b) 

# a = int(input("press 1 if the person is permitted\nor 2 if is not = "))
# if a == 1:
#     a = True
# else:
#     a = False
# permitted = a
# message = "welcome " if a else "get out "
# print(message) 

# is_magician = False
# is_expert = False
# if is_magician and is_expert:
#     print("You are a master magician")
# elif is_magician and not is_expert:
#     print("at least you're getting there")
# else :
#     print("you're not a magician")

# difference among is and ==  -> 
# The == operator checks if two variables have the same value.
# It doesn’t care if they are the exact same object in memory;
# it only checks if the contents are equivalent.

# The is operator checks if two variables refer to the exact same object in memory.
# It’s a check for object identity, not just value equality.

# FOR
# for item in ["leo", "vane", "juli"]:
#     for side in ["you are in the best family", "we love you" , "you are great"]:
#         print(f"hello {item} {side}")

# user = {'name': 'Leo', 'age': 29, 'skill': 'plays the piano'}
# for person in user.items():
#     print(f'so this is your info: {person}')
    
# user = {'name': 'Leo', 'age': 29, 'skill': 'plays the piano'}
# for person in user.values():
#     print(f'so this is your info: {person}')    
    
# user = {'name': 'Leo', 'age': 29, 'skill': 'plays the piano'}
# for person in user.keys():
#     print(f'so this is your info: {person}')    
    
# user = {'name': 'Leo', 'age': 29, 'skill': 'plays the piano'}
# # In here is possible to use k(instead of key) and v(instead of value)
# for k, v in user.items():
#     print(f'so this is your info: {k}= {v}')   

# my_list = [1,2,3,4,5,6,7,8,9,10]
# n = 0
# sum = 0
# for count in my_list:
#     print(f'this number = {my_list[n]}')
#     n += 1
#     sum = sum + count
# print (f'this is the sum of all numbers= {sum}')

# RANGE
# for number in range(50,10,-1):
#     print (number) 

# ENUMERATE
# for num in enumerate('hey dude'):
#     print(num)

# ENUMERATE AND RANGE
# for i, char in enumerate(list(range(100))):
#     if char == 50:
#         print("your number index is: ", i)

# WHILE
# i = 0
# while i < 50:
#     print(i)
#     i += 2
# else:
#     print("we're finished")

# my_list = [1,2,3]
# for item in my_list:
#     print(item) 
    
# i = 0
# while i< len(my_list):
#     print(my_list[i])
#     i += 1

# my_list = [1,2,3]
# i = 0
# while i< len(my_list):
#     print(my_list[i])
#     i += 1
#     continue
# print("we're finished")

# MATRIX
# matrix = [
#   [1,5,1],
#   [0,1,0],
#   [1,0,1]
# ]
# print(matrix[0][1])

# CHRISTAMAS TREE
#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'.
#This will reveal an image!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
# for image in picture:
#   for pixel in image:
    # if pixel == 1:
# end joins the previous line with the following in order to have a straight row
# instead of saying  "hello"
#                    "leo"
# You may say, "hello" "Leo"
  #     print('o', end ="")
  #   else:
  #     print(' ', end ="")
  # print('')



# My method
# l = 0
# c = 0
# i = 0
# turn = 1
# limit = len(picture[l]) - 1 
# print(limit)
# image = 0

# for image in picture[l]:
#   for i in picture:    
#    if  picture[l][c] == 0:
#      picture[l][c] = ' '
#      print(picture[l])
#      l += 1    
#      turn += 1    
#    elif picture[l][c] == 1:
#       picture[l][c] = "*"
#       print(picture[l])
#       l += 1
#       turn += 1
#   l = 0
#   c = c + 1
#   i = 0
#   turn = 0
#   print("here= ",c)

# parameters
# def say_hi(name, feeling):
#   print(f'hi {name}, so you feel {feeling}')
# # arguments
# n = input('what is your name? ')
# f = input('how do you feel today? ')
# say_hi(n,f)

# n1 = int(input('first number= '))
# n2 = int(input('second number= '))

# def sum(n1, n2):
#   return n1 + n2
# print(sum(n1,n2))

# A NESTED function 
# for i in range(3):  # Outer loop
#   for j in range(2):  # Inner loop
#     print(f"Outer loop: {i}, Inner loop: {j}")
    
    
  # Exercice 
# def checkDriverAge():
#   age = input("What is your age?: ")
#   if int(age) < 18:
#     print("Sorry, you are too young to drive this car. Powering off")
#   elif int(age) > 18:
#     print("Powering On. Enjoy the ride!");
#   elif int(age) == 18:
#     print("Congratulations on your first year of driving. Enjoy the ride!")
# checkDriverAge()

# # IS YOUR NUMBER EVEN?
# num = int(input("write a number to know if it is even: "))
# def is_even(num):
#   if num % 2 == 0:
#     return True
#   return False

# print(is_even(num))

# # CLEAN CODE
# def is_even(num):
#   return num % 2 == 0
  
# print(is_even(51))


# *args
# def super_func(*args):
#   print(*args)
#   return sum(args)
# print(super_func(1,2,3,4,5))


# # DISPLAY DICTIONARIES
# def super_func(*args, **kargs):
#   print(kargs)
#   return sum(args)
# print(super_func(1,2,3,4,5, num1=5, num2=10))

# RULE_ PARAMS, *ARGS, DEFAULT PARAMETERS, ** KWARGS

# My answer
# li = [10, 2, 3, 4, 8, 11]
# def highest_even(li):
#       li.sort()
#       for num in li :
#             if num % 2 == 0:
#                   choosen = 0
#                   if num >= choosen:
#                         choosen = num
#       print(f"The highest even number is: {choosen}")
      
# highest_even(li)

# Course answer
# def highest_even(li):
#   evens = []
#   for item in li:
#     if item % 2 == 0:
#       evens.append(item)
#   return max(evens)

# print(highest_even([2,10,2,3,4,8,11]))