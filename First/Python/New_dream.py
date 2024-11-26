# TYPES
# type, n.isalpha and n.isdigit
# while True:
#   n1 = input("Por favor, escribe tu nombre: ")
#   print (type(n1))
#   print (5+4)
#   print (type(5+4))
#   if n1.isalpha():
#     print("eso es     " + n1[4] + n1leo::-1]) 
#   if n1.isnumeric():
#     print("numero everywhere ")
#     break


# FEELINGS
# veamos que siente leo por ti
# print ("Veamos que siente leo por ti")
# n1 = input("Por favor, escribe tu nombre: ")
# if n1 == "vanesa" or n1 == "Vanesa":
#   print ("Leo te ama locamente... loca.... por cierto, TENGO HAMBRE, ALIMENTAME ")
# elif n1 == "juliana" or n1 == "Juliana":
#   print ("Leo creo que eres muy inteligente y te quiere, y quiere  que LEAAAAAAAAS MUCHOS LIBROS")
# else: print ("NO SE QUIEN ERES, VETE HHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHE")


# COUNTING
# conteo hasta 100
# while True:
#   try:
#     n = float(input ("Write a number in order to have the count  \nfrom the number you write down up to 100 : ")) 
#     if n== 0 or n>= 100:
#       print("that value is not valid, write another one")
#     else : 
#       while True:      
#         n += 1     
#         print (n)
#         if n >= 100:
#           break
#       break
#   except ValueError:
#     print("you wrote an invalid character, try again")


# CALCULATOR
# print("hello, welcome to calculatron.\nplease type 2 digits in order to do a math operation \nor press 'q' to quit")
# while True:  
#   try:    
#     n1 = float(input("first number: "))
#     n2 = float(input("second number: "))
#     print ("so your first number is " + str(n1) +"\nand the second is " + str(n2) )    
#     try:
#             op = input("please type the math operation symbol (+ , -, *, /) \n or if you rather to quit press 'q'")
#             if op == "+":
#                 plu = n1 + n2
#                 print ("result is " + str(plu))  
#             if op == "-":
#                 min = n1 - n2
#                 print ("result is " + str(min))  
#             if op == "*":
#                 tim = n1 * n2
#                 print ("result is " + str(tim))
#             if op == "/":
#                 div = n1 / n2
#                 print ("result is " + str(div))  
#             if op == "q":
#                 print("thanks for coming")
#                 break   
#     except ValueError:
#             print ("wrong value, try again again")
#   except ValueError:
#     print ("wrong value, try again again")

# wether = str("it's \"really\" sunny")
# print (wether)
# name = "Leo"
# age = "29"
# print(f"hi {name} you are {age} years old {wether}")

# leo = "vanesa"
# print (leo[::-1])

# year = int(input("when were you born? "))
# print (f"so you are {str(2024-year)} years old")

# user1=input("Say my name: ")
# password=input("Say the clue word: ")
# hidden_password = "*" * len(password)
# print(f"{user1} \nyour assinged password is: {password} and has {len(password)} letters\nso this is your password {hidden_password}")


# SHORE LIST
# while True:
#   try:
#     lengh=int(input("please write your shore lengh list: "))
#     list = []
#     if lengh <= 0:
#       print("Write a possitive number")
#     else:
#       break
#   except ValueError:
#     print("wrong value, try again")
# for i in range(lengh):
#   n = input(f"Write product # {i+1} ")
#   list.append(n)
# print(f"The list is: {list}")
# while True:
#   try:
#     elect=int(input("What element do you want to check,\nwrite the number of the element: "))
#     #Se le resta 1 porque el indice empieza en 0
#     elect = int(elect-int(1))
#     if elect < 0 :
#       print("Write a possitive number")
#     elif elect > lengh:
#       print("Write a number less than the lengh of the list")
#     else:
#       break
#   except ValueError:
#     print("wrong value, try again")
# print(f"your element is: {list[elect]}")
# new=input(" write your new product: ")
# list[elect]=new
# list.sort()
# print(f"your new list is: {list}")
#task to be carried out
#1. Edit the program in order to switch an specific elements of the list (or elements)

# MATRIX
# matrix = [
#   [1,5,1],
#   [0,1,0],
#   [1,0,1]
# ]
# print(matrix[0][1])


# GAME Rock, Paper, Scissors
# import random
# print("Welcome to Rock, Paper, Scissors ")
# game = 1
# pc = 0
# player = 0
# while game < 4 and pc < 2 and player < 2:
#       try:            
#             sel = int(input("let's play, so chose your option...\n1-Rock\n2-paper\n3-Scissors\nWhat would you rather..."))
#             if sel not in [1, 2, 3]:
#                   print ("this digit is not valid...try again")
#                   continue
#             else:               
#                   cpu = random.randint(1, 3)
#                   dec = {
#                         1 : 'rock',
#                         2 : 'Paper',
#                         3 : 'Scissors'
#                         }       
#             if sel == cpu:
#                   print(f"Cpu = {dec[cpu]} VS you = {dec[sel]} We're tie... ")
#             elif sel == 1 and cpu == 2:
#                   print(f"Cpu = {dec[cpu]} VS you = {dec[sel]} I win...")
#                   game += 1
#                   pc += 1
#             elif sel == 2 and cpu == 3:
#                   print(f"Cpu = {dec[cpu]} VS you = {dec[sel]} I win...")  
#                   game += 1
#                   pc += 1
#             elif sel == 3 and cpu == 1:
#                   print(f"Cpu = {dec[cpu]} VS you = {dec[sel]} I win...")  
#                   game += 1 
#                   pc += 1 
#             else:            
#                   print(f"Cpu = {dec[cpu]} VS you = {dec[sel]} You win...")
#                   game += 1
#                   player += 1
#       except ValueError:
#             print(f"Be carefull, this is not a valid value, try again...")
# if pc > player:
#     print(f"I won the game! Final score: Cpu {pc} - You {player}")
# else:
#     print(f"Congratulations! You won the game! Final score: You {player} - Cpu {pc}")
      
