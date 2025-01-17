
"""Данная библиотека работает с HTTP запросами"""
import requests


def get_random_pet_facts():
    # Получаем случайный факт о коте
    cat_response = requests.get('https://catfact.ninja/fact')
    cat_fact = cat_response.json()['fact']

    # Получаем случайный факт о собаке
    dog_response = requests.get('https://dog-api.kinduff.com/api/facts')
    dog_fact = dog_response.json()['facts'][0]

    print("🐱 Интересный факт о котах:")
    print(cat_fact)
    print("\n🐶 Интересный факт о собаках:")
    print(dog_fact)


if __name__ == "__main__":
    try:
        print("Ищем интересные факты о питомцах...\n")
        get_random_pet_facts()
    except requests.RequestException:
        print("Ой! Кажется, питомцы сейчас заняты... Попробуйте позже! 🙈")
