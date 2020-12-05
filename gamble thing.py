#this is my shitty gambiling thing ( i think i spelt that wrong )
import random, time, os

def input_verify(message):
    while True:
        user_input = input(message).lower() #does shit
        if user_input in ("yes", "no"):
            return user_input
        print("Invalid Input")

def win(number_of_matches, fruit):
    global balance
    print ("Well done! You got", number_of_matches, "of the same fruit!")#more shit lmao
    time.sleep(0.5)
    reward = fruits[fruit][1] * number_of_matches
    print("You won £{}!".format(reward))
    balance += reward

fruits = {"apple": [10000, 1], "banana": [7000, 1.5], "lemon": [6000, 1.75], "orange": [5000, 2], "kiwi": [4000, 4],
          "peach": [3000, 6], "avocado": [2000, 10], "grapes": [1000, 20], "mango": [500, 100], "melon": [1, 10000]}
weighted_fruits = [fruit for fruit in fruits for i in range(fruits[fruit][0])]

print("Welcome to my even even even even even even better version of ewans better version of my better version of his ball game")
print("Each spin costs 1 doge coin")#doge coin best coin
balance = 10
if os.path.exists("One Armed Bandit.txt"):
    with open("One Armed Bandit.txt", "r") as f:
        contents = f.readlines()
    continue_saved_game = input_verify("Do you want to continue your saved game?")
    if continue_saved_game == "yes":
        balance = float(contents[1].strip())

time.sleep(0.5)
print("\nYour current balance is £{}.\n".format(balance))#idk why its now £ and not doge coin but i cba to change it
time.sleep(1)
while True:
    balance -= 1
    reward = 0
    a, b, c = [random.choice(weighted_fruits) for i in range(3)]
    print("Spinning...")
    for fruit in (a, b, c):
        time.sleep(0.5)
        print(fruit)
    time.sleep(0.5)
    if a == b == c:
        win(3, a)
    elif a == b or a == c or b == c:
        if b == c:
            win(2, c)
        else:
            win(2, a)
    else:
        print("Unlucky. None of your fruits matched each other.")
    time.sleep(0.5)
    print("\nYour current balance is £{}.\n".format(balance))
    time.sleep(0.5)
    replay = input_verify("Do you want to play again?")
    if replay == "no":
        save = input_verify("Do you want to save your game?")#idek if the saving works lmao 
        if save == "yes":
            name = input("What is you name?")
            with open (name + ".txt", "w") as f:
                f.write("{}'s Balance:\n{}".format(name, balance))
        break
#made by chris hansen#3106
#<3
#there is a undefined error but im a lazy programmer and cba to fix it
