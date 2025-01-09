class Hero:
    def __init__(self, name, lvl=1, hp=100):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl} , мое HP {self.hp}.")

    def is_adult(self):
        if self.lvl >= 10:
            return True
        else:
            return False

    def __str__(self):
        return f"Имя {self.name} \n Уровень {self.lvl} \n Жизнь {self.hp}"

    def action(self):
        return f"{self.name} Принял боевую стойку!"

    def attack(self):
        return f"{self} наносит урон 20"