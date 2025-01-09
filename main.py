from HomeWorks.homework1 import Hero
from HomeWorks.homework2 import Archer


def main():
    # spider_man = Hero("Peter Parker", 11, 100)
    #
    # spider_man.introduce()
    # print(str(spider_man))

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
main()
