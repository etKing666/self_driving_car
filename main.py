from abc import ABC, abstractmethod
from time import sleep
from sys import exit


#Defining interfaces:

class SO_Control_Unit(ABC):
    """Control unit stores all the critical information and manages the car."""

    def __init__(self, users, obstacles, status, log):
        self.users = users
        self.obstacles = obstacles
        self.status = status
        self.log = log

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
    def state(self):
        raise NotImplementedError

    @state.setter
    @abstractmethod
    def state(self):
        raise NotImplementedError

class Smart_Vehicle(ABC):
    def __init__(self, type, velocity, direction, lane):
        self.type = type
        self.velocity = velocity
        self.direction = direction
        self.lane = lane

class Sensor(ABC):
    def __init__(self, obstacles, types):
        self.obstacles = obstacles
        self.types = types

    @abstractmethod
    def detect(self):
        raise NotImplementedError

    @abstractmethod
    def send_data(self):
        raise NotImplementedError

class Comms_Module(ABC):
    @abstractmethod
    def get_data(self):
        raise NotImplementedError

    @abstractmethod
    def update_db(self):
        raise NotImplementedError

class Obstacles(ABC):
    def __init__(self, type, lane):
        self.type = type
        self.lane = lane # Refers to the lane on the road where the obstacle is located

class System_User(ABC):
    def __init__(self, name, surname, username):
        self.name = name
        self.surname = surname
        self.username = username

    @abstractmethod
    def turn_on(self):
        # Turns on the car
        raise NotImplementedError

class Sign_Recognition_System(ABC):
    def __init__(self, sign_data):
        self.sign_data = sign_data

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
        self.type = type

class Sign_DB(ABC):
    def __init__(self, signs):
        self.signs = signs

    @abstractmethod
    def check_sign(self):
        raise NotImplementedError

    @abstractmethod
    def list_signs(self):
        raise NotImplementedError


# Creating classes:

class Vehicle(SmartVehicle):
    def __init__(self, type, velocity, direction, lane):
        self.type = type
        self.velocity = velocity
        self.direction = direction
        self.lane = lane

users = {} # Creating an empty users dictionary in order to store the new user objects in the dictionary

class Control_Unit(SO_Control_Unit):

    def __init__(self, users=None, obstacles=None, status=False, log=None):
        self.users = set()
        self.obstacles = obstacles
        self.status = status
        self.log = log

    def add_user(self):
        new_user= []
        new_user[0] = input("Please enter the name of the user: ")
        new_user[1] = input("Please enter the surname of the user: ")
        new_user[2] = input("Please enter the username of the user: ")
        if new_user[2] in users{}:
            print("The username already exists! Returning to the main menu.")
            sleep(2)
            main_menu()
        else:
            self.users.add(new_user[2]) # Adding username to the user database
            # Creating a new object and storing it to the users dictionary. Key is the username.
            users[new_user[2]] = User(new_user[0], new_user[1], new_user[2])
            print("The user has been added! Returning to the main menu.")
            sleep(2)
            main_menu()


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
    def state(self):
        raise NotImplementedError

    @state.setter
    @abstractmethod
    def state(self):
        raise NotImplementedError

class User:
    pass


# Menus

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
            print("Thank you for using SCIS!")
            sleep(2)
            exit()
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

    pass

def interact_menu():
    print("I am the interaction menu")
    pass

main_menu()