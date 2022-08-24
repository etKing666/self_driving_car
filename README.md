# Smart Car Information and Interaction System

## Introduction

Smart Car Information and Interaction System (SCIIS) is a program aimed to simulate the behaviour of a driverless car which intreracts with its environment (e.g. other vehicles, traffic signs and obstacles on the road).  

## Usage

The program relies on a textual interface. The user can get information or interact with the car using menus. The user lands on the login screen when the program is run. In order to keep the process simple, only username is required to login to the system (no password is needed). After successful login, user can navigate between the main menu, interaction menu and information menu.

### Assumptions

The program is developed on following assumptions:

1. For the sake of simplicty, only two directions for travel are accepted: North (N) and South (S).
2. The car is projected to travel in a three-lane road where the rightmost lane is the slowest one.
3. The lanes are open for opposite-side traffic (e.g. a car can come from the opposite direction).

## Features

### Informational Features

1. Check the current status of the car
2. Check the car log
3. Print out the user list
4. Print out the list of obstacles and vehicles 

### Interactive Features

1. Start and stop the car
2. Increase and decrease the speed of the car
3. Change directions
4. Place an obstacle
5. Put a traffic sign
6. Instantiate a car
7. Add, delete and change user

## Development Methodology

### Design and UML Models

Please check out the project design document from here: https://github.com/etKing666/eportfolio/blob/main/files/System%20Design%20v1.0.pdf

### Data Structures

As pointed out in the project design document, the main data structures used in the project are lists, dictionaries, sets and stacks.

### External Modules

The external modules used in the project are as follows:

1. abc (ABC class and abstractmethod decorator): This class and the decorator are used to design the abstract classes and abstract methods.
2. time (sleep() function): The sleep function is used to pause the interface for a moment so that the output is more readable.
3. sys (exit() function): exit() function is used to exit the system whenever the user wants. 
4. datetime (datetime): datetime() is used to create a timestamp for the car log and detected obstacles database. 

### Interfaces and Classes

In order to provide a blueprint for the classes that would be used in the program, the abstract classes were designed. The abstract classes doesn't include any implementation (their methods raise NotImplementedError) and all methods are decorated with abstractmethod decorator. In order to make sure that the interfaces are followed strictly, extra attention was paid to override all methods of abstract classes when designing classes. Moreover, getter and setter methods were used to access and manipulate the attributes of the classes from outside of the object.

### Objects and the Information Flow

There are two different kinds of objects that are used in the project:

#### Permanent Objects

These objects are created in compile time. For example, car, control unit, LiDAR, Traffic Sign Recognition System and V2V Communication Module are permanent objects and they live as long as the program runs. Because of this, in order to pass information to these objects, direct reference to object methods are used in the method definitions of classes.

#### Temporary Objects

Temporary objects are created in run time. For example, an Obstacle object is instantiated based on user input when the user decides to put an obstacle on the road. Apart from obstacles, vehicles and traffic signs are temporary objects which might be instantiated for arbitrary number of times, depending on user preference and input. 

The most important function of the temporary objects are encapsulating information. For example, instead of passing vehicle's type, speed, lane and direction individually to control unit for evaluation, all data is encapsulated in an object and passed as such.

## Testing

