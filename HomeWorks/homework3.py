from random import randint
from main import Hero


class Jester(Hero):
    def action(self):
        rnd = self.get_random_int()

        if rnd == 1:
            self.attack()
        elif rnd == 2:
            self.protection()
        elif rnd == 3:
            self.rest()

    def unique_scream(self):
        print(f"{self.name} говорит:> попробуй это!")

    def unique_attack(self):
        print(f"{self.name} делает супер удар!")


# Домашнее задание 3 (Абстракция)
joker = Jester('Jocker', 42, 50)

joker.action()
