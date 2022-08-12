from abc import ABC, abstractmethod
from time import sleep
from sys import exit

#Defining interfaces:

class SO_Control_Unit(ABC):
    """Control unit stores all the critical information and manages the car."""

    def __init__(self, users, obstacles, log, status=False):
        self._users = users
        self._obstacles = obstacles
        self._log = log
        self._status = status

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
    def __init__(self, obstacles, types):
        self._obstacles = obstacles # A list to add obstacle objects
        self._types = types # Do we really need this? Implemented only the getter method.

    @abstractmethod
    def detect(self):
        raise NotImplementedError

    @abstractmethod
    def send_data(self):
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
    def types(self):
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
        self._type = type
        self._lane = lane # Refers to the lane on the road where the obstacle is located

    @property
    @abstractmethod
    def type(self):
        raise NotImplementedError

    @type.setter
    @abstractmethod
    def type(self):
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
    def name(self):
        raise NotImplementedError

    @name.setter
    @abstractmethod
    def name(self, value):
        raise NotImplementedError

    @property
    @abstractmethod
    def surname(self):
        raise NotImplementedError

    @surname.setter
    @abstractmethod
    def surname(self, value):
        raise NotImplementedError

    @property
    @abstractmethod
    def username(self):
        raise NotImplementedError

    @username.setter
    @abstractmethod
    def username(self, value):
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
    def __init__(self, users=None, obstacles=None, status=False, log=None, user_db=None):
        self._users = {'admin'}
        self._obstacles = obstacles
        self._status = status
        self._log = log
        self._user_db = user_db # A list to store user objects

    def add_user(self, user_db=None):
        new_user= []
        new_user[0] = input("Please enter the name of the user: ")
        new_user[1] = input("Please enter the surname of the user: ")
        new_user[2] = input("Please enter the username of the user: ")
        if new_user[2] in users:
            print("The username already exists! Returning to the main menu.")
            sleep(2)
            main_menu()
        else:
            self.users.add(new_user[2]) # Adding username to the user database
            # Creating a new object and storing it to the users dictionary. Key is the username.
            user_db[new_user[2]] = User(new_user[0], new_user[1], new_user[2])
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

    def eval_veh(self):
        #Evaluates other vehicles detected
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
    def users (self, value):
        self._users.add(value)

class User:
    def __init__(self, name, surname, username):
        self._name = name
        self._surname = surname
        self._username = username

    def turn_on(self):
        if Control_Unit.status == True:
            print("The car is already turned on!")
        else:
            Control_Unit.status = True

    def register(self):
        register


# Creating objects

control_unit = Control_Unit()
user = User('John', 'Doe', 'admin')
control_unit.users.add(user)
car = Car('Car', 'N', 1)





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

    choice = int(input("Please make your choice [1-5] : "))
    while True:
        if choice == 1:
            pass # Start the car
        elif choice == 2:
            pass # Accelerate
        elif choice == 3:
            pass # Brake
        elif choice == 4:
            pass  # Place an obstacle
        elif choice == 5:
            pass  # Put a traffic sign
        elif choice == 6:
            pass  # Car
        elif choice == 7:
            pass  # Stop the car
        elif choice == 8:
            pass  # Add a user
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

# user_login()

print(control_unit.users)