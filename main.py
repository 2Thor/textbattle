# ------------ imports ------------
import os
import random
from character import Hero, Enemy
from weapon import Weapon, short_bow, iron_sword

# ------------ setup ------------
hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)

# Randomly select a weapon for the enemy from all available weapon instances
enemy_weapon = random.choice(Weapon.instances)
enemy = Enemy(name="Enemy", health=100, weapon=enemy_weapon)

# ------------ game loop ------------
while True:
    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()
    
    input()
