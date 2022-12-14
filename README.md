# Smart Car Information and Interaction System (SCIIS)

## Introduction

SCIIS is a program aimed to simulate the behaviour of a driverless car which interacts with its environment.  

## Usage

The program relies on a textual interface. The user lands on the login screen when the program is run. For simplicty, only username is required to log in to the system (no password is needed). After successful login, user can navigate between the various menus.

The default username is 'admin'. Additional usernames can be created later in the program.

### Assumptions

The program is developed on following assumptions:

1. For the sake of simplicity, only two directions of travel are accepted: North (N) and South (S).
2. The car is projected to travel in a three-lane road where the rightmost lane is the slowest one.
3. The road is open for two-way traffic.

## Features

### Informational Features

1. Check the current status of the car
2. Check the car log
3. Print out the list of users, obstacles and vehicles

### Interactive Features

1. Start and stop the car
2. Increase and decrease the car speed 
3. Change direction and lane of the car
4. Place an obstacle
5. Put a traffic sign
6. Instantiate a car
7. Add, delete or change user

## Development Methodology

### Design and UML Models

Project design document can be accessed from [here](https://github.com/etKing666/eportfolio/blob/main/files/System%20Design%20v1.0.pdf).

### Data Structures

As pointed out in the design document, the main data structures used in the project are lists, dictionaries, queues, sets and stacks.

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

These objects are created in compile time. For example, car, control unit, LiDAR, Traffic Sign Recognition System and V2V Communication Module are permanent objects, and they live as long as the program runs. Because of this, in order to pass information to these objects, direct reference to object methods are used in the method definitions of classes.

#### Temporary Objects

Temporary objects are created in run time. For example, an Obstacle object is instantiated based on user input when the user decides to put an obstacle on the road. Apart from obstacles, vehicles and traffic signs are temporary objects which might be instantiated for arbitrary number of times, depending on user preference and input. 

The most important function of the temporary objects are encapsulating information. For example, instead of passing vehicle's type, speed, lane and direction individually to control unit for evaluation, all data is encapsulated in an object and passed as such.

## Testing

During the development process, unit tests was used extensively in order to make sure that each component works properly. Once all components are developed, integration and functional tests were employed to test full functionality. Pylint was also used to identify defects in the code.

The test cases can be found [here](test_cases.md). 