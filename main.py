from abc import ABC, abstractmethod
from time import sleep
from sys import exit
from datetime import datetime

# Defining interfaces:

class SO_Control_Unit(ABC):
    """Control unit stores all the critical information and manages the car."""

    def __init__(self, users, obstacles=None, status=False, log=None):
        self._users = users
        self._obstacles = []
        self._log = log
        self._status = status

    @abstractmethod
    def add_user(self):
        raise NotImplementedError

    @abstractmethod
    def delete_user(self):
        raise NotImplementedError

    @abstractmethod
    def auth(self, user):
        raise NotImplementedError

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
    def change_direction(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError

    @abstractmethod
    def eval_sign(self):
        # Evaluates traffic signs detected
        raise NotImplementedError

    @abstractmethod
    def eval_veh(self):
        # Evaluates other vehicles detected
        raise NotImplementedError

    @abstractmethod
    def eval_obs(self):
        # Evaluates obstacles detected
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

    @abstractmethod
    def add_obstacles(self):
        raise NotImplementedError

    @abstractmethod
    def list_obstacles(self):
        raise NotImplementedError

    @abstractmethod
    def update_log(self):
        raise NotImplementedError

    @abstractmethod
    def read_log(self):
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
        self._obstacle = obstacle  # A list to store the information about the detected obstacle

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

    @abstractmethod
    def list_vehicles(self):
        raise NotImplementedError

    @abstractmethod
    def send_data(self, ):
        raise NotImplementedError


class Obstacles(ABC):
    def __init__(self, type, lane, timestamp):
        self._type = type  # Type of obstacle as evaluated by Lidar
        self._lane = lane  # Refers to the lane on the road where the obstacle is located
        self._timestamp = timestamp  # Date and time of detection

    @property
    @abstractmethod
    def type(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def lane(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def timestamp(self):
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


class T_Sign(ABC):
    def __init__(self, type):
        self._type = type

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
    def desc(self):
        raise NotImplementedError

    @desc.setter
    @abstractmethod
    def desc(self, value):
        raise NotImplementedError


class Sign_DB(ABC):
    def __init__(self, signs):
        self.signs = signs

    @abstractmethod
    def check_sign(self):
        raise NotImplementedError

# Creating classes:

class Vehicle(Smart_Vehicle):
    """
    A vehicle superclass which is instantiated by vehicle objects and subclassed by the car class.
    It only has four attributes and no methods other than getter/setter methods.
    """
    def __init__(self, type, direction, lane, velocity=0):
        self._type = type
        self._velocity = velocity
        self._direction = direction
        self._lane = lane

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = value

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    @property
    def lane(self):
        return self._lane

    @lane.setter
    def lane(self, value):
        self._lane = value


class Car(Vehicle):
    """Subclasses the vehicle superclass and adds one method which allows for printing its state."""
    def print_state(self):
        print(f"Vehicle type: {self.type}")
        print(f"Velocity: {self.velocity}")
        print(f"Direction: {self.direction}")
        print(f"Lane: {self.lane}")


class Control_Unit(SO_Control_Unit):
    """
    Control unit is the central unit which controls all the interaction between the user and all the components
    of the car.
    """
    def __init__(self, users, obstacles=None, status=False, log=None):
        self._users = users
        self._obstacles = []
        self._status = status
        self._log = []

    def add_user(self):
        new_user = (input("Please enter the username of the user: "))
        if new_user in self._users:
            print("The username already exists! Returning to the main menu.")
            self.update_log("Tried to add a new user. The user already exists.")
        else:
            self._users.add(new_user)  # Adding username to the user database
            print("The user has been added! Returning to the main menu.")
            self.update_log(f"The user {new_user} has been added.")

    def delete_user(self):
        del_user = (input("Please enter the username of the user that you want to delete: "))
        if del_user in self._users:
            self._users.remove(del_user)
            print("The username has been deleted from the user database! Returning to the main menu.")
            self.update_log(f"The user {del_user} has been deleted.")
        else:
            print("This user doesn't exist! Returning to the main menu.")
            self.update_log("Tried to delete a user. The user doesn't exist.")

    def auth(self, login):
        if login in control_unit.users:
            print("You are authorized to use the system!\n")
            self.update_log(f"The user '{login}' has been authorized to use the system.")
            sleep(1)
            main_menu()
        else:
            print("You are not authorized to use the system!\n")
            self.update_log("Unauthorized attempt to access the system.")
            sleep(1)
            exit()

    def start_car(self, vehicle):
        if self.status:
            print("\nThe car has already been started. It is not possible to start it again.\n")
            sleep(1)
        else:
            self.status = True
            vehicle.velocity = 50
            print("\nThe car has been started. The car's speed is set to 50 km/h.\n")
            self.update_log("The car has been activated. The car's speed is set to 50 km/h.")
            sleep(1)
        interact_menu()

    def accelerate(self, vehicle):
        if not self.status:
            print("\nThe car is not activated. Turn on the car first to accelerate.\n")
            self.update_log("Attempted to accelerate the car. The car is not activated.")
        else:
            vehicle.velocity += 10
            print(f"\nThe car has been accelerated. The car's speed is set to {vehicle.velocity} km/h.\n")
            self.update_log(f"The car has been accelerated. The car's speed is set to {vehicle.velocity} km/h.")

    def brake(self, vehicle):
        if not self.status:
            print("\nThe car is not activated. Turn on the car first to brake.\n")
            self.update_log("Attempted to slow down the car. The car is not activated.")
        else:
            if vehicle.velocity == 0:
                print("\nThe car is stopped already. It is not possible to reduce the speed.\n")
                self.update_log("Attempted to reduce the speed the car. The car is already stopped.")
            else:
                vehicle.velocity -= 10
                print(f"\nThe car's speed has been reduced. The car's speed is set to {vehicle.velocity} km/h.\n")
                self.update_log(f"The car's speed has been reduced. The car's speed is set to {vehicle.velocity} km/h.")

    def change_direction(self):
        if car.direction == "N":
            car.direction = "S"
            print(f"\nThe car's direction has been changed. New direction is: {car.direction}\n")
            self.update_log(f"The car's direction has been changed. New direction is: {car.direction}.")
            sleep(1)
        else:
            car.direction ="N"
            print(f"\nThe car's direction has been changed. New direction is: {car.direction}\n")
            self.update_log(f"The car's direction has been changed. New direction is: {car.direction}.")
            sleep(1)

    def stop(self, vehicle):
        if not self._status:
            print("\nThe car is not activated. It is not possible to stop the car.\n")
            self.update_log("Attempted to stop the car. The car is not activated.")
        else:
            if vehicle.velocity == 0:
                print("\nThe car has already been stopped. You can't stop it again.\n")
                self.update_log("Attempted to stop the car. The car is already stopped.")
                sleep(1)
            else:
                vehicle.velocity = 0
                print("\nThe car has been stopped.\n")
                self.update_log("The car has been stopped.")
                sleep(1)

    def eval_sign(self, sign):
        # Unpacking the object attributes to variables for easier processing
        code = sign.type
        desc = sign.desc

        if code == 1:
            if car.velocity <= 50:
                print(f"\nCar's speed is {car.velocity}. No action is taken.\n")
                self.update_log(f"{desc} sign detected. Car's speed is below 50. No action taken.")
            else:
                car.velocity = 50
                print("\nCar's speed is set to 50 km/h.\n")
                self.update_log(f"{desc} sign detected. Car's speed is set to 50 km/h.")
        elif code == 2:
            if car.velocity <= 90:
                print(f"\nCar's speed is {car.velocity}. No action is taken.\n")
                self.update_log(f"{desc} sign detected. Car's speed is {car.velocity}. No action taken.")
            else:
                car.velocity = 90
                print("\nCar's speed is set to 90 km/h.\n")
                self.update_log(f"{desc} sign detected. Car's speed is set to 90 km/h.")
        elif code == 3:
            if car.velocity == 0:
                print("\nThe car has already been stopped. No action istaken.\n")
                self.update_log(f"{desc} sign detected. The car is already stopped.")
            else:
                car.velocity = 0
                print("\nThe car has been stopped.\n")
                self.update_log(f"{desc} sign detected. Car has been stopped.")
        elif code == 4:
            if car.velocity == 0:
                print("\nThe car is not moving. No action is taken.\n")
                self.update_log(f"{desc} sign detected. Car is already stopped. No action is taken.")
            else:
                car.velocity = car.velocity * 0.7
                print(f"\nDue to slippery road, the speed of the car is reduced 30%. The current speed of the car is {car.velocity}.\n")
                self.update_log(f"{desc} sign detected. The speed is reduced 30% and set to {car.velocity}.")
        elif code == 5:
            if car.velocity >= 60:
                print(f"\nCar's speed is {car.velocity}. No action is taken.\n")
                self.update_log(f"{desc} sign detected. Car's speed is {car.velocity}. No action is taken.")
            else:
                car.velocity = 60
                print("\nCar's speed is set to 60 km/h.\n")
                self.update_log(f"{desc} sign detected. Car's speed is set to {car.velocity}.")

        # No corner cases are included here, as the input is already checked for validity via try/except statements.

    def eval_veh(self, veh):
        # Compares the car's information against the vehicle detected
        if veh.direction != car.direction:  # If the vehicle and the car travel in opposite directions
            if veh.lane == car.lane:  # If they are approaching to each other on the same lane
                if car.lane == 1:
                    car.lane = 2
                    print("\nThe car changed its lane from 1 to 2.\n")
                    self.update_log(f"A vehicle (Lane: {veh.lane} Direction: {veh.direction}) detected. The car changed its lane from 1 to 2.")
                elif car.lane == 2:
                    if car.velocity < 80:  # If the velocity is less than 80, car changes its lane to the slowest one.
                        car.lane = 1
                        print("\nThe car changed its lane from 2 to 1.\n")
                        self.update_log(f"A vehicle (Lane: {veh.lane} Direction: {veh.direction}) detected. The car changed its lane from 2 to 1.")
                    else:
                        car.lane = 3
                        print("\nThe car changed its lane from 2 to 3.\n")
                        self.update_log(f"A vehicle (Lane: {veh.lane} Direction: {veh.direction}) detected. The car changed its lane from 2 to 3.")
                else:
                    car.lane = 2
                    print("\nThe car changed its lane from 3 to 2.\n")
                    self.update_log(f"A vehicle (Lane: {veh.lane} Direction: {veh.direction}) detected. The car changed its lane from 3 to 2.")
            else:
                print("\nThe cars are on different lanes, no action has been taken.\n")
                self.update_log(f"A vehicle (Lane: {veh.lane} Direction: {veh.direction}) detected. No action is taken (different lane).")
        else:
            if veh.lane == car.lane:
                if veh.velocity <= car.velocity:
                    print("\nThe car is so slow to pose a threat.\n")  # It is on the same lane, but slower than our car.
                    self.update_log(f"A vehicle (Lane: {veh.lane} Direction: {veh.direction}) detected. No action is taken (car too slow).")
                else:
                    if car.lane == 1:
                        print("\nThe car is already on the slowest lane and other car should change the lane. No actions are taken.\n")
                        self.update_log(f"A vehicle (Lane: {veh.lane} Direction: {veh.direction}) detected. No action is taken (car on slowest lane).")
                    elif car.lane == 2:
                        car.lane = 1
                        print("\nThe car changed its lane from 2 to 1.\n")
                        self.update_log(f"A vehicle (Lane: {veh.lane} Direction: {veh.direction}) detected. The car changed its lane from 2 to 1.")
                    else:
                        car.lane = 2
                        print("\nThe car changed its lane from 3 to 2.\n")
                        self.update_log(f"A vehicle (Lane: {veh.lane} Direction: {veh.direction}) detected. The car changed its lane from 3 to 2.")
            else:
                print("\nThe cars are on different lanes, no action has been taken.\n")
                self.update_log(f"A vehicle (Lane: {veh.lane} Direction: {veh.direction}) detected. No action is taken (different lane).")

    def eval_obs(self, obstacle):
        self.add_obstacles(obstacle)  # Adds the obstacle to the obstacle list
        if car.lane == obstacle.lane:
            if car.lane == 1:
                car.lane = 2
                print("\nThe car changed its lane from 1 to 2.\n")
                self.update_log(f"{obstacle.type} on lane {obstacle.lane} is detected. The car changed its lane from 1 to 2.")
            elif car.lane == 2:
                if car.velocity < 80:  # If the velocity is less than 80, car changes its lane to the slowest one.
                    car.lane = 1
                    print("\nThe car changed its lane from 2 to 1.\n")
                    self.update_log(f"{obstacle.type} on lane {obstacle.lane} is detected. The car changed its lane from 2 to 1.")
                else:
                    car.lane = 3
                    print("\nThe car changed its lane from 2 to 3.\n")
                    self.update_log(f"{obstacle.type} on lane {obstacle.lane} is detected. The car changed its lane from 2 to 3.")
            else:
                car.lane = 2
                print("\nThe car changed its lane from 3 to 2.\n")
                self.update_log(f"{obstacle.type} on lane {obstacle.lane} is detected. The car changed its lane from 3 to 2.")
        else:
            print(f"\nThe car is on lane {car.lane} and obstacle is on lane {obstacle.lane}. No action is taken.\n")
            self.update_log(f"{obstacle.type} on lane {obstacle.lane} is detected. No action is taken (different lane).")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def users(self):
        return self._users

    @property
    def obstacles(self):
        return self._obstacles

    def add_obstacles(self, obstacle):
        self._obstacles.append(obstacle)

    def list_obstacles(self):
        print("\n", 30 * "=", "DETECTED OBSTACLES", 30 * "=", "\n")
        print("{:<30} {:<18} {:<30}".format('DETECTED OBSTACLE', 'LANE', 'DATE AND TIME'))
        for obstacle in self._obstacles:
            print("{:<30} {:<18} {:<30}".format(obstacle.type, obstacle.lane, obstacle.timestamp))
        print("\n", 78 * "=", "\n")

    def update_log(self, text):
       # Calculating timestamp
        time_now = datetime.now()
        timestamp = time_now.strftime("%d/%m/%Y %H:%M:%S")
        self._log.append([text, timestamp])  # Adding the message with timestamp

    def read_log(self):
        print("\n", 30 * "=", "CAR LOG (starting from the most recent incident):", 30 * "=", "\n")
        print("{:<84} {:<25}".format('INCIDENT', 'DATE AND TIME'))
        while len(self._log) > 0:
            temp = self._log.pop()
            print("{:<84} {:<25}".format(temp[0], temp[1]))
        print("\n", 39 * "=", "----- THE END OF CAR LOG -----", 40 * "=", "\n")


class User(System_User):
    """A class which stores the system user information."""
    def __init__(self, name, surname, username):
        self._name = name
        self._surname = surname
        self._username = username

    def turn_on(self):
        control_unit.start_car(car)

    # Only a getter for username is added because no other attributes will be called for and be amended in the program.
    @property
    def username(self):
        return self._username


class Lidar(Sensor):
    """The component which detects the obstacles and sends obstacle information to control unit for evaluation."""
    def __init__(self, types=None, obstacle=None):
        self._types = {1: 'Rock', 2: 'Pedestrian', 3: 'Animal', 4: 'Trash', 5: 'Traffic cone'}  # Obstacle type database
        self._obstacle = []

    def detect(self):
        """Detects the traffic sign."""
        type_code = int(input("""\nPlease select an obstacle to place on the road:
1. Rock
2. Pedestrian
3. Animal
4. Trash
5. Traffic cone

Your selection [1-5]: """))

        lane = int(input("""\nPlease select a lane to place the obstacle.
Your selection [1-3]: """))

        # The LiDAR interprets the sign detected (e.g. the code entered by the user) by using obstacle type database.
        for x in self._types.keys():
            if type_code == x:
                type = self._types.get(x)

        # Calculating timestamp
        time_now = datetime.now()
        timestamp = time_now.strftime("%d/%m/%Y %H:%M:%S")

        # Updating the obstacle data according to the outcome of the detection
        obs = Obstacle(type, lane, timestamp)
        self._obstacle = (obs)
        self.send_data(obs)  # To send the data to the control unit for processing.

    def send_data(self, obs):
        """Sends the data to the control unit"""
        control_unit.eval_obs(obs)

    # Only obstacle getter method is written, because the values are set by the detect() method.
    @property
    def obstacle(self):
        return self._obstacle


class Obstacle(Obstacles):
    """A class which stores the information of each individual obstacle."""
    def __init__(self, type, lane, timestamp):
        self._type = type
        self._lane = lane
        self._timestamp = timestamp

    @property
    def type(self):
        return self._type

    @property
    def lane(self):
        return self._lane

    @property
    def timestamp(self):
        return self._timestamp

class V2V_Comms(Comms_Module):
    """
    The component which detects the other vehicles in the environment. It sends vehicle data to the Control Unit
    for evaluation.
    """
    def __init__(self, veh_types=None, vehicles=None):
        self._veh_types = {1: 'Car', 2: 'Van', 3: 'SUV', 4: 'Truck', 5: 'Trailer'}
        self._vehicles = []

    def get_data(self):
        """Intercepts incoming communication from nearby vehicles."""
        while True:
            try:
                type_code = int(input("""\nPlease select a vehicle type to instantiate:
1. Car
2. Van
3. SUV
4. Truck
5. Trailer
    
Your selection [1-5]: """))
                if type_code < 1 or type_code > 5:
                    print("\nInvalid input.\n")
                    sleep(1)
                    continue
            except ValueError:
                print("\nPlease enter an integer.\n")
                sleep(1)
                continue
            else:
                break

        while True:
            try:
                velocity = int(input("""\nPlease enter the velocity of the vehicle.
Enter value [max. 180]: """))
                if velocity > 180:
                    print("\nYou are way too fast! Max. permitted speed for the car is 180.\n")
                    sleep(1)
                    continue
                elif velocity < 0:
                    print("\nSpeed cannot be negative. Please enter a positive integer.\n")
                    sleep(1)
                    continue
            except ValueError:
                print("\nPlease enter an integer.\n")
                sleep(1)
                continue
            else:
                break

        # There are only two valid directions in the program: North and South
        while True:
            try:
                direction = input("""\n Please select the direction the vehicle is moving.
Your selection [N or S]: """)
                direction = direction.upper()  # In order to accept valid lowercase inputs.
                if direction != "N" and direction != "S":
                    print("\nPlease make a valid choice [N or S].\n")
                    sleep(1)
                    continue
            except:
                print("\nInvalid input. Please make a valid choice [N or S]\n")
                continue
            else:
                break

        while True:
            try:
                lane = int(input("""\n Please select a lane the vehicle is on.
Your selection [1-3]: """))
                if lane not in [1, 2, 3]:
                    print("\nPlease make a valid choice [1-3]\n")
                    sleep(1)
                    continue
            except:
                print("\nInvalid input. Please make a valid choice [1-3]\n")
                sleep(1)
                continue
            else:
                break

        # V2V Comms module interprets the vehicle code it receives to identify the type of the vehicle:
        for x in self._veh_types.keys():
            if type_code == x:
                car_type = self._veh_types.get(x)

        # Creating a Vehicle object using the input data
        vehicle = Vehicle(car_type, direction, lane, velocity)

        # Updating the obstacle data according to the outcome of the detection
        self.update_db(vehicle)
        self.send_data(vehicle)

    def update_db(self, veh):
        self._vehicles.append(veh)

    def list_vehicles(self):
        print("\n", 30 * "=", "DETECTED VEHICLES", 31 * "=", "\n")
        print("{:<33} {:<15} {:<15} {:<15}".format('DETECTED VEHICLE', 'DIRECTION', 'LANE', 'VELOCITY'))
        for vehicle in self._vehicles:
            print("{:<33} {:<15} {:<15} {:<15}".format(vehicle.type, vehicle.direction, vehicle.lane, vehicle.velocity))
        print("\n", 78 * "=", "\n")

    def send_data(self, veh):
        control_unit.eval_veh(veh)

class TSRS(Sign_Recognition_System):
    """The component which detects traffic signs and sends traffic sign data to the Control Unit for evaluation."""
    def __init__(self, sign_code=None):
        self._sign_code = sign_code

    def detect_sign(self):
        while True:
            try:
                self._sign_code = int(input("""\nPlease select a traffic sign to put on the road:
         1. Speed Limit (50 km/h)
         2. Speed Limit (90 km/h)
         3. Stop
         4. Slippery Road
         5. Minimum Speed Limit (60 km/h)
         Your selection [1-5]: """))
                if self._sign_code < 1 or self._sign_code > 5:
                    print("Invalid input. Please provide a valid input [1-5]")
                    sleep(1)
            except ValueError:
                print("Please enter an integer.")
                sleep(1)
            else:
                return self.sign_code

    def check_db(self, code):
        return sign_db.check_sign(code)

    def send_data(self, sign_code, sign_desc):
        traffic_sign = Traffic_Sign(sign_code, sign_desc)
        control_unit.eval_sign(traffic_sign)

    @property
    def sign_code(self):
        return self._sign_code

class Traffic_Sign(T_Sign):
    """
    The class that is instantiated for each traffic sign and which stores the information for each traffic sign
    detected. It only has attributes and setter/getter methods.
    """
    def __init__(self, type=None, desc=None):
        self._type = type
        self._desc = desc

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value


class TMA_DB(Sign_DB):
    """A class to simulate the Traffic Management Authority database."""
    def __init__(self, signs=None):
        self._signs = {1: 'Speed Limit (50 km/h)', 2: 'Speed Limit (90 km/H)', 3: 'Stop', 4: 'Slippery Road',
                       5: 'Minimum Speed Limit (60 km/h)'}

    def check_sign(self, code):
        return self._signs.get(code)

# Creating permanent objects
admin = User('John', 'Doe', 'admin')
control_unit = Control_Unit({'admin'})
car = Car('Car', 'N', 1)
v2vcomms = V2V_Comms()
lidar = Lidar()
sign_db = TMA_DB()
sign_recog = TSRS()

# User menu

def user_login():
    """User login menu. Prompts for username only."""
    print(25 * "=", "WELCOME TO SMART CAR INFORMATION AND INTERACTION SYSTEM (SCIIS)", 24 * "=")
    print("""
        Please enter your username to log in to the system.
        """)
    print("")
    print(98 * "=")
    username = input("Username : ")
    control_unit.auth(username)  # Control unit authenticates the user


def main_menu():
    """Main menu on which the user lands upon successful login. It is also possible to change the user using this
    menu."""
    while True:
        print(30 * "=", "SMART CAR INFORMATION AND INTERACTION SYSTEM (SCIIS)", 30 * "=")
        print("""
        1. Get information about the car
        2. Interact with the car
        3. Change user
        4. Exit
        """)
        print(112 * "=")
        try:
            choice = int(input("Please make your choice [1-3] : "))
            if choice == 1:
                inf_menu()
            elif choice == 2:
                interact_menu()
            elif choice == 3:
                user_login()
            elif choice == 4:
                print("Thank you for using SCIIS!")
                sleep(1)
                exit()
            else:
                print("You have entered an invalid choice. Please try again.")
                sleep(1)
        except ValueError:
            print("Invalid input. Please provide a valid input [1-3]")


def inf_menu():
    """The Information Menu is where the user can access information about the car."""
    while True:
        print(30 * "=", "SMART CAR INFORMATION AND INTERACTION SYSTEM (SCIIS)", 30 * "=")
        print("""
        INFORMATION MENU
        
        1. Check the current status of the car
        2. Check the car log
        3. Print out the user list
        4. Print out the list of obstacles detected
        5. Print out the list of vehicles detected
        6. Return to main menu
        7. Exit the system
            """)
        print(112 * "=")
        try:
            choice = int(input("Please make your choice [1-7] : "))
            if choice == 1:
                print("")
                car.print_state()
                print("")
                sleep(1)
            elif choice == 2:
                control_unit.read_log()
                sleep(1)
            elif choice == 3:
                print("\nThe current authorized users of the system:")
                for name in control_unit.users:
                    print(name)
                print("")
                sleep(1)
            elif choice == 4:
                control_unit.list_obstacles()
            elif choice == 5:
                v2vcomms.list_vehicles()
            elif choice == 6:
                main_menu()
            elif choice == 7:
                print("Thank you for using SCIIS!")
                sleep(2)
                exit()
            else:
                print("You have entered an invalid choice. Please try again.")
                sleep(1)
        except ValueError:
            print("Invalid input. Please provide a valid input [1-5]")
            sleep(1)

def interact_menu():
    """Interaction Menu is where user interacts with the car."""
    while True:
        print(30 * "=", "SMART CAR INFORMATION AND INTERACTION SYSTEM (SCIIS)", 30 * "=")
        print("""
        INTERACTION MENU
    
        1. Start the car
        2. Accelerate
        3. Brake
        4. Change direction (U-turn)
        5. Place an obstacle on the road
        6. Put a traffic sign
        7. Instantiate a car
        8. Stop the car
        9. Add a user
        10. Delete a user
        11. Return to main menu
        12. Exit the system
            """)
        print(112 * "=")

        try:
            choice = int(input("Please make your choice [1-12] : "))
            if choice == 1:
                admin.turn_on()
                sleep(1)
            elif choice == 2:
                control_unit.accelerate(car)
                sleep(1)
            elif choice == 3:
                control_unit.brake(car)
                sleep(1)
            elif choice == 4: # U-turn
                control_unit.change_direction()
                sleep(1)
            elif choice == 5:
                lidar.detect()
                sleep(1)
            elif choice == 6:
                code = sign_recog.detect_sign()
                description = sign_recog.check_db(code)
                sign_recog.send_data(code, description)
                sleep(1)
            elif choice == 7:
                v2vcomms.get_data()
                sleep(1)
            elif choice == 8:
                control_unit.stop(car)
                sleep(1)
            elif choice == 9:
                control_unit.add_user()
                sleep(1)
            elif choice == 10:
                control_unit.delete_user()
                sleep(1)
            elif choice == 11:
                main_menu()
                sleep(1)
            elif choice == 12:
                print("Thank you for using SCIIS!")
                sleep(1)
                exit()
            else:
                print("You have entered an invalid choice. Please try again.")
                sleep(1)
        except ValueError:
            print("Invalid input. Please provide a valid input [1-12]")
            sleep(1)

user_login()
