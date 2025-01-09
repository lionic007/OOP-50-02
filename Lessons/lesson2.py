# FLAT - Плоская структура
# SRC - Исходный

# from main import * - Плохая практика лучше явно указывать класс
# import main
# import main as m

# Наследование

from HomeWorks.homework1 import Hero


class ShieldHero(Hero):
    """Ни чего не делает"""

    def __init__(self, name: str, hp, lvl, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def introduce(self):
        print(f"А вот фсе! А ФСЕ! Я уже не тот метод{self}")


hr = ShieldHero('Наофуми', 100, 10, 77)

hr.introduce()
hr.is_adult()
