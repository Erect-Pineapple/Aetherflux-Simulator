# -*- coding: utf-8 -*-
"""
Updated on Sun Feb 04 2021

@author: Paul
"""
def whole_number_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            # break can also be here instead of else
        except ValueError:
            print("Please enter a whole number.")
        else:
            break
    return value

def flux(spells,life=0,prev_spells=0,bowls=1):
    """
    Recursive function for Aetherflux calculation.
    Returns life after casting X spells.
    spells: positive integer
    """
    assert spells > -1 ,'Cannot cast negative spells'
    if spells == 0:
        return life
    else:
        newlife = life + ((spells + flux(spells-1) + prev_spells*spells)*bowls)
        return newlife

# iterative version of flux.  Not used currently.
def fishbowl(starting_life, spells_cast, previous_spells = 0, bowls = 1):
    """
    Returns to updated life total after casting spells and gaining life from 
    Aetherflux Reservoir after casting spells_cast spells.
    starting_life: int, how much life you have before casting spells
    spells_cast: int, how many spells you can cast this turn
    previous_spells: int, spells cast beforehand
    bowls:int, number of Aetherflux Reservoirs controlled before casting.   
    """
    assert spells_cast > -1, "Cannot cast a negative number of spells."
    life = starting_life
    for count in range(1, spells_cast + 1):
        life +=  bowls * (count + previous_spells)
    return life


def lasers(life, enemies):
    """
    Prints
    """
    
    print("You have", life, "Life to shoot with")
    print(enemies)

    while True:
        forenemies = enemies.copy()
        for x in forenemies:
            if forenemies[x] != min(enemies.values()):
                continue
            elif life > 50:
                life -= 50
                enemies[x] -= 50
                print("shot at", x, life, "life remaining")
                print(enemies)             
                if enemies[x] < 1:
                    del(enemies[x])
                    print(x,"is dead")
                    if len(enemies) != 0:
                        print(enemies)
                    else:
                        print("All enemies are dead, with", life, "life remaining")
                        break
        if life <= 50:
            print("Laser out of power.", life, "life remaining")
            break
        elif len(enemies) <= 0:
            break
    return life
                

p = whole_number_input("How many enemies? ")
enemies = {}
for x in range(1, p+1):
  name = input("Enemy Name " + str(x) + ": ")
  enemies[name] = whole_number_input(name + "'s life total:")
life = int(input("What life are you at? "))
prev_spells = 0
bowls = 1
while True:
    userinput = input('''Enter a number to cast that many spells (1 default), shoot to shoot your LAZOR, bowl to add a bowl,
or eot to end your turn. ''')
    if userinput == "eot":
        prev_spells = 0
        print("Previous spells reset to 0")
    elif userinput == 'shoot':
        life = lasers(life,enemies)
        if len(enemies) <= 0:
            break
    elif userinput == 'exit':
        break
    elif userinput == 'bowl':
        bowls += 1
        print("Added another Aetherflux. ", bowls, "total.")
    else:
        try:
            userinput = int(userinput)
        except:
            life = flux(1,life,prev_spells,bowls)
            prev_spells += 1
            print("Your new life is", life, "with", prev_spells,"spells cast.")
        else:
            life = flux(userinput,life,prev_spells,bowls)
            prev_spells += userinput
            print("Your new life is", life, "with", prev_spells,"spells cast.")
