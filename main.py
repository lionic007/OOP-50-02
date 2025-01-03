# OOP

# First class


# class

class Person:

    # Магический метод
    def __init__(self, name, age=0, city="None"):
        # Атрибуты класса
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет меня зовут {self.name} мне {self.age} я живу в {self.city}.")

    def __str__(self):
        return f"Вернул имя объекта {self.name}"

# Экземпляры класса или объекты
person_first = Person("Ардагер", 25, "Sokiluk")
person_second = Person(name="John Doe", age=33, city="Osh")

person_first.introduce()
print(f"Прямой доступ к полям объекта!!!", person_first.age)
person_second.introduce()
