from HomeWorks.homework1 import Hero
from HomeWorks.homework2 import Archer


def main():
    # spider_man = Hero("Peter Parker", 11, 100)
    #
    # spider_man.introduce()
    # print(str(spider_man))

    # Экземпляр класса Archer
    lara_croft = Archer("Lara Croft", 1, 100, 5, 50, 'female')

    lara_croft.attack()
    lara_croft.rest()
    print(f"{lara_croft.status()}")
    lara_croft.setPrecision(90)
    print(f"{lara_croft.status()}")

    for i in range(1, 10):
        lara_croft.setPrecision(i)


# Точка входа приложения
main()
