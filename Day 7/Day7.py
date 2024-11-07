import random
import word_list
import art


print(art.logo)

chosen_word = random.choice(word_list.word_list)
print(chosen_word)


placeholder = len(chosen_word) * "_ "
print(placeholder)

gameover = False
correct_letters = []
life = 6 

while not gameover:
    guess = input("Guess a letter: ")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += guess + " "
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter + " "
        else :display += "_ "
        
    print(display)

    if guess not in chosen_word:
        life -= 1
    print(f"lives left: {life}")

    if "_" not in display:
        gameover = True
    else : gameover = False

    if life == 0:
        gameover = True
        print("You lost sucker")
    
    print(art.stages[life])
