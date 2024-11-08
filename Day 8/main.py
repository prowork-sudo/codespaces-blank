# def greet(name, loc): # function with parameter    positional
#     print(f"hello {name} are you from {loc}")

# greet("Provr", "blr") # provr is the argument


# def greet(name, loc): # function with parameter        key 
#     print(f"hello {name} are you from {loc}")

# greet(loc = "blr1",name = "Provr1") # provr is the argument
import art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# def encrypt(user_message,user_shift_num):
#     final = ''
#     for letter in user_message:
#         a = alphabet.index(letter) + user_shift_num
#         a %= len(alphabet)      # to loop the list in case of 25 + 9 = 34     34 % 25 = 9
#         final += alphabet[a]
#     print(f"Here's the encoded result: {final} ")



# def decrypt(user_message,user_shift_num):
#     final = ''
#     for letter in user_message:
#         a = alphabet.index(letter) - user_shift_num
#         final += alphabet[a]
#     print(f"Here's the decoded result: {final}")

def ceaser(user_message,user_shift_num,encrypt_decript):

    final = ''

    if encrypt_decript == "decode":
        user_shift_num *= -1

    for letter in user_message:
        a = alphabet.index(letter) + user_shift_num
        a %= len(alphabet)      # to loop the list in case of 25 + 9 = 34     34 % 25 = 9
        final += alphabet[a]
    print(f"Here's the {encrypt_decript} result: {final} ")


cont = True
while cont :
    print(art.logo)
    eord = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    user_message = input("Type your message:\n")

    user_shift_num = int(input("Type the shift number:\n"))

    ceaser(user_message,user_shift_num,eord) 

    loop = input("type 'yes' if you want ot go again. else 'no'. \n")
    if loop == "no":
        cont = False
