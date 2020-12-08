class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'The {self.name} is moving')
    def stop(self):
        print(f'The {self.name} has stopped')
    def turn(self,direction):
        self.direction = direction
        print(f'The {self.name} has turned {self.direction}')
    def show_speed(self):
        print(f'The {self.name} is moving with the speed of {self.speed} m/per hour')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('You are exceeding the speed limit')

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('You are exceeding the speed limit')
class SportCar(Car):
    pass
class PoliceCar(Car):
    pass

police_vehicle = PoliceCar(120,'Black','Police car',True)
sports_car = SportCar(320,'Red','Mustang',False)
work_car = WorkCar(50,'White','Toyota',False)
town_car = TownCar(70,'Grey','BMW','False')

police_vehicle.show_speed()
work_car.show_speed()
town_car.show_speed()
town_car.go()
work_car.turn('right')