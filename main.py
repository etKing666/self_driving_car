from abc import ABC, abstractmethod
from time import sleep
from sys import exit

#Defining interfaces:

class SO_Control_Unit(ABC):
    """Control unit stores all the critical information and manages the car."""

    def __init__(self, users, obstacles, log, status=False, car_info):
        self._users = users
        self._obstacles = obstacles
        self._log = log
        self._status = status
        self._car_info = car_info

    @abstractmethod
    def auth(self, user):
        # Authenticates user
        raise NotImplementedError #Since it is more descriptive, we raise NotImplementedError instead of "pass"

    @abstractmethod
    def start_car(self):
        raise NotImplementedError

    @abstractmethod
    def accelerate(self):
        raise NotImplementedError

    @abstractmethod
    def brake(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError

    @abstractmethod
    def eval_sign(self):
        #Evaluates traffic signs detected
        raise NotImplementedError

    @abstractmethod
    def eval_veh(self):
        #Evaluates other vehicles detected
        raise NotImplementedError

    @abstractmethod
    def eval_obs(self):
        #Evaluates obstacles detected
        raise NotImplementedError

    @property
    @abstractmethod
    def status(self):
        raise NotImplementedError

    @status.setter
    @abstractmethod
    def status(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def users(self):
        raise NotImplementedError

    @users.setter
    @abstractmethod
    def users(self, value):
        raise NotImplementedError

    @property
    @abstractmethod
    def obstacles(self):
        raise NotImplementedError

    @obstacles.setter
    @abstractmethod
    def obstacles(self, value):
        raise NotImplementedError

    @property
    @abstractmethod
    def car_info(self):
        raise NotImplementedError

    @car_info.setter
    @abstractmethod
    def car_info(self, value):
        raise NotImplementedError

    @car_info.deleter
    @abstractmethod
    def car_info(self):
        raise NotImplementedError

class Smart_Vehicle(ABC):
    def __init__(self, type, direction, lane, velocity=0):
        self._type = type
        self._velocity = velocity
        self._direction = direction
        self._lane = lane

        @property
        @abstractmethod
        def type(self):
            raise NotImplementedError

        @type.setter
        @abstractmethod
        def type(self, value):
            raise NotImplementedError

        @property
        @abstractmethod
        def velocity(self):
            raise NotImplementedError

        @velocity.setter
        @abstractmethod
        def velocity(self, value):
            raise NotImplementedError

        @property
        @abstractmethod
        def direction(self):
            raise NotImplementedError

        @direction.setter
        @abstractmethod
        def direction(self, value):
            raise NotImplementedError

        @property
        @abstractmethod
        def lane(self):
            raise NotImplementedError

        @lane.setter
        @abstractmethod
        def lane(self, value):
            raise NotImplementedError

class Sensor(ABC):
    def __init__(self, types, obstacle=None):
        self._types = types
        self._obstacle = obstacle # A list to store the information about the detected obstacle

    @abstractmethod
    def detect(self):
        raise NotImplementedError

    @abstractmethod
    def send_data(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def obstacle(self):
        raise NotImplementedError

class Comms_Module(ABC):
    def __init__(self, veh_types=None, vehicles=None):
        veh_types = {}
        vehicles = []

    @abstractmethod
    def get_data(self):
        raise NotImplementedError

    @abstractmethod
    def update_db(self):
        raise NotImplementedError

class Obstacles(ABC):
    def __init__(self, type, lane):
        self._type = type
        self._lane = lane # Refers to the lane on the road where the obstacle is located

    @property
    @abstractmethod
    def type(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def lane(self):
        raise NotImplementedError

class System_User(ABC):
    def __init__(self, name, surname, username):
        self._name = name
        self._surname = surname
        self._username = username

    @abstractmethod
    def turn_on(self):
        # Turns on the car
        raise NotImplementedError

    @property
    @abstractmethod
    def username(self):
        raise NotImplementedError

class Sign_Recognition_System(ABC):
    def __init__(self, sign_data):
        self._sign_data = sign_data

    @abstractmethod
    def detect_sign(self):
        raise NotImplementedError

    @abstractmethod
    def check_db(self):
        raise NotImplementedError

    @abstractmethod
    def send_data(self):
        raise NotImplementedError

class Traffic_Sign(ABC):
    def __init__(self, type):
        self._type = type

    @property
    @abstractmethod
    def type(self):
        raise NotImplementedError

class Sign_DB(ABC):
    def __init__(self, signs):
        self.signs = signs

    @abstractmethod
    def check_sign(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def list_signs(self):
        raise NotImplementedError

# Creating classes:

class Vehicle(Smart_Vehicle):
    def __init__(self, type, direction, lane, velocity=0):
        self._type = type
        self._velocity = velocity
        self._direction = direction
        self._lane = lane

    @property
    def type(self):
        return self.type

    @type.setter
    def type(self, value):
        self.type = value

    @property
    def velocity(self):
        return self.velocity

    @velocity.setter
    def velocity(self, value):
        self.velocity = value

    @property
    def direction(self):
        return self.direction

    @direction.setter
    def direction(self, value):
        self.direction = value

    @property
    def lane(self):
        return self.lane

    @lane.setter
    def lane(self, value):
        self.lane = value

class Car(Vehicle):
    def print_state(self):
        print(f"Car type: {self.type}")
        print(f"Velocity: {self.velocity}")
        print(f"Direction: {self.direction}")
        print(f"Lane: {self.lane}")


class Control_Unit(SO_Control_Unit):
    def __init__(self, users, obstacles=None, status=False, log=None, car_info=None):
        self._users = users
        self._obstacles = []
        self._status = status
        self._log = log
        self._car_info = []

    def add_user(self):
        new_user = (input("Please enter the username of the user: "))
        if new_user in self._users:
            print("The username already exists! Returning to the main menu.")
            sleep(2)
            main_menu()
        else:
            self._users.add(new_user) # Adding username to the user database
            print("The user has been added! Returning to the main menu.")
            sleep(2)
            main_menu()

    def auth(self, user):
        # Authenticates user
        raise NotImplementedError #Since it is more descriptive, we raise NotImplementedError instead of "pass"

    def start_car(self):
        raise NotImplementedError

    def accelerate(self):
        raise NotImplementedError

    def brake(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def eval_sign(self):
        #Evaluates traffic signs detected
        raise NotImplementedError

    def eval_veh(self, type, direction, lane, velocity):
        # Compares the car's information against the vehicle detected
        if self._car_info[1] != direction: # Compares the direction
            if self._car_info[2] == 1:
                self._car_info[2] == 2
                car.lane == 2
                print("The car changed its lane from 1 to 2.")
            elif self._car_info[2] == 2:
                if self._car_info[3] < 80: # If the velocity is less than 80, car changes its lane to the slowest one.
                    self._car_info[2] == 1
                    car.lane == 1
                    print("The car changed its lane from 2 to 1.")
                self._car_info[2] == 3
                car.lane == 3
                print("The car changed its lane from 2 to 3.")
            else:
                self._car_info[2] == 2
                car.lane == 2
                print("The car changed its lane from 3 to 2.")
        else:
            print("A car coming from opposite direction is detected. Since it is on a different lane, car did not change "
                  "its lane and continued the trip.")


        """ BURADA KALDIK. CAR INFO'YU GERİ NASIL GÜNCELLEYECEĞİZ? BELKİ DE BURADAN DOĞRUDAN NESNEYİ DEĞİŞTİRİZ
        GETTER VE SETTER METHODLARI VAR SONUÇTA."""
        raise NotImplementedError

    def eval_obs(self):
        #Evaluates obstacles detected
        raise NotImplementedError

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, value):
        self._users.add(value)

    @property
    def obstacles(self):
        return self._obstacles

    @obstacles.setter
    def obstacles(self, value):
        self._obstacles = value

    @property
    def car_info(self):
        return self._car_info

    @car_info.setter
    def car_info(self, value):
        self._car_info.append(value)

    @car_info.deleter
    def car_info(self):
        del self._car_info

class User(System_User):

    def __init__(self, name, surname, username):
        self._name = name
        self._surname = surname
        self._username = username

    def turn_on(self):
        if Control_Unit.status == True:
            print("The car is already turned on!")
        else:
            Control_Unit.status = True

    # Only a getter for username is added because no other attributes will be called for and be amended in the program.
    @property
    def username(self):
        return self._username

class Lidar(Sensor):
    def __init__(self, types=None, obstacle=None):
        self._types = {1: 'rock', 2: 'pedestrian', 3: 'animal', 4: 'trash', 5: 'traffic cone'} # Obstacle type database
        self._obstacle = []

    def detect(self):
        """Detects the traffic sign."""
        type_code = int(input(""" Please select an obstacle to place on the road:
         1. Rock
         2. Pedestrian
         3. Animal
         4. Trash
         5. Traffic cone

         Your selection [1-5]: """))

        lane = int(input(""" Please select a lane to place the obstacle.
        Your selection [1-3]: """))

        # The LiDAR interprets the sign detected (e.g. the code entered by the user) by using obstacle type database.
        for x in self._types.keys():
            if type_code == x:
                type = self._types.get(x)

        # Updating the obstacle data according to the outcome of the detection
        self._obstacle = (Obstacle(type, lane))
        self.send_data() # To send the data to the control unit for processing.
        print(f"The obstacle has been placed on lane {lane}. Please see car log for car's reaction.")
        # Returns to the main menu
        main_menu()

    def send_data(self):
        """Sends the data to the control unit"""
        Control_Unit.obstacles = self._obstacle

    # Only obstacle getter method is written, because the values are set by the detect() method.
    @property
    def obstacle(self):
        return self._obstacle

class Obstacle(Obstacles):
    def __init__(self, type, lane):
        self._type = type
        self._lane = lane # Refers to the lane on the road where the obstacle is located

    @property
    def type(self):
        return self._type

    @property
    def lane(self):
        return self._lane

class V2V_Comms(Comms_Module):
    def __init__(self, veh_types=None, vehicles=None):
        _veh_types = {1: 'Car', 2: 'Van', 3: 'SUV', 4: 'Truck', 5: 'Trailer'}
        _vehicles = []

    def get_data(self):
        """Intercepts incoming communication from nearby vehicles."""
        type_code = int(input(""" Please select a vehicle type to instantiate:
                 1. Car
                 2. Van
                 3. SUV
                 4. Truck
                 5. Trailer

                 Your selection [1-4]: """))

        while True:
            velocity = int(input(""" Please enter the velocity of the vehicle.
                       Enter value [max. 180]: """))
            if velocity <= 180:
                break
            else:
                print("Please enter a valid value [max. 180]")

        # There are only to valid directions in the program: North and South
        while True:
            direction = input(""" Please select the direction the vehicle is moving.
                        Your selection [N or S]: """)
            if lane == "N" or lane == "S":
                break
            else:
                print("Please make a valid choice [N or S]")

        while True:
            lane = int(input(""" Please select a lane the vehicle is on.
                       Your selection [1-3]: """))
            if lane == 1 or lane == 2 or lane == 3:
                break
            else:
                print("Please make a valid choice [1-3]")

        # V2V Comms module interprets the vehicle code it receives to identify yhe type of the vehicle:
        for x in self._veh_types.keys():
            if type_code == x:
                car_type = self._types.get(x)

        # Updating the obstacle data according to the outcome of the detection
        self.update_db(car_type, direction, lane, velocity)
        self.send_data(car_type, direction, lane, velocity)
        print(f"The obstacle has been placed on lane {lane}. Please see car log for car's reaction.")
        # Returns to the main menu
        main_menu()


    def update_db(self, typ, dir, ln, vel):
        self._vehicles.append() = (Vehicle(typ, dir, ln, vel))

    def send_data(self, typ, dir, ln, vel):
        Control_Unit.eval_veh(typ, dir, ln, vel)


# Helper functions

def update_car_info(car):
    # Updates car information in the control unit
    del control_unit.car_info
    control_unit.car_info = car.type
    control_unit.car_info = car._direction
    control_unit.car_info = car._lane
    control_unit.car_info = car._velocity

# Creating objects
admin = User('John', 'Doe', 'admin')
control_unit = Control_Unit({'admin'})
car = Car('Car', 'N', 1)
update_car_info(car)
lidar = Lidar()

# User menu

def user_login():
    print(25 * "=", "WELCOME TO SMART CAR INFORMATION SYSTEM (SCIS)", 24 * "=")
    print("""
        Please enter your username to log in to the system.
        """)
    print("")
    print(97 * "=")
    username = input("Username : ")

    if username in control_unit.users:
        print("You are authorized to use the system!")
        sleep(2)
        main_menu()
    else:
        print("You are not authorized to use the system!")
        sleep(2)
        exit()

def main_menu():
    print(30 * "=", "SMART CAR INFORMATION SYSTEM (SCIS)", 30 * "=")
    print("""
    1. Get information about the car
    2. Interact with the car
    3. Exit
    """)
    print(97 * "=")

    choice = int(input("Please make your choice [1-3] : "))
    while True:
        if choice == 1:
            inf_menu()
        elif choice == 2:
            interact_menu()
        elif choice == 3:
            print("Thank you for using SCIS!")
            sleep(2)
            exit()
        else:
            print("You have entered an invalid choice. Please try again.")
            sleep(2)
            main_menu()

def inf_menu():
    print(30 * "=", "SMART CAR INFORMATION SYSTEM (SCIS)", 30 * "=")
    print("""
    INFORMATION MENU
    
        1. Check the current status of the car
        2. Check the car log
        3. Print out the user list
        4. Return to main menu
        5. Exit the system
        """)
    print(97 * "=")

    choice = int(input("Please make your choice [1-5] : "))
    while True:
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            main_menu()
        elif choice == 5:
            print("Thank you for using SCIS!")
            sleep(2)
            exit()
        else:
            print("You have entered an invalid choice. Please try again.")
            sleep(2)
            inf_menu()


def interact_menu():
    print(30 * "=", "SMART CAR INFORMATION SYSTEM (SCIS)", 30 * "=")
    print("""
    INTERACTION MENU

        1. Start the car
        2. Accelerate
        3. Brake
        4. Place an obstacle
        5. Put a traffic sign
        6. Simulate a car
        7. Stop the car
        8. Add a user
        9. Delete a user
        10. Return to main menu
        11. Exit the system
        """)
    print(97 * "=")

    choice = int(input("Please make your choice [1-11] : "))
    while True:
        if choice == 1:
            pass # Start the car
        elif choice == 2:
            pass # Accelerate
        elif choice == 3:
            pass # Brake
        elif choice == 4:
            lidar.detect()
        elif choice == 5:
            pass  # Put a traffic sign
        elif choice == 6:
            pass  # Car
        elif choice == 7:
            pass  # Stop the car
        elif choice == 8:
            control_unit.add_user()
        elif choice == 9:
            pass  # Delete a user
        elif choice == 10:
            main_menu()
        elif choice == 11:
            print("Thank you for using SCIS!")
            sleep(2)
            exit()
        else:
            print("You have entered an invalid choice. Please try again.")
            sleep(2)
            inf_menu()

user_login()
