import random
#Create two variable with each player's health bar starting at 100
#Create a list containing numbers in an interval of 5.
#Randomly choose a number from the list to determine how many damage that pokemon does

poke1_health = 100
poke2_health = 100
attack_lst = [0, 5, 10, 15, 20, 25] #Attack damage that is random choosen for players 1 and 2
counter_play1 = 3 #This counter is use to keep track of the 3 maximum defend player 1 can do.
counter_play2 = 3 #This counter is use to keep track of the 3 maximum defend player 2 can do.


while True:
    damage1 = random.choice(attack_lst) #Random damage for player 1
    damage2 = random.choice(attack_lst) #Random damage for player 2
#Player 1 action
    poke1 = input("Its player 1 turn. Would you like to attack or defend: ")
    if poke1 == 'attack' or poke1 == 'a':
        poke2_health -= damage1
        print(f"Player 1 deals {damage1}. Player 2 has {poke2_health} HP left!", '\n')
        if poke2_health <= 0:
            print("Player 1 won the battle!")
            break
    elif poke1 == 'defense' or poke1 == 'd':
        poke2_health -= 0
        print(f"Player 1 has choose to defend and has {counter_play1} defense move left. Player 1 has {poke2_health} HP left!"'\n')
        counter_play1 -= 1
        if counter_play1 <= 0:
            if poke1 == 'defense' or poke1 == 'd':
                print("You cannot defend yourself anymore!")
    elif poke1 == "give":
        print("Player 1 has given up. Player 2 won the battle!")
        break

#Player 2 action
    poke2 = input("Its player 2 turn. Would you like to attack or defend: ")
    if poke2 == 'attack' or poke2 == "a":
        poke1_health -= damage2
        print(f"Player 2 deals {damage2}. Player 1 has {poke1_health} HP left!", '\n')
        if poke1_health <= 0:
            print("Player 2 won the battle!")
            break
    elif poke2 == 'defense' or poke2 == 'd':
        poke1_health -= 0
        print(f"Player 2 choose to defend and has {counter_play2} defense move left. Player 2 has {poke1_health} HP left!"'\n')
        counter_play2 -= 1
        if counter_play2 < 0:
            if poke1 == 'defense' or poke1 == 'd':
                print("You cannot defend yourself anymore!")
    elif poke2 == "give":
        print("Player 2 has given up. Player 1 won the battle!")
        break
    continue
