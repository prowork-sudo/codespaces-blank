# a = int(input("enter a number"))
# b = a % 2
# if b == 0:
#     print("even")
# else: print("Odd")
a = """                            ____________
                           /            \
                          |  Yes, I do.  |
                           \_______  ___/
         ______                    \|
        /      \                    `
       |  Ungh! |                    ,.~~~~"
        \__  __/  *Punch!*           ~(\~~~'    ______ _ _
           `.\                       /- ((\__--'      _ _
             `      \|/            ,'(((\\\~~'   _,--'
                 ___          ,-'\\  ((_/       /|
               <'___')   ___,'    _\            ~~--__
          ((    )=*/3\,-'     _,-'  \         =-__\\
   _            \_*\3______,-' _,----\\    _,-=   `._ _ _
  ' |   _    ,-_/__/\-'`------'   _,-' \,-'
  : | -'    /  /  | __ (     __,-'      `.
  : |  --   (     \.\_\ ,---'  ,'`-       `.
  : | -._   / |    \.  /     ,'    )        `-._
  ._|       -_|     \. (   ,'  ,/  |            - - _ _
  \_       ( =3\     \,'\_/  ,' /  /
  __]__[~~-_`"'|\   ,' ,'-  /  (   |    ) )
  __________] [| (,' ,'  ___  /|  /
        |||    | |\,','\    `-./ /
        |||    \ \_\ \,' ---..  `-.
        |||     \___`-._____,.`-.  `--.
        |||         ||==I     `-.`-.__ `-,_._
        |||         ||           `-._____/8xx`)
        |||         ||                   `==='     ) )
        |||      ___||___
  -------||-----o---o----o------------                         Ool"""
print(a)


print("Welcome to Treasure Island. Your mission is to find the treasure.")
one = input("Yor are at a cross road Left or Right")
if one == "Left":
    two = input("Wait or Swim")
    if two == "Wait":
        three = input("Which Door R B Y ?")
        if three == "R":
            print("Burned by fire.\nGame Over.")
        elif three =="B":
            print("Eaten by beasts. \n Game Over.")
        elif three =="Y":
            print("You win")
        else:print("Game over")
    else: print("Attacked by trout. \nGame Over.")
    
else: print("Fall into a hole.\n Game Over.")
