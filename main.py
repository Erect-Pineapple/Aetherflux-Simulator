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


starting_life = whole_number_input("What is your current life total? ")
while True:
    try:
        spells_cast = whole_number_input("How many spells can you cast? ")
        assert spells_cast > -1, "Cannot cast negative number of spells."
        break
    except:
        print("Cannot cast negative number of spells.")

p = whole_number_input("How many enemies? ")
enemies = {}
for x in range(p):
  name = input("Enemy Name: ")
  enemies[name] = int(input(name + "'s life total:"))



    
def fishbowl(starting_life, spells_cast, previous_spells = 0, bowls = 1):
    """
    Returns updated life total after casting spells and gaining life from 
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
        print(life)
    print("From", starting_life, "starting life, you went to", life, "life after casting", spells_cast, "spells!")
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
        if len(forenemies) == 0:
            print("all enemies are dead, with", life, "life remaining")
            break
        if life <= 50:
            print("Laser out of power.", life, "life remaining")
            break
                

lasers(fishbowl(starting_life, spells_cast), enemies)
