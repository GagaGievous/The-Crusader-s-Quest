# Python Text RPG
# Authored by: Gaga Gievous
# Copyright February 2021

import cmd
import textwrap
import sys
import os
import time
import random
import math

counter = 0
counter_set = 0

name =''
hp = 0
max_hp = 0

martial_prowess = 0
consumption_rate = 10
endurance = 10
food = 0
max_food = 0
race = ''
luck = 0
arrows = 0
max_arrows = 0
speed = 0
occupation = ''
illness = 'None'
gold = 100
max_gold = 0

blacksmith_price = 500



weapon = 'Sword'
weapon_type = 'sword'

location = ''
days_to_go = 0
adventure_state = False

enemy_adjective = ''
enemy_type = ''
enemy_locater = ''
enemy_number = ''
enemy_exclude = 0
enemy_battlescore = 0
enemy_gold = 0
enemy_arrows = 0
enemy_food = 0
enemy_specific_gold = 0
enemy_specific_arrows = 0
enemy_specific_food = 0
damage_taken = 0

### Title Screen ###
def title_screen_selections():
    option = input('>: ')

    if option.lower() == '1':
        setup_game() 
    elif option.lower() == '2':
        help_menu()
    elif option.lower() == '0':
        sys.exit()
    while option.lower() not in ['1', '2', '0']:
        option = input('>: ')
        if option() == '1':
            setup_game() 
        elif option() == '2':
            help_menu()
        elif option() == '0':
            sys.exit()

def title_screen():
    os.system('cls')
    
    print('The Crusader\'s Quest: Survival Text RPG.\n')
    print('  1 Play  ')
    print('  2 Tips  ')
    print('  0 Quit  ')
    title_screen_selections()

def help_menu():
    print('Human, Dwarf, and Satyr are the best races for beginners.')
    print('The Adventurer class works well with every race, but is not necessarily the best.')

    title_screen_selections()

### Character Creation ###

# Name #
def setup_game():
    global name
    global hp
    global max_hp
    global martial_prowess 
    global consumption_rate 
    global endurance 
    global food 
    global max_food 
    global race 
    global luck 
    global arrows 
    global max_arrows
    global speed 
    global occupation 
    global illness 
    global illness_chance 
    global gold
    global max_gold 
    global durability 
    global weapon
    global max_heal_item
    global adventure_state

    arrows = 0
    gold = 0
    food = 0
    max_arrows = 0
    max_gold = 0
    max_food = 0
    hp = 0
    max_hp = 0
    martial_prowess = 0
    heal_item = 0
    endurance = 10
    adventure_state = False
    os.system('cls')
    print('The Antipope is defiling the holiest religious site in the world. You are a warrior monk from the Freemasons, and it is up to you to destroy the Antipope.\n')
    print('You begin your journey in Goodshire, one of the many towns you hope to pass through.\n')
    print('What is your name?\n')

    name = input('>: ')

# Race #
    os.system('cls')
    print('What is your race?\n')
    print('1 Human\n2 Dwarf\n3 Satyr\n4 Halfling\n5 Elf\n6 Tigerman\n7 Leprechaun\n')

    selection = input('>: ')
    if selection == '1':
        race = "Human"
        hp = 25
        max_hp = 25
        martial_prowess = 10
        consumption_rate = 10
        endurance = 30
        gold = 100
        luck = 0
        speed = 0

    elif selection == '2':
        race = "Dwarf"
        hp = 50
        max_hp = 50
        martial_prowess = 30
        consumption_rate = 20
        endurance = 240
        gold = 200
        luck = 0
        speed = 0

    elif selection == '3':
        race = "Satyr"
        hp = 200
        max_hp = 200
        martial_prowess = 0
        consumption_rate = 20
        endurance = 240
        gold = 0
        luck = 0
        speed = 0

    elif selection == '4':
        race = "Halfling"
        hp = 25
        max_hp = 25
        martial_prowess = 0
        consumption_rate = 20
        endurance = 200
        gold = 100
        luck = 0
        speed = 0

    elif selection == '5':
        race = "Elf"
        hp = 10
        max_hp = 10
        martial_prowess = 0
        consumption_rate = 10
        endurance = 1000
        gold = 100
        luck = 0
        speed = 0

    elif selection == '6':
        race = "Tigerman"
        hp = 25
        max_hp = 25
        martial_prowess = 50
        consumption_rate = 20
        endurance = 100
        gold = 0
        luck = 0
        speed = 0

    elif selection == '7':
        race = "Leprechaun"
        hp = 10
        max_hp = 10
        martial_prowess = 0
        consumption_rate = 10
        endurance = 10
        gold = 1000
        luck = 0
        speed = 0
        
    else:
        race = "Human"
        hp = 25
        max_hp = 25
        martial_prowess = 10
        consumption_rate = 10
        endurance = endurance + 30
        gold = 100
        luck = 0
        speed = 0

    os.system('cls')

# Occupation #
    print('What is your occupation?\n')
    print('1 Hunter\n2 Knight\n3 Adventurer\n4 Assassin\n5 Glutton\n')
    
    selection = input('>: ')
    if selection == '1':
        occupation = 'Hunter'
        hp = hp + 10
        max_hp = max_hp + 10
        food = food + 50
        max_food = max_food + 150
        arrows = arrows + 75
        max_arrows = max_arrows + 100
        gold = gold + 0
        max_gold = max_gold + 800
        martial_prowess = martial_prowess + 0    
    elif selection == '2':
        occupation = 'Knight'
        hp = hp + 100
        max_hp = max_hp + 100
        food = food + 25
        max_food = max_food + 100
        arrows = arrows + 8
        max_arrows = max_arrows + 10
        gold = gold + 400
        max_gold = max_gold + 1000
        martial_prowess = martial_prowess + 20
    elif selection == '3':
        occupation = 'Adventurer'
        hp = hp + 25
        max_hp = max_hp + 25
        food = food + 75
        max_food = max_food + 100
        arrows = arrows + 20
        max_arrows = max_arrows + 20
        gold = gold + 100
        max_gold = max_gold + 800
        martial_prowess = martial_prowess + 10
    elif selection == '4':
        occupation = 'Assassin'
        hp = hp + 0
        max_hp = max_hp + 0
        food = food + 25
        max_food = max_food + 100
        arrows = arrows + 8
        max_arrows = max_arrows + 10
        gold = gold + 100
        max_gold = max_gold + 1000
        martial_prowess = martial_prowess + 60
    elif selection == '5':
        occupation = 'Glutton'
        hp = hp + 25
        max_hp = max_hp + 25
        food = food + 500
        max_food = max_food + 500
        arrows = arrows + 0
        max_arrows = max_arrows + 1
        gold = gold + 0
        max_gold = max_gold + 1000
        martial_prowess = martial_prowess + 0
    else:
        occupation = 'Hunter'
        hp = hp + 10
        max_hp = max_hp + 10
        food = food + 50
        max_food = max_food + 150
        arrows = arrows + 75
        max_arrows = max_arrows + 100
        gold = gold + 0
        max_gold = max_gold + 300
        martial_prowess = martial_prowess + 0  

    os.system('cls')

    print('What kind of weapon do you want to use? (ie. sword, poleaxe, etc.)')

    weapon = input('>: ')
    gold_mechanic()
    os.system('cls')
    
    #print('What is your weapon called? (ie. Thorn, Crusher, etc.)')

    #weapon = input('>: ')
    #os.system('cls')

    print('You are ' + name + ', the ' + race + ' ' + occupation + '. You wield a ' + weapon + '.\n')
    print('1 Begin Adventure\n2 Restart')
    selection = input('>: ')
    if selection == '1': 
        start_game()
    else: 
        title_screen()    

### Death ###
def death():
    os.system('cls')
    print('You have died.\n')
    selection = input('Press enter enter to continue')
    char_menu()
    print()
    print('1 Menu\n')
    selection = input('>: ')
    if selection == '1':
        title_screen()
    else:
        title_screen()

### Food and Endurance Mechanic ###

def food_endurance_mechanic():
    global food
    global endurance
    global consumption_rate
    if food < consumption_rate and food > 0:
        food = 0
    elif food > 1:
        food = food - consumption_rate
    elif food < 1:
        food = 0
        endurance = endurance - consumption_rate
        if endurance < 1:
            endurance = 0
            death()
        elif endurance <= consumption_rate:
            print('If you do not get food, you will starve to death.')
        
    #need to work on restoring endurance#

### Resource Mechanics ###

def hp_mechanic():
    global hp
    global max_hp
    if hp > max_hp:
        hp = max_hp
        print('You have max HP.')
    if hp < 1:
        hp = 0
        death()

def gold_mechanic():
    global gold
    global max_gold
    if gold < 1:
        gold = 0
    if gold > max_gold:
        gold = max_gold
        print('You have completely filled your coin purse.')
    if gold < 1:
        gold = 0

def food_mechanic():
    global food
    global max_food
    if food > max_food:
        food = max_food
        print('You have maxed out your food supply.')
    if food < 1:
        food = 0

def arrows_mechanic():
    global arrows
    global max_arrows
    if arrows < 1:
        arrows = 0 
    if arrows > max_arrows:
        arrows = max_arrows
        print('You have maxed out your arrow count.')
    if arrows < 1:
        arrows = 0
        
### Character Menu ###
def char_menu():
    os.system('cls')
    global name
    global hp
    global max_hp
    global martial_prowess 
    global consumption_rate 
    global endurance 
    global food 
    global max_food 
    global race 
    global luck 
    global arrows 
    global max_arrows
    global speed 
    global occupation 
    global illness 
    global illness_chance 
    global gold
    global max_gold 
    global weapon


    print('Name: ' + name + '')
    print('Race: ' + race + '')
    print('Occupation: ' + occupation + '')

    print('HP: ' + str(hp) + '/' + str(max_hp) + '')
    print('Martial Prowess: ' + str(martial_prowess) + '')
    print('Weapon: ' + weapon + '')
    #print('######################')
    print('Consumption Rate: ' + str(consumption_rate) + '')
    print('Food: ' + str(food) + '/' + str(max_food) + '')
    print('Endurance: ' + str(endurance) + '')
    print('Arrows: ' + str(arrows) + '/' + str(max_arrows) + '')
    #print('######################')
    #print('Luck: ' + str(luck) + '')
    #print('Speed: ' + str(speed) + '\n')
    #print('Illness: ' + illness + '')
    print('Gold: ' + str(gold) + '/' + str(max_gold) + '')
    #print('######################\n')
    selection = input('Press enter to continue')
    

### Adventure Menu ###
def adventure_menu():
    global hp
    global max_hp
    global martial_prowess 
    global consumption_rate 
    global endurance 
    global food
    global max_food
    global arrows
    global max_arrows
    global gold
    global max_gold
    global weapon

    os.system('cls')
    print('######################')
    print('HP: ' + str(hp) + '/' + str(max_hp) + '')
    print('Food: ' + str(food) + '/' + str(max_food) + '')
    print('Arrows: ' + str(arrows) + '/' + str(max_arrows) + '')
    print('Gold: ' + str(gold) + '/' + str(max_gold) + '')
    print('Endurance: ' + str(endurance) + '')
    print('######################')
    print('Martial Prowess: ' + str(martial_prowess) + '')
    print('Weapon: ' + weapon + '')
    print('Consumption Rate: ' + str(consumption_rate) + '')
    print('######################\n')

### Map ###         Update this to turn X into another symbol when that location is active
def the_map():
    #print('Key: T = Town; C = City; etc.)

   

    days_to_go()

### Days to Go ###
def days_to_go():
    global location
    global counter
    global counter_set
    global adventure_state
    
    if location == 'Goodshire':
        if adventure_state == False:
            counter_set = 7
            counter = 7
            print('You will brave the wilds for ' + str(counter_set) + ' days.')
            print('1 Continue\n2 Back')
            selection = input('>: ')
            if selection == '1':
                input('Press enter to continue')
                adventuring()
                
            elif selection == '2':
                town()
            else:
                town()
        if adventure_state == True:
            print('You have ' + str(counter) + ' days to go.')
            input('Press enter to continue')

    if location == 'Rodez':
        if adventure_state == False:
            counter_set = 11
            counter = 11
            print('You will brave the wilds for ' + str(counter_set) + ' days.')
            print('1 Continue\n2 Back')
            selection = input('>: ')
            if selection == '1':
                input('Press enter to continue')
                adventuring()
                
            if selection == '2':
                town()
            else:
                town()
        if adventure_state == True:
            print('You have ' + str(counter) + ' days to go.')
            input('Press enter to continue')
    if location == 'Oristano':
        if adventure_state == False:
            counter_set = 15
            counter = 15
            print('You will brave the wilds for ' + str(counter_set) + ' days.')
            print('1 Continue\n2 Back')
            selection = input('>: ')
            if selection == '1':
                input('Press enter to continue')
                adventuring()
                
            if selection == '2':
                town()
            else:
                town()
        if adventure_state == True:
            print('You have ' + str(counter) + ' days to go.')
            input('Press enter to continue')
    if location == 'Thasos':
        if adventure_state == False:
            counter_set = 19
            counter = 19
            print('You will brave the wilds for ' + str(counter_set) + ' days.')
            print('1 Continue\n2 Back')
            selection = input('>: ')
            if selection == '1':
                input('Press enter to continue')
                adventuring()
                
            if selection == '2':
                town()
            else:
                town()
        if adventure_state == True:
            print('You have ' + str(counter) + ' days to go.')
            input('Press enter to continue')
    if location == 'Karabuk':
        if adventure_state == False:
            counter_set = 25 
            counter = 25
            print('You will brave the wilds for ' + str(counter_set) + ' days.')
            print('1 Continue\n2 Back')
            selection = input('>: ')
            if selection == '1':
                input('Press enter to continue')
                adventuring()
                
            if selection == '2':
                town()
            else:
                town()
        if adventure_state == True:
            print('You have ' + str(counter) + ' days to go.')
            input('Press enter to continue')
    if location == 'Last Refuge':
        if adventure_state == False:
            counter_set = 25
            counter = 25
            print('You will brave the wilds for ' + str(counter_set) + ' days.')
            print('1 Continue\n2 Back')
            selection = input('>: ')
            if selection == '1':
                input('Press enter to continue')
                adventuring()
                
            if selection == '2':
                town()
            else:
                town()
        if adventure_state == True:
            print('You have ' + str(counter) + ' days to go.')
            input('Press enter to continue')

### Treasure Generator ###
#def treasure_generator():
   # v = random.randint(0, 3)
   # print('You found ' + str(v) + ' treasures on this leg of the journey.')
    

### Location Changer ###
def location_changer():
    global location
    global adventure_state

    adventure_state == False
    
    if location == 'Goodshire':
        location = 'Rodez'
        blacksmith_price_generator()
        #treasure_generator()
        town()
    if location == 'Rodez':
        location = 'Oristano'
        blacksmith_price_generator()
        town()
    if location == 'Oristano':
        location = 'Thasos'
        blacksmith_price_generator()
        town()
    if location == 'Thasos':
        location = 'Karabuk'
        blacksmith_price_generator()
        town()
    if location == 'Karabuk':
        location = 'Salem'
        blacksmith_price_generator()
        salem()
    if location == 'Last Refuge':
        location = 'Rodez'
        blacksmith_price_generator()
        #end_game()

    #town()

### Town Description ###
def town_description():
    global location
    
    if location == 'Goodshire':
        print('The sun shines brightly on the lazy Halfling natives.')
    elif location == 'Rodez':
        print('The sky is overcast, and your feet squelch in the mud from a recent rain.')
    elif location == 'Oristano':
        print('The surrounding trees loom over the town like giants, and block the sun\'s rays.')
    elif location == 'Thasos':
        print('A hot, dry wind blows clouds across the yellow sun, and you feel hot.')
    elif location == 'Karabuk':
        print('There is a foul stench in the air, and the ground is covered bubbling puddles of unknown origin.')

### Start Game ###
def start_game():
    global location
    location = 'Goodshire'
    blacksmith_price_generator()
    enemy_locater_generator()
    town()

### Town ###
def town():
    global counter
    global adventure_state
    os.system('cls')
    adventure_state == False
    print('You are in ' + location + '.')
    town_description()
    print()
    print('1 Tavern\n2 Blacksmith\n3 Character\n4 Adventure')
    selection = input('>: ')
    if selection == '1':
        os.system('cls')
        tavern()
    if selection == '4':
        os.system('cls')
        counter = 0
        the_map()
        print('You will brave the wilds for 5 days.')
        input('Press enter to continue')
        adventuring()

    if selection == '2':
        os.system('cls')
        blacksmith()
    if selection == '3':
        os.system('cls')
        char_menu()
        town()
    else:
        town()

### Tavern ###
def tavern():
    global food
    global consumption_rate
    global gold
    global hp
    global location

    os.system('cls')
  
    print('Gold: ' + str(gold) + '/' + str(max_gold) + '')
    print('HP: ' + str(hp) + '/' + str(max_hp) + '')
    print('Food: ' + str(food) + '/' + str(max_food) + '')
    
    print('"Welcome to the ' + location + ' Inn. How may I serve you?"\n')
    print('1 Rest (1 gold)\n2 Buy Food (5 gold)\n3 Sell Food (3 gold)\n4 Speak with random patron\n5 Back')
    selection = input('>: ')
    if selection == '1':
        if gold < 1:
            print('You cannot afford a bed here.')
            input('Press enter to continue.')
            tavern()
        else:
            print('You slept like a rock.')
            hp = hp + 99999
            hp_mechanic()
            gold = gold - 1
            input('Press enter to continue.')
            tavern()

    if selection == '2':
        print('How much food do you want to buy?')
        total_cost = 0
        food_price = 5
        n = input('>: ')
        if n == '0':
            tavern()
        n = int(n)
        total_cost = n * food_price
        if total_cost > gold:
            print('You do not have enough gold to buy ' + str(n) + ' food.')
            input('Press enter to continue')
            tavern()
        elif total_cost <= gold:
            food = food + n
            food_mechanic()
            gold = gold - total_cost
            print('You complete the transaction')
            input('Press enter to continue')
            tavern()
    if selection == '3':
        print('How much food do you want to sell?')
        total_sell = 0
        food_sell = 3
        n = input('>: ')
        if n == '0':
            tavern()
        n = int(n)
        total_sell = n * food_sell
        if food < n:
            print('You do not have that much food.')
            input('Press enter to continue')
            blacksmith()
        if food >= n:
            food = food - n
            gold = gold + total_sell
            print('You complete the transaction')
            gold_mechanic()
            input('Press enter to continue')
            os.system('cls')
            tavern()
    if selection == '4':
        talk()
        tavern()
    if selection == '5':
        town()
    else:
        tavern()

# Talk #
def talk():
    dialogue = random.randint(1, 10)
    part = ''
    if dialogue == 1:
        print('I don\'t take too kindly to travelers.')
    if dialogue == 2:
        print('I\'m too scared to leave ' + location + '. I don\'t know how you survive out there.')
    if dialogue == 3:
        print('The ' + location + ' Inn is the best tavern in the world. Not that I would know.')
    if dialogue == 4:
        print('There\'s nasty things where you\'re headed.')      
    if dialogue == 5:
        print('Someone I know was killed looking inside a hollow tree. You wouldn\'t want that happening to you.')  
    if dialogue == 6:
        print('If you run out of food and arrows in the wilds, how will you survive? On pure endurance?')
    if dialogue == 7:
        print('If you want stronger equipment, I recommend going to the blacksmith.')
    if dialogue == 8:
        n = random.randint(1, 8)
        if n == 1:
            part = 'arm'
        if n == 2:
            part = 'leg'
        if n == 3:
            part = 'hand'
        if n == 4:
            part = 'foot'
        if n == 5:
            part = 'eye'
        if n == 6:
            part = 'ear'
        if n == 7:
            part = 'finger'
        if n == 8:
            part = 'toe'
        print('In the wilds, I got caught in a hunter\'s trap. That\'s how I lost my ' + part + '.')
    if dialogue == 9:
        print('Tales of the beasts and Satanic denizens in the wilds have kept me inside the city walls.')
    if dialogue == 10:
        print('The good thing about resting at ' + location + ' Inn is that you get a complimentary meal.')  
    input('Press enter to continue')
    tavern()
### Blacksmith ###
def blacksmith():
    global weapon
    global weapon_type
    global gold
    global max_gold
    global blacksmith_price
    global martial_prowess
    global arrows
    global max_arrows

    os.system('cls')
    
    print('Gold: ' + str(gold) + '/' + str(max_gold) + '')
    print('Arrows: ' + str(arrows) + '/' + str(max_arrows) + '')
    print('Martial Prowess: ' + str(martial_prowess) + '')
    
    print('"What can I do for you, traveler?"')
    print('1 Upgrade your ' + weapon + ' (' + str(blacksmith_price) + ') gold.\n2 Buy Arrows (5 gold)\n3 Sell Arrows (3 gold) \n4 Back')
    selection = input('>: ')
    if selection == '1':
        if gold < blacksmith_price:
            print('You do not have enough gold to upgrade your ' + weapon_type + '.')
            input('Press enter to continue')
            blacksmith()
        else:
            gold = gold - blacksmith_price
            gold_mechanic()
            v = random.randint(10, 30)
            martial_prowess = martial_prowess + v
            print('Your martial prowess increases by ' + str(v) + '.')
            input('Press enter to continue')
            blacksmith()
    if selection == '2':
        print('How many arrows do you want to buy?')
        total_cost = 0
        arrow_price = 5
        n = input('>: ')
        n = int(n)
        total_cost = n * arrow_price
        if total_cost > gold:
            print('You do not have enough gold to buy ' + str(n) + ' arrows.')
            input('Press enter to continue')
            blacksmith()
        if total_cost <= gold:
            arrows = arrows + n
            arrows_mechanic()
            gold = gold - total_cost
            print('You complete the transaction')
            input('Press enter to continue')
            blacksmith()
    if selection == '3':
        print('How many arrows do you want to sell?')
        total_sell = 0
        arrow_sell = 3
        n = input('>: ')
        n = int(n)
        total_sell = n * arrow_sell
        if arrows < n:
            print('You do not have that many arrows.')
            input('Press enter to continue')
            blacksmith()
        if arrows >= n:
            arrows = arrows - n
            gold = gold + total_sell
            print('You complete the transaction')
            gold_mechanic()
            input('Press enter to continue')
            os.system('cls')
            blacksmith()

    if selection == '4':
        town()
    else:
        blacksmith()


### Blacksmith Price Generator ###
def blacksmith_price_generator():
    global gold
    global location
    global blacksmith_price
    
    blacksmith_price = random.randint(51, 75)
    if location == 'Rodez':
        blacksmith_price = blacksmith_price + 25
    if location == 'Oristano':
        blacksmith_price = blacksmith_price + 45
    if location == 'Thasos':
        blacksmith_price = blacksmith_price + 65
    if location == 'Karabuk':
        blacksmith_price = blacksmith_price + 85
    if location == 'Last Refuge':
        blacksmith_price = blacksmith_price + 105
    
        
### Adventuring ###
def adventuring():
    global name
    global hp
    global max_hp
    global martial_prowess 
    global consumption_rate 
    global endurance 
    global food 
    global max_food 
    global race 
    global luck 
    global arrows 
    global max_arrows
    global speed 
    global occupation 
    global illness 
    global gold
    global max_gold  
    global weapon
    global counter
    global location
    global adventure_state

    adventure_state == True
    while counter != 0:
        adventure_state = True
        if hp > 0:
            adventure_menu()
            print('1 Continue\n2 Hunt\n3 Rest\n4 Map\n')
            selection = input('>: ')
            os.system('cls')
            if selection == '1':
                food_endurance_mechanic()
                adventure_menu()
                random_event()    
                counter = counter - 1
            if selection == '2':
                hunt()
            if selection == '3':
                rest()
            if selection == '4':
                the_map()
            else:
                adventuring()
        else:
            death()
    counter = 0
    os.system('cls')
    adventure_menu()
    print('You have survived the trip.')
    adventure_state = False
    print('Enter 0 to continue.')
    selection = input('>: ')
    if selection == '0':
        location_changer()
    else:
        adventuring()    #was location_changer()

### Rest ###
def rest():
    global hp
    global max_hp
    global food

    x = random.randint(15, 25)
    food_endurance_mechanic()

    if hp == max_hp:
        print('You rest for one day. Your HP is already maxed out.')

        input('Press enter to continue')
        adventuring()
    
    print('You rest for one day, gaining ' + str(x) + ' HP.')
    hp = hp + x
    hp_mechanic()
    
    input('Press enter to continue')

### Hunt ###
def hunt():
    global arrows
    global food
    x = random.randint(1, 10)
    y = random.randint(1, 25)

    if arrows == 0:
       print('You do not have any arrows to hunt with.')
       input('Press enter to continue')
       adventuring()

    elif arrows < x:
        adventure_menu()
        x = arrows
        arrows = arrows - x
        food = food + y
        arrows_mechanic()
        print('You shot ' + str(x) + ' arrows, and gained ' + str(y) + ' food.') 
        food_mechanic()

    else:
        adventure_menu()
        arrows = arrows - x
        food = food + y
        arrows_mechanic()
        food_mechanic()
        print('You shot ' + str(x) + ' arrows, and gained ' + str(y) + ' food.')

    input('Press enter to continue')
                 
    
########################################################################
########################### Random Events ##############################
########################################################################
def random_event():
    n = random.randint(1, 20)
    if n == 1:
        chest()
    if n == 2:
        fight()
    if n == 3:
        robbed()
    if n == 4:
        traveller()
    if n == 5:
        damaged()
    if n == 6:
        miracle()
    if n == 7:
        mushroom()
    if n == 8:
        nothing()
    if n == 9:
        fight()
    if n == 10:
        fight()
    if n == 11:
        chest()
    if n == 12:
        fight()
    if n == 13:
        robbed()
    if n == 14:
        traveller()
    if n == 15:
        damaged()
    if n == 16:
        mystic()
    if n == 17:
        bigger_bag()
    if n == 18:
        lose_day()
    if n == 19:
        fight()
    if n == 20:
        fight()

### Mushroom ###
def mushroom():
    global endurance
    global hp
    global consumption_rate
    global race
    
    print('You see a strange mushroom.')
    print('1 Consume\n2 Leave')
    w = 0
    selection = input('>: ')
    if selection == '1':
        x = random.randint(1, 4)
        if x == 1:
            if race == 'Satyr':
                w = consumption_rate + consumption_rate + consumption_rate
                endurance = endurance + w
                print('You eat the mushroom, and gain ' + str(w) + ' Endurance.')
            else:
                print('You eat the mushroom, and nothing happened.')
        if x == 2:
            if race == 'Satyr':
                w = consumption_rate + consumption_rate + consumption_rate
                endurance = endurance + w
                print('You eat the mushroom, and gain ' + str(w) + ' Endurance.')
            else:
                print('You eat the mushroom, and it causes you to vomit.')
                food_endurance_mechanic()
        if x == 3:
            w = consumption_rate + consumption_rate
            endurance = endurance + w
            print('You eat the mushroom, and gain ' + str(w) + ' Endurance.')
        if x == 4:
            if race == 'Satyr':
                w = consumption_rate + consumption_rate
                endurance = endurance + w
                print('You eat the mushroom, and gain ' + str(w) + ' Endurance.')
            else:
                hp = 0
                endurance = 0
                print('You eat the mushroom, and then fall to the ground, foaming at the mouth.')
                input('Press enter to continue')
                death()

    elif selection == '2':
        print('You leave the mushroom.')
    else:
        mushroom()
    input('Press enter to continue')

### Miracle ###
def miracle():
    global race
    global food
    global max_food
    global arrows
    global max_arrows
    global gold
    global max_gold
    global hp
    global max_hp
    
    if race == 'Halfling':
        print('You see an old wizard, and the wizard beckons you over.')
        print('"Ho, there, traveler!"')
        print('"I did not expect to see a Halfing out in the wilderness."')
        print('"This is delightful. Here, have a gift."')
        print('Fill:\n1 Food\n2 Arrows\n3 Gold\n4 HP')
        selection = input('>: ')
        if selection == '1':
            food = max_food
            food_mechanic
        if selection == '2':
            arrows = max_arrows
            arrows_mechanic
        if selection == '3':
            gold = max_gold
            gold_mechanic
        if selection == '4':
            hp = max_hp
            hp_mechanic
        input('Press enter to continue')
    else:
        nothing()
    
### Bigger Bag ###
def bigger_bag():
    global max_food
    global max_arrows
    global max_gold
    
    y = random.randint(1, 3)
    if y == 1:
        max_food = max_food + 10
        print('You find an empty food storage container on the side of the path, and it holds more food than your current one.')
        input('Press enter to take\n')
        print('Max food increased by 10.')
    if y == 2:
        max_arrows = max_arrows + 10
        print('You spot an empty quiver on the side of the path. It holds more arrows than your current one.')
        input('Press enter to take\n')
        print('Max arrows increased by 10.')
    if y == 3:
        max_gold = max_gold + 100
        print('You discover an empty coin purse on the side of the path. It holds more gold than your current one.')
        input('Press enter to take\n')
        print('Max gold increased by 100.')
    print()
    input('Press enter to continue')

### Lose a Day ###
def lose_day():
    global counter
    global location
    v = random.randint(1, 3)
    #y = random.randint(1, 2)
    #k = random.randint(1, 100)
    counter = counter + v
    #if y == 1:

    print('You realize that you are lost. It will take you ' + str(v) + ' days to get back on the right path.')
    #if y == 2:
        #if location == 'Goodshire' or 'Rodez':
            #print('You arrive at a bridge spanning a massive whitewater river that is guarded by a score of bandits. One bandit approaches you.')
        #elif location == 'Oristano' or 'Thasos' or 'Karabuk':
            #print('You arrive at a bridge spanning an enormous chasm that is guarded by a score of bandits. One bandit approaches you.')
        #print('"If you want to cross this bridge, you have to pay us, ' + str(k) 'gold.\n')
#        print('1 Pay gold\n2 Take a detour\n')
##        selection = input('>: ')
#        if selection == '1':
#            if k > gold:
#            print('"That is not enough to cross, but we will keep what you gave us, and you can find another way around. Have fun out there."')
#            gold = 0
##            else:
 #               gold = gold - k
 #               print('You gave the bandit ' + str(k) + ' gold, and they let you cross the bridge.')
 #       elif selection == '2'
 #       else:
 #           selection = input('>: ')


    input('Press enter to continue')

### Mystic ###
def mystic():
    global name
    global hp
    global max_hp
    global martial_prowess 
    global consumption_rate 
    global endurance 
    global food 
    global max_food 
    global race 
    global luck 
    global arrows 
    global max_arrows
    global speed 
    global occupation 
    global illness 
    global illness_chance 
    global gold
    global max_gold 
    global weapon
    global consumption_rate


    
    print('You come upon a roaming mystic.')
    print('The mystic offers you a blessing.\n')
    print('Increase:\n1 Max HP\n2 Endurance\n3 Martial Prowess\n')
    #print('Fill: ')
    selection = input('>: ')
    os.system('cls')
    if selection == '1':
        max_hp = max_hp + 10
        hp = hp + 10
        print('Your max HP increases by 10.')
        input('Press enter to continue')
    elif selection == '2':
        endurance = endurance + consumption_rate
        print('Your endurance increases by ' + str(consumption_rate) + '.')
        input('Press enter to continue')
    elif selection == '3':
        martial_prowess = martial_prowess + 10
        print('Your martial prowess increases by 10.')
        input('Press enter to continue')
    else:
        mystic()
        

### Nothing ###
def nothing():
    print('Nothing notable happens.')
    input('Press enter to continue')

### Damaged (Random Event) ###
def damaged():
    global hp
    global gold
    global food
    global arrows
    #adventure_menu()
    v = random.randint(1, 20)
    n = random.randint(1, 3)
    hp = hp - v
    
    if n == 1:
        g = random.randint(1, 20)
        gold = gold + g
        print('You sprain your ankle in a divot, taking ' + str(v) + ' damage.')
        print('However, you find ' + str(g) + ' gold on the ground.')
        gold_mechanic()
    if n == 2:
        f = random.randint(1, 20)
        food = food + f
        print('You are stung by a swarm of bees, taking ' + str(v) + ' damage.')
        print('However, you manage to take ' + str(f) + ' honey before you flee.')
        food_mechanic()
        
    if n == 3:
        a = random.randint(1, 20)
        arrows = arrows + a
        print('You walk into an hunter\'s trap, taking ' + str(v) + ' damage.')      
        print('However, you find ' + str(a) + ' arrows nearby.')
        arrows_mechanic()

    
    input('Press enter to continue')
    hp_mechanic()

### Traveller ###
def traveller():
    global gold
    global arrows
    global food
    global hp
    print('A friendly adventurer approaches you and wants to trade.')
    n = random.randint(1, 3)
    if n == 1:
        print('"Good morning, traveler."\n')
    if n == 2:
        print('"Good evening, traveler."\n')
    if n == 3:
        print('"Good afternoon, traveler."\n')

    traveller_values()

# Traveller Values #
def traveller_values():
    
    traveller_generation()
    input('Press enter to continue')
    


#### Traveller Generation ####
def traveller_generation():
    global gold
    global arrows
    global food
    global hp
    x = random.randint(1, 50) # how much trader wants
    v = random.randint(1, 100) #how much trader is willing to give
    c = random.randint(1, 4) # what trader wants

    if c == 1:
        print('The trader wants ' + str(x) + ' food.')
        p = random.randint(1, 3) # what trader is giving
        if p == 1:
            print('The trader is willing to give ' + str(v) + ' arrows.')
            print('1 Accept\n2 Decline')
            selection = input('>: ')
            if selection == '1':
                if food < x:
                    print('You cannot afford the trade.')        
                else:
                    food = food - x
                    arrows = arrows + v
                    print('You accept the trade.')
                    arrows_mechanic()
                    
            else:
                print('You decline the trade.')
                
        if p == 2:
            print('The trader is willing to pay ' + str(v) + ' gold.')
            print('1 Accept\n2 Decline')
            selection = input('>: ')
            if selection == '1':
                if food < x:
                    print('You cannot afford the trade.')        
                else:
                    food = food - x
                    gold = gold + v
                    print('You accept the trade.')
                    gold_mechanic()
                    
            else:
                print('You decline the trade.')
                
        if p == 3:
            print('The trader is willing to heal you ' + str(v) + ' HP.')
            print('1 Accept\n2 Decline')
            selection = input('>: ')
            if selection == '1':
                if food < x:
                    print('You cannot afford the trade.')        
                else:
                    food = food - x
                    hp = hp + v
                    print('You accept the trade.')
                    hp_mechanic()
                    
            else:
                print('You decline the trade.')
    if c == 2:
        print('The trader wants ' + str(x) + ' arrows.')
        p = random.randint(1, 3) # what trader is giving
        if p == 1:
            print('The trader is willing to give ' + str(v) + ' food.')
            print('1 Accept\n2 Decline')
            selection = input('>: ')
            if selection == '1':
                if arrows < x:
                    print('You cannot afford the trade.')        
                else:
                    arrows = arrows - x
                    food = food + v
                    print('You accept the trade.')
                    food_mechanic()
                    
            else:
                print('You decline the trade.')
        if p == 2:
            print('The trader is willing to give ' + str(v) + ' gold.')
            print('1 Accept\n2 Decline')
            selection = input('>: ')
            if selection == '1':
                if arrows < x:
                    print('You cannot afford the trade.')        
                else:
                    arrows = arrows - x
                    gold = gold + v
                    print('You accept the trade.')
                    gold_mechanic()
                    
            else:
                print('You decline the trade.')
        if p == 3:
            print('The trader is willing to heal you for ' + str(v) + ' HP.')
            print('1 Accept\n2 Decline')
            selection = input('>: ')
            if selection == '1':
                if arrows < x:
                    print('You cannot afford the trade.')        
                else:
                    arrows = arrows - x
                    hp = hp + v
                    print('You accept the trade.')
                    hp_mechanic()
                    
            else:
                print('You decline the trade.')
    if c == 3:
        print('The trader wants ' + str(x) + ' gold.')
        p = random.randint(1, 3) # what trader is giving
        if p == 1:
            print('The trader is willing to give ' + str(v) + ' food.')
            print('1 Accept\n2 Decline')
            selection = input('>: ')
            if selection == '1':
                if gold < x:
                    print('You cannot afford the trade.')        
                else:
                    gold = gold - x
                    food = food + v
                    print('You accept the trade.')
                    food_mechanic()
        
            else:
                print('You decline the trade.')
        if p == 2:
            print('The trader is willing to give ' + str(v) + ' arrows.')
            print('1 Accept\n2 Decline')
            selection = input('>: ')
            if selection == '1':
                if gold < x:
                    print('You cannot afford the trade.')        
                else:
                    gold = gold - x
                    arrows = arrows + v
                    print('You accept the trade.')
                    arrows_mechanic()
                    
            else:
                print('You decline the trade.')

        if p == 3:
            print('The trader is willing to heal you ' + str(v) + ' HP.')
            print('1 Accept\n2 Decline')
            selection = input('>: ')
            if selection == '1':
                if gold < x:
                    print('You cannot afford the trade.')        
                else:
                    gold = gold - x
                    hp = hp + v
                    print('You accept the trade.')
                    hp_mechanic()
                    
            else:
                print('You decline the trade.')        
    if c == 4:
        print('The trader wants your blood. Specifically, ' + str(x) + ' HP.')
        p = random.randint(1, 3) # what trader is giving
        if p == 1:
            print('The trader is willing to give ' + str(v) + ' food.')
            print('1 Accept\n2 Decline')
            selection = input('>: ')
            if selection == '1':
                if hp < x:
                    print('You cannot afford the trade, but the trader will accept what you have.')        
                    hp = hp - x
                    food = food + v
                    food_mechanic()
                else:
                    hp = hp - x
                    food = food + v
                    print('You accept the trade.')
                    food_mechanic()
                    
            else:
                print('You decline the trade.')
        if p == 2:
            print('The trader is willing to give ' + str(v) + ' arrows.')
            print('1 Accept\n2 Decline')
            selection = input('>: ')
            if selection == '1':
                if hp < x:
                    print('You cannot afford the trade, but the trader is willing to let you slide, this time.')        
                    hp = hp - x
                    food = food + v
                    food_mechanic()
                else:
                    hp = hp - x
                    arrows = arrows + v
                    print('You accept the trade.')
                    arrows_mechanic()
                    
            else:
                print('You decline the trade.')
        if p == 3:
            print('The trader is willing to give ' + str(v) + ' gold.')
            print('1 Accept\n2 Decline')
            selection = input('>: ')
            if selection == '1':
                if hp < x:
                    print('You cannot afford the trade, but the trader is willing to let you slide, this time.')        
                    hp = hp - x
                    food = food + v
                    food_mechanic()
                else:
                    hp = hp - x
                    gold = gold + v
                    print('You accept the trade.')
                    gold_mechanic()

            else:
                print('You decline the trade.')

    

### Robbed ###
def robbed():
    global gold
    global arrows
    global food

    x = random.randint(1, 3)
    if food == 0 and arrows == 0 and gold == 0:
        nothing()
    elif x == 1: 
        v = random.randint(1, 50) 
        if food < v:
            v = food

        food = food - v
        food_mechanic()
        y = random.randint(1, 2)
        #adventure_menu()
        if y == 1:
            print('During the night, a shadowy figure stole ' + str(v) + ' of your food.')
        elif y == 2:
            print('You check your food supply and find that ' + str(v) + ' food is missing.')   
    elif x == 2:
        v = random.randint(1, 50)
        if arrows < v:
            v = arrows
        arrows = arrows - v
        arrows_mechanic()
        y = random.randint(1, 2)
        #adventure_menu()
        if y == 1:
            print('During the night, a shadowy figure stole ' + str(v) + ' of your arrows.')
        elif y == 2:
            print('You check your arrow quill, and find that ' + str(v) + ' arrows are missing.') 
        
    elif x == 3:
        v = random.randint(1, 50)
        if gold < v:
            v = gold
        gold = gold - v
        gold_mechanic()
        y = random.randint(1, 2)
        #adventure_menu()
        if y == 1:
            print('During the night, a shadowy figure stole ' + str(v) + ' of your gold.')
        elif y == 2:
            print('You check your coin purse, and find that ' + str(v) + ' gold is missing.')

    v = 0
    x = 0
    
    input('Press enter to continue')

# Doppelganger #
def doppelganger():
    global enemy_type
    global weapon
    global name

    if enemy_type == 'Doppelganger':
        print('The doppelganger is wielding a ' + weapon + ' exactly like yours.')

### Fight ###
def fight():
    global hp
    global martial_prowess
    global weapon
    global durability
    global gold
    global enemy_adjective
    global enemy_type
    global enemy_battlescore
    global enemy_gold
    global counter


    enemy_generator()
    print('You see a ' + enemy_adjective + ' ' + enemy_type + ' approaching.')
    doppelganger()
    print('1 Fight\n2 Flee')
    selection = input('>: ')
    if selection == '1':
        fight_simulation()
        counter = counter - 1
        adventuring()
            
    if selection == '2':
        flee_fight()
        counter = counter - 1
        adventuring()

    else:
        flee_fight()
        counter = counter - 1
        adventuring()
    
# Fight Simulation #
def fight_simulation():
    global hp
    global martial_prowess
    global weapon
    global gold
    global enemy_adjective
    global enemy_type
    global enemy_battlescore
    global enemy_gold
    global enemy_arrows
    global enemy_food
    global damage_taken

    your_damage_taken()
    enemy_loot()

    input('Press enter to continue')
    #adventure_menu()

# Enemy Loot #
def enemy_loot():
    global gold
    global arrows
    global food
    global enemy_gold
    global enemy_arrows
    global enemy_food
    
    f = random.randint(1, 10)
    enemy_food = enemy_food + f
    food = food + enemy_food
    a = random.randint(1, 5)
    enemy_arrows = enemy_arrows + a
    arrows = arrows + enemy_arrows
    g = random.randint(1, 10)
    enemy_gold = enemy_gold + g
    gold = gold + enemy_gold
    print('You found ' + str(enemy_food) + ' food, ' + str(enemy_arrows) + ' arrows, and ' + str(enemy_gold) + ' gold on the corpse.')    
    food_mechanic()
    arrows_mechanic()
    gold_mechanic()

# Your Damage Taken #
def your_damage_taken():
    global hp
    global martial_prowess
    global enemy_battlescore
    global damage_taken

    damage_taken = enemy_battlescore - martial_prowess
    hp = int(hp - damage_taken)
    if damage_taken < 1:
        hp = hp + damage_taken
        damage_taken = 0
        print('The enemy was slain, and you took no damage.')
    else:
        print('The enemy was slain, but you took ' + str(damage_taken) + ' damage.')

# Flee Fight #
def flee_fight():
    n = random.randint(1, 2)
    if n == 1:
        print('You escaped the fight.')
        input('Press enter to continue')
        adventure_menu()
    elif n == 2:    
        print('You failed to flee the fight.')
        input('Press enter to continue')
        fight_simulation()

# Enemy Generator #
def enemy_generator():
    global enemy_adjective
    global enemy_type
    global enemy_battlescore

    enemy_resetter()
    enemy_adjective_generator()
    enemy_type_generator()
    
# Enemy Resetter #
def enemy_resetter():
    global enemy_type
    global enemy_battlescore
    global enemy_gold
    global enemy_food
    global enemy_arrows
    global enemy_specific_gold
    global enemy_specific_arrows
    global enemy_specific_food

    enemy_type = ''
    enemy_food = 0
    enemy_arrows = 0
    enemy_gold = 0
    enemy_specific_gold = 0
    enemy_specific_arrows = 0
    enemy_specific_food = 0
    enemy_battlescore = 0
    enemy_adjective = ''

### Enemy Locater and Excluder Generator ###
def enemy_locater_generator():
    global enemy_locater
    global location
    global enemy_exclude
    global enemy_number
    
    if location == 'Goodshire':
        enemy_locater = 'Goodshire'
        enemy_exclude = [3,4,5]
    if location == 'Rodez':
        enemy_locater = 'Rodez'
        enemy_exclude = [2,4,5]
    if location == 'Oristano':
        enemy_locater = 'Oristano'
        enemy_exclude = [1,2,5]
    if location == 'Thasos':
        enemy_locater = 'Thasos'
        enemy_exclude = [1,2]
    if location == 'Karabuk':
        enemy_locater = 'Karabuk'
        enemy_exclude = [1,2,3]
    if location == 'Last Refuge':
        enemy_locater = 'Last Refuge'
        enemy_exclude = [2,3]
    enemy_number = random.randint(1, 5)
    while enemy_number in enemy_exclude:
        enemy_number = random.randint(1, 5)

# Enemy Type Generator #
def enemy_type_generator():
    global enemy_type
    global enemy_battlescore
    global enemy_gold
    global enemy_food
    global enemy_arrows
    global enemy_specific_gold
    global enemy_specific_arrows
    global enemy_specific_food
    global enemy_locater
    global enemy_exclude
    global enemy_number

    enemy_locater_generator()    

    if enemy_number == 1:
        enemy_type = 'Lone Wolf'
        enemy_battlescore = enemy_battlescore + 35
        enemy_specific_food = 2
        enemy_specific_arrows = 0
        enemy_specific_gold = 0
        enemy_food = enemy_food + enemy_specific_food
        enemy_arrows = enemy_arrows + enemy_specific_arrows
        enemy_gold = enemy_gold + enemy_specific_gold
        
        
    if enemy_number == 2:
        enemy_type = 'Large Maggot'
        enemy_battlescore = enemy_battlescore + 15
        enemy_specific_food = 1
        enemy_specific_arrows = 0
        enemy_specific_gold = 0
        enemy_food = enemy_food + enemy_specific_food
        enemy_arrows = enemy_arrows + enemy_specific_arrows
        enemy_gold = enemy_gold + enemy_specific_gold
        
    if enemy_number == 3:
        enemy_type = 'Rogue Vampire'
        enemy_battlescore = enemy_battlescore + 55
        enemy_specific_food = 0
        enemy_specific_arrows = 0
        enemy_specific_gold = 5
        enemy_food = enemy_food + enemy_specific_food
        enemy_arrows = enemy_arrows + enemy_specific_arrows
        enemy_gold = enemy_gold + enemy_specific_gold
        
        
    if enemy_number == 4:
        enemy_type = 'Dark Cultist'
        enemy_battlescore = enemy_battlescore + 85
        enemy_specific_food = 10
        enemy_specific_arrows = 0
        enemy_specific_gold = 10
        enemy_food = enemy_food + enemy_specific_food
        enemy_arrows = enemy_arrows + enemy_specific_arrows
        enemy_gold = enemy_gold + enemy_specific_gold

    if enemy_number == 5:
        enemy_type = 'Doppelganger'
        enemy_battlescore = enemy_battlescore + 105
        enemy_specific_food = 10
        enemy_specific_arrows = 0
        enemy_specific_gold = 10
        enemy_food = enemy_food + enemy_specific_food
        enemy_arrows = enemy_arrows + enemy_specific_arrows
        enemy_gold = enemy_gold + enemy_specific_gold

    

# Enemy Adjective Generator #
def enemy_adjective_generator():
    global enemy_adjective
    global enemy_battlescore

    j = random.randint(1, 3)
    if j == 1:
        enemy_adjective = 'Bloodthirsty'
        enemy_battlescore = enemy_battlescore + 35
    if j == 2:
        enemy_adjective = 'Regular'
        enemy_battlescore = enemy_battlescore + 0
    if j == 3:
        enemy_adjective = 'Starved'
        enemy_battlescore = enemy_battlescore - 10

### Chest ###                 
def chest():
    global hp
    global max_hp

    p = random.randint(1, 2)
    if p == 1:
        print('You see a treasure chest.')
    if p == 2:    
        print('You see a large hollow tree.')
    print('1 Inspect\n2 Avoid')
    selection = input('>: ')
    if selection == '1':
        a = random.randint(1, 3)
        if a == 1:
            print('It is empty. Nothing but cobwebs remain.')
            input('Press enter to continue')
            adventure_menu()
        if a == 2:
            print('It was booby trapped. A dart flies out and hits you for 20 damage.')
            hp = hp - 20  
            input('Press enter to continue')
            hp_mechanic()
            adventure_menu()
        #if a == 2 and luck > 0:
            #print('It was booby trapped. A dart flies out and hits you for 20 damage.')
            #chestloot()
        if a == 3:
            chest_loot()

    elif selection == '2':
        print()

    else:
        chest()

# Chest Loot #
def chest_loot():
    global gold
    global arrows
    global food
    global max_food
    
    x = random.randint(1, 3)
    if x == 1: 
        v = random.randint(50, 100)
        food = food + v
        print('Inside, you found ' + str(v) + ' food.')
        food_mechanic()
    if x == 2:
        v = random.randint(50, 100)
        arrows = arrows + v
        print('Inside, you found ' + str(v) + ' arrows.')
        arrows_mechanic()
    if x == 3:
        v = random.randint(50, 100)
        gold = gold + v
        print('Inside, you found ' + str(v) + ' gold.')
        gold_mechanic()

    v = 0
    input('Press enter to continue')
    adventure_menu()

####### Salem #######
def salem():
    global counter
    global adventure_state
    global damage_taken
    global enemy_battlescore
    global martial_prowess
    global hp

    os.system('cls')
    print('-----------------')
    print('| G |   |   |   |')
    print('+---+---+---+---+')
    print('| R |   |   |   |')
    print('+---+---+---+---+')
    print('|   | O |   |   |')
    print('+---+---+---+---+')
    print('|   | T | K |   |')
    print('+---+---+---+---+')
    print('|   |   |   | S |')
    print('+---------------+\n')
    print('Salem\n')
    input('Press enter to continue')
    os.system('cls')

    print('You enter the ancient city of Salem, now blackened with fire and as silent as a graveyard, and see a man who looks like a commoner lounging upon a throne of skeletons in the courtyard.')
    print('"Ah, ' + name + '", I was expecting you."\n')
    print('Type \'who are you?\'')
    input('>: ')

    os.system('cls')
    print('"I am the called by your order the Antipope or the Prince of Darkness, but my birth name is Chernobog."')
    print('"As you can see, I have already razed Salem. Your sacred temples and artifacts are totally destroyed. You have failed."')
    print('"But I admire your willpower and resourcefulness to make it all the way here from Goodshire."')
    print('"I want to make you an offer. Join me, and become my champion. Together, we will forge a New Dawn."')
    print('"Your old ways are gone. You have failed your order, and they will no longer accept you."')
    print('"If you decline, I won\'t kill you, but I will beat you within an inch of your life and enslave you for eternity."\n')
    print('"The choice is yours, ' + name + '."\n')
    print('1 Accept offer\n2 Decline offer\n')
    selection = input('>: ')
    os.system('cls')

    if selection == '1':
        char_menu()
        print('You join the forces of Chernobog, the Prince of Darkness, and forsake your old way of life. You both combine your powers and forge a New Dawn.')
        print()
        input('Press enter to end game')
        title_screen()

    elif selection == '2':
        print('"Very well, then." Chernobog stands up.')
        input('Press enter to fight')

        enemy_battlescore = 170
        damage_taken = enemy_battlescore - martial_prowess
        hp = int(hp - damage_taken)
        if hp > 0:
            print('You have slain the Antipope. His body magically lights on fire, and leaves ashes on the ground.')
            print('Your surroundings shimmer, and the city of Salem transforms from its ruined state to its former glory. You have succeeded in every goal.')
            input('Press enter to continue')
            char_menu()
            os.system('cls')
            print('You win!')
            
            print('Occupation: ' + occupation + '')
            input('Press enter to end game')
            title_screen()
            
        else:
            hp = 0.1
            char_menu()
            print()
            print('You have lost the fight, letting Chernobog win. He enslaves you for all eternity, and he takes over the world.\n')
            input('Press enter to end game')
            title_screen()

    else:
        salem()


title_screen()
