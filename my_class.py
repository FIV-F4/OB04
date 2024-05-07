from abc import ABC, abstractmethod


class Monster:
    def __init__(self, name, health, damagePerAttack):
        self.name = name
        self.health = health
        self.damagePerAttack = damagePerAttack

    def attack(self, otherMonster):
        otherMonster.health -= self.damagePerAttack

class Weapon(ABC):
    @abstractmethod
    def attack(self, other):
        pass

class Sword(Weapon):
    def attack(self, other):
        other.health -= 10
class Gun(Weapon):
    def attack(self, other):
        other.health -= 5

class Bow(Weapon):
    def attack(self, other):
        other.health -= 3

class Fighter:
    def __init__(self, name, health, weapon: Weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def attack(self, otherFighter):
        self.weapon.attack(otherFighter)


fighter = Fighter("Сеня", 100, Gun())
other = 100
fighter.attack(fighter)
print(fighter.health)
