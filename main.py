from HomeWorks.homework1 import Hero
from HomeWorks.homework2 import Archer
from random import randint
from abc import abstractmethod


class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.__random_int = randint(1, 3)

    def attack(self):
        print(f"{self.name} наносит урон 20")

    def protection(self):
        print(f"{self.name} защищается")

    def __heal_hp(self):
        return randint(1, 100)

    def rest(self):
        add_hp = self.__heal_hp()
        print(f"В ожидании пополнена жизнь + {add_hp}")
        self.hp += add_hp

    def get_random_int(self):
        return self.__random_int

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass


def main():
    # spider_man = Hero("Peter Parker", 11, 100)
    #
    # spider_man.introduce()
    # print(str(spider_man))
    #
    # Домашнее задание 2 (Наследование, полиморфизм)
    #
    # Экземпляр класса Archer
    lara_croft = Archer("Lara Croft", 1, 100, 5, 30, 'female')

    for i in range(1, 7):
        if not lara_croft.attack():
            print(f"Нехватает стрел!!!")

    print(f"{lara_croft.status()}")
    lara_croft.rest()
    print(f"{lara_croft.status()}")
    lara_croft.setPrecision(80)
    print(f"{lara_croft.status()}")
    lara_croft.attack()




# Точка входа приложения
# main()
