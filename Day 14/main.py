import art
import game_data
import random

def compare(A_followers,B_followers):
    if A_followers > B_followers:
        return 'a'
    else: return 'b'
score = 0

run_a_rand = True
loop = True

while loop == True:

    while run_a_rand:
        a = random.randint(0, len(game_data.data) -1)
        run_a_rand = False

    b = random.randint(0, len(game_data.data) -1)
    if a == b:
        b = random.randint(0, len(game_data.data) -1)
        
    print(art.logo)
    print(f"Compare A: {game_data.data[a]["name"]}, {game_data.data[a]["description"]} from {game_data.data[a]["country"]}")
    print(art.vs)
    print(f"Compare B: {game_data.data[b]["name"]}, {game_data.data[b]["description"]} from {game_data.data[b]["country"]}")
    a_b = input("Who has more followers? Type 'A' or 'B': ")
    A_followers =  {game_data.data[a]["follower_count"]} 
    B_followers = {game_data.data[b]["follower_count"]} 
    print(compare(A_followers, B_followers))

    if a_b == compare(A_followers, B_followers):
        score += 1
        print(f"You're right!!!! Current score: {score}")
        run_a_rand = False
        
    else:
        print("looser")
        loop = False
   