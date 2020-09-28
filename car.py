class Car:
    def __init__(self, make, year_model):
        self.__make= make
        self.__year_model = year_model
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    def get_speed (self):
        return self.__speed
time_machine = Car('ferrari', '1981 dmc-12')
print('\033[4mtime (s)\033[0m    \033[4mSpeed (mph)\033[0m')
for i in range(5):
    time_machine.accelerate()
    speed = time_machine.get_speed()
    print(format(i+1, '4d'), format(speed, '13d'))
for i in range(5):
    time_machine.brake()
    speed = time_machine.get_speed()
    print(format(i+6, '4d'), format(speed,'13d'))
                            
