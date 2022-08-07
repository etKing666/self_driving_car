from abc import ABC, abstractmethod


#Defining interfaces:

class Control_Unit(ABC)
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

class SmartVehicle(ABC):
    def __init__(self, type, velocity, direction, lane):
        self.type = type
        self.velocity = velocity
        self.direction = direction
        self.lane = lane

class Sensor(ABC):
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



# Creating classes:

class Vehicle():
    def __init__(self, status=False):
        self.status = status

    @property
    def state(self):
        return self.status

    @state.setter
    def state(self, value):
        self.status = value





