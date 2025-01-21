# Декоратор без аргументов
def simpl_dec(func):  # 2 - создание обертки
    def wrapper():  # 3 -
        print("start")  # 5 -
        func()
        print("end")

    return wrapper  # 4 -


@simpl_dec  # 1 - вызов
def print_text():
    print("hello")


print_text()


# Декораторы с аргументами
def greeting_dec(func):
    def wrapper(name):
        print(f"hello {name}")
        func(name)
        print('By')

    return wrapper


# @simpl_dec
#
# @greeting_dec
# def say
#
# print("WOW")


