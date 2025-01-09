from random import randint
from symtable import Class

from HomeWorks.homework1 import Hero


class Archer(Hero):
    """Класс наследник от родителя Hero"""

    def __init__(self, name: str, lvl: int = 1, hp: int = 100, arrows: int = 5, precision: int = 90,
                 gender: str = 'male'):
        super().__init__(name, lvl, hp)
        self.arrows = arrows
        self.precision = precision
        self.gender = gender

    def attack(self):
        """Переназначенный метод: Проверяет наличие стрел и в случае успеха, наносит атаку с вероятностью precision"""
        if self.arrows < 1: return False

        gender_done_text = "Нанес" if self.gender == 'male' else 'Нанесла'
        gender_fail_text = "Промахнулся" if self.gender == 'male' else 'Промахнулась'

        self.arrows -= 1
        random_attack = randint(1, 100)
        print(f"RANDOM> {random_attack}")
        if random_attack <= self.precision:
            print(f"{self.name} {gender_done_text} урон")
        else:
            print(f"{self.name} {gender_fail_text}")
        return True

    def rest(self):
        """Метод добавления стрел"""
        self.arrows += 5
        print(f"Добавлено 5 стрел")

    def status(self) -> dict:
        """Получить текущие значения экземпляра класса"""
        return dict({
            'name': self.name,
            'hp': self.hp,
            'arrows': self.arrows,
            'precision': self.precision
        })

    def setPrecision(self, precision: int):
        """Установить точность атаки, если достигнуто максимальное число 100 то при превышении будет установлено 100"""
        self.precision = min(100, self.precision + precision)
