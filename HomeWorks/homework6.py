# # 1) При момоши команды pip создайте файл requirements.txt в вашем проекте 
# # 2) Создайдете файл hw6.py в директории hw
# # 3) В файле hw6.py нужно будет написать:
# #      Написать классы с множественным наследованием используя робмбовидное наследование 

# #      Написать методы на свое усмотрение которые выведут принты в терминал 
# # 4) Все нужно будет сохранить на вашем репозитории и отправить ДЗ виде ссылки на ваш репозиторий 

class Transport:
    def __init__(self, color):
        self.color = color
        self.status = "остановлен"
    
    def start_engine(self):
        self.status = "запущен"
        print(f"Двигатель {self.color} транспорта {self.status}")

class Car(Transport):
    def __init__(self, color, max_speed):
        super().__init__(color)
        self.max_speed = max_speed
    
    def drive(self):
        print(f"{self.color} автомобиль едет со скоростью {self.max_speed} км/ч")
    
    def brake(self):
        print("Автомобиль тормозит")

class Fly(Transport):
    def __init__(self, color, max_speed):
        super().__init__(color)
        self.max_speed = max_speed
        self.altitude = 0
    
    def take_off(self):
        self.altitude = 1000
        print(f"Летательный аппарат взлетел на высоту {self.altitude} метров")
    
    def land(self):
        print("Летательный аппарат приземлился")

class AmphibiousVehicle(Car, Fly):
    def __init__(self, color, max_speed_ground, max_speed_air):
        super().__init__(color, max_speed_ground)
        self.max_speed_air = max_speed_air
        self.mode = "наземный"
    
    def switch_mode(self):
        self.mode = "воздушный" if self.mode == "наземный" else "наземный"
        print(f"Режим изменен на: {self.mode}")
    
    def status_check(self):
        print(f"Состояние: {self.color} амфибия в {self.mode} режиме")

# Пример использования
vehicle = AmphibiousVehicle("красный", 200, 500)
vehicle.start_engine()
vehicle.drive()
vehicle.switch_mode()
vehicle.take_off()
vehicle.status_check()
