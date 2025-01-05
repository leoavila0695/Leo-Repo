
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
#     if pixel == 1:
# # end joins the previous line with the following in order to have a straight row
# # instead of saying  "hello"
# #                    "leo"
# # You may say, "hello" "Leo"
#       print('*', end ="")
#     else:
#       print(' ', end ="")
#   print('')



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


# PRINT ITEM BY ITEM 
# a = 'helloooooooooo'
# if ((n := len(a)) > 10):
#     print(f"too long {n} elements")
# while ((n := len(a)) > 1):
#     print(n)
#     a = a[:-1]
# print(a)

# OOP (Object Oriented Programming)

# class PlayerCharacter:
#   # Class Object Attribute 
#   membership = True
#   def __init__(self, name, age):
#     if (PlayerCharacter.membership):
#       self.name = name #Attributes
#       self.age = age
    
#   def run(self):
#     print("run")
#     return "done"
  
#   def shout(self):
#         print(f'my name is {self.name}')
  
# player1 = PlayerCharacter("Leo", 29)
# player2 = PlayerCharacter("Vane", 30)

# # print(player1.name, player1.age)
# # print(player2.name, player2.age)
# # print(player1.run())
# print(player1.shout(),player2.shout())

# class PlayCha1:
#   def __init__(self, name='none', age=0):
#     if (age > 18):
#       self.name = name
#       self.age = age
#     else:
#       self.name = 'none'
#       self.age = 0
      
#   def another(self):
#     print(f'my name is {self.name}')
    
# p1 = PlayCha1('Leo', 29)
# p1.another()

# my_answer
# class Cat:
#     species = 'mammal'
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    

#     def the_oldest(cats):
#         if cats[0].age >= cats[1].age and cats[0].age >= cats[2].age:
#             print(f'The oldest cat is {cats[0].name}')
#         elif cats[1].age >= cats[0].age and cats[1].age >= cats[2].age:
#             print(f'The oldest cat is {cats[1].name}')
#         elif cats[2].age >= cats[0].age and cats[2].age >= cats[1].age:
#             print(f'The oldest cat is {cats[2].name}')
            
# # Crear los gatos
# cat1 = Cat('Raul', 8)
# cat2 = Cat('Luna', 3)
# cat3 = Cat('Aren', 10)

# # Lista de gatos
# cats = [cat1, cat2, cat3]

# # Llamar al método estático
# Cat.the_oldest(cats)


# *args, **kwargs

# def sumar(*args):
#     return sum(args)

# print(sumar(1, 2, 3,54,7897,45))  # Salida: 6
# print(sumar(10, 20))   # Salida: 30

# def mostrar_informacion(**kwargs):
#     for clave, valor in kwargs.items():
#         print(f"{clave}: {valor}")

# mostrar_informacion(nombre="Juan", edad=30, profesion="Ingeniero")
# Salida:
# nombre: Juan
# edad: 30
# profesion: Ingeniero

# class PlayerCharacter:
#   membership = True
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age
        
#   def shout(self):
#     print(f'my name is {self.name} and I am {self.age}')
#     return self.age + self.age
#   @classmethod
#   def adding_things(cls, num1, num2):
#     return cls('Teddy', num1 + num2)
#   @staticmethod
#   def adding_things(num1, num2):
#     return ('Teddy', num1 + num2)
                
# # player1 = PlayerCharacter('Tom', 20)
# player2 = PlayerCharacter.adding_things(2,3)


# # print(player1.adding_things(2,3))
# print(player2.age)
# # print(PlayerCharacter.adding_things(2,3))
# # print(PlayerCharacter.adding_things(200,50))
# # print(player1.shout())

# class Persona:
#     def _init_(self, nombre, edad):
#         self.nombre = nombre  # Atributo público
#         self._edad = edad    # Atributo privado (se encapsula usando _)
    
#     # Método público para obtener la edad
#     def get_edad(self):
#         return self.__edad
    
#     # Método público para cambiar la edad de manera controlada
#     def set_edad(self, nueva_edad):
#         if nueva_edad > 0:  # Verificamos que la edad sea válida
#             self.__edad = nueva_edad
#         else:
#             print("La edad debe ser mayor a 0")
    
#     def mostrar_informacion(self):
#         print(f"Nombre: {self.nombre}, Edad: {self.__edad}")

# # Uso
# persona = Persona("Alice", 25)
# persona.mostrar_informacion()  # Salida: "Nombre: Alice, Edad: 25"

# # Intentar acceder directamente al atributo privado (no funciona)
# # print(persona.__edad)  # Esto dará un error

# # Acceso controlado usando métodos
# print(persona.get_edad())  # Salida: 25
# persona.set_edad(30)
# persona.mostrar_informacion()  # Salida: "Nombre: Alice, Edad: 30"

# class User():
#   def sign_in(self):
#     print("logged in" )
    
# class Wizard(User):
#   def __init__(self, name, power):
#         self.name = name
#         self.power = power
        
#   def attack(self):
#     print(f'attacking with power of {self.power}')
    
# class Archer(User):
#     def __init__(self, name, arrows):
#       self.name = name
#       self.arrows = arrows
#     def attack(self):
#       print(f'attacking with arrows. Arrows left-> {self.arrows}')

# # isinstance(instance, Class)   -> in order to know the structure
# # to verify if an instance is in a class
# wizard1 = Wizard('leo', 100)
# print(isinstance(wizard1, Wizard))



# # Cats_everywhere exercise:
# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# #1 Add nother Cat DONE
# class Aren(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'




# #2 Create a list of all of the pets (create 3 cat instances from the above) DONE
# my_cats = []
# simon = Simon("Simon",6)
# sally = Sally("Sally",5)
# aren = Aren("Aren",12)

# my_cats.append(simon)
# my_cats.append(sally)
# my_cats.append(aren)


# #3 Instantiate the Pet class with all your cats use variable my_pets DONE
# my_pets = Pets(my_cats)

# #4 Output all of the cats walking using the my_pets instance

# my_pets.walk()
