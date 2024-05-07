from abc import ABC, abstractmethod


class Monster:
    def __init__(self, name, health, damagePerAttack):
        self.name = name
        self.health = health
        self.damagePerAttack = damagePerAttack

    def attack(self, otherMonster):
        print(f"{self.name}({self.health}) атакует по существу {otherMonster.name}")
        otherMonster.health -= self.damagePerAttack


class Weapon(ABC):
    @abstractmethod
    def attack(self, other):
        pass

class Sword(Weapon):
    def attack(self, other):
        print("атакует мечом", end="")
        other.health -= 10

class Gun(Weapon):
    def attack(self, other):
        print("производит меткий выстрел", end="")
        other.health -= 5

class Bow(Weapon):
    def attack(self, other):
        print("стреляет из лука в колено", end="")
        other.health -= 3

class Fighter:
    def __init__(self, name, health, weapon: Weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def attack(self, otherFighter):
        print(f"{self.name}({self.health})", end="")
        self.weapon.attack(otherFighter)
        print(f" по существу {otherFighter.name}")
    def changeWeapon(self, newWeapon : Weapon):
        self.weapon = newWeapon

def game():
    name = input("Введите имя: ")
    fighter = Fighter(name, 50, Sword())
    monster = Monster("Гоблин", 50, 5)
    while True:

        print("Выберите оружие:")

        print("1. Меч")
        print("2. Лук")
        print("3. Пистолет")
        print("4. Выход")
        choice = int(input("Выберите оружие: "))
        if choice == 1:
            fighter.changeWeapon(Sword())
        elif choice == 2:
            fighter.changeWeapon(Bow())
        elif choice == 3:
            fighter.changeWeapon(Gun())
        elif choice == 4:
            break
        fighter.attack(monster)
        monster.attack(fighter)
        if monster.health <= 0:
            print(f"{fighter.name} победил")
            return
        if fighter.health <= 0:
            print(f"{monster.name} победил")
            return



