#   I have added random to give the game dodge and miss random functions, similar to Pokemon
#   Import time is basically delay of the messages!

import random
import time

wizard = "wizard"
elf = "elf"
human = "human"

wizard_hp = 270
elf_hp = 300
human_hp = 350

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 700

# --"Choose your character" Section--
def choose_character():
    while True:
        print("Choose your character:")
        print(f"1) {wizard}")
        print(f"2) {elf}")
        print(f"3) {human}")

        character_choice = input("Choose your character: ").lower()

        if character_choice == "wizard" or character_choice == "1":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif character_choice == "elf" or character_choice == "2":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif character_choice == "human" or character_choice == "3":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif character_choice == "exit" or character_choice == "5":
            print("Exiting the game.")
            exit()
        else:
            print("Unknown character. Try something else..")

    print("You chose:", character)
    return character, my_hp, my_damage


# --"Dodging or Miss 10% chance" Section--

def is_dodge():
    return random.random() < 0.1

def is_miss():
    return random.random() < 0.1 


# --"Healing Chosen Character" Section--

def healing_option(character, my_hp):
    if my_hp < 70:
        choice = input(f"Do you want to heal the {character} before continuing the intense fight? (yes/no): ").lower()
        while choice not in ["yes", "no"]:
            print(f"Invalid input. Please type 'yes' or 'no'.")
            choice = input(f"Do you want to heal the {character} before continuing the intense fight? (yes/no): ").lower()

        if choice == "yes":
            if character == "human":
                my_hp += 20
                print(f"The {character} recovers from drinking the potion. The Health went up by ✨ {my_hp} ✨! The {character} appreciates your choice to heal!🧍‍♂️")
                time.sleep(4)

            elif character == "elf":
                my_hp += 20
                print(f"The {character} recovers from drinking the potion. The Health went up by ✨ {my_hp} ✨! The {character} appreciates your choice to heal!🧝")
                time.sleep(4)

            elif character == "wizard":
                my_hp += 20
                print(f"The {character} finds a safe space to cast a healing spell on itself. Health went up by ✨ {my_hp} ✨! The {character} appreciates your choice to heal! 🧙")
                time.sleep(4)

    return my_hp

while True:
    character, my_hp, my_damage = choose_character()
    time.sleep(1)

    print("Your HP:", my_hp)
    time.sleep(1)

    print("Dragon's HP:", dragon_hp)
    time.sleep(1)

    print("Let the battle begin!")
    time.sleep(1)

    while True:
        my_hp = healing_option(character, my_hp)

        if is_miss():
            time.sleep(1)
            print(f"The {character} missed the attack!")
            time.sleep(1)
            print(f"The Dragon dodged the {character}'s attack!")
        elif is_dodge():
            time.sleep(1)
            print(f"The {character} dodged the Dragon's attack!")
            time.sleep(1)
            print(f"The Dragon missed the {character}'s attack!")
        else:
            dragon_hp = dragon_hp - my_damage
            time.sleep(1)
            print("The", character, "damaged the Dragon for", my_damage, "damage!")

        if dragon_hp <= 0:
            time.sleep(1)
            print("The Dragon has lost the battle! Victory!")
            dragon_hp = 300  # <-- (Restart of the dragon's health) For some reason, I have to add dragon_hp here because the game thinks the dragon is immortal
            break

        time.sleep(1)
        print("Dragon's HP:", dragon_hp)

        dragon_damage = 50
        my_hp = my_hp - dragon_damage
        time.sleep(1)
        print("The Dragon's counterattack caused the", character, "to lose", dragon_damage, "health!")

        if my_hp <= 0:
            time.sleep(1)
            print("Oh no! You have been defeated!!")
            dragon_hp = 300  # (Restart of the dragon's health
            break

        time.sleep(1)
        print("Your HP:", my_hp)

        continue_game = input("Do you want to continue the battle? (yes/no): ").lower()
        if continue_game != "yes":
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        time.sleep(1)
        print("Thanks for playing! Have a good one and Stay safe!!")
        break