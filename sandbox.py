class Car:
    def __init__(self, status):
        self.status = status

class User:
    def change_status(self, Car):
        Car.status = True

audi = Car(False)
etkin = User()
etkin.change_status(audi)
print(audi.status)




