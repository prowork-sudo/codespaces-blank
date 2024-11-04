import random

# print(random.randint(1,10))

# a = random.randint(0,1)

# if a == 0:
#     print("head")
# else:print("tail")

# a = ['a','b','c','d','e']
# b = random.randint(0,4)
# print (a[b])

# print(random.choice(a))

rock = """                                            
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
                                             """

paper =""" 8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88   """

scissors = """ 
  O O   \ /
   X     X      VK
  / \   O O  """

li = [rock, paper, scissors]

user = int(input("0 for Rock\n 1 for Paper\n 2 for scissors"))

comp = random.randint(0,2)
print(f"your choice{li[user]}\n")
print(f"comp choice{li[comp]}")

if user == comp:
    print("draw")
elif user == 1 and comp == 2 or user == 1 and comp == 0 or user == 2 and comp == 1:
    print("you win master")
else:print("Suck my binary ass")
