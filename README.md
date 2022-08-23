# Smart Car Information and Interaction System

## Introduction

## Usage

## Features

The main features of the program are:

### Information Features

1. Check the current status of the car
2. Check the car log
3. Print out the user list
4. Print out the list of obstacles and vehicles 

### Interactive Features

1. Start and stop the car
2. Increase and decrease the speed of the car
3. Make a U-turn
4. Place an obstacle on the road
5. Put a traffic sign
6. Instantiate a car in the environment
7. Add, delete and change user

## Development Methodology

### Design and UML Models

A use case diagram, sequence diagrams, an activity diagram, a state transition diagram, and a class diagram were prepared in the design phase. Please check out the project design document from here: https://github.com/etKing666/eportfolio/blob/main/files/System%20Design%20v1.0.pdf

### Data Structures

As pointed out in the project design document, the main data structures used in the project are:

1. Lists: Lists are used to simulate databases to store detected obstacles or vehicles.
2. Dictionaries: Dictionaries are used to store predefined types of objects in a key:pair format, such as traffic sign or vehicle types.
3. Sets: Sets are mainly used for membership testing (e.g. checking if the username already exists in the user database).
4. Stacks: The car log is designed as a stack. It displays the most recent message first and goes through the older ones.

### External modules

The external modules used in the project are as follows:

1. abc (ABC class and abstractmethod decorator): This class and decorator are used to design the abstract classes and abstract methods.
2. time (sleep() function): The sleep function is used to pause the interface for a moment so that the output is more readable.
3. sys (exit() function): exit function is used to exit the system whenever the user wants. 
4. datetime (datetime): datetime is used to create a timestamp for the car log and detected obstacles database. 

### Interfaces and Classes

In order to provide a blueprint for the classes that would be used in the program, the abstract classes were designed. The abstract classes doesn't include any implementation (their methods raise NotImplementedError) and all methods are decorated with abstractmethod decorator. In order to make sure that the interfaces are followed strictly extra attention was paid to override all methods of abstract classes when designing classes.  

### Objects and the Information Flow

There are two different kinds of objects that are used in the project:

#### Permanent Objects

These objects are created in compile time. For example, car, control unit, LiDAR, Traffic Sign Recognition System and V2V Communication Module are permanent objects and they live as long as the program runs. Because of this, in order to pass information to these objects, direct reference to object methods are used in the method definitions of classes.

#### Temporary Objects

Temporary objects are created in run time. For example, an Obstacle object is instantiated based on user input when the user decides to put an obstacle on the road. Apart from obstacles, vehicles and traffic signs are temporary objects which might be instantiated for arbitrary number of times, depending on user preference and input. 

The most important function of the temporary objects are encapsulating information. For example, instead of passing vehicle's type, speed, lane and direction individually to control unit for evaluation, all data is encapsulated in an object and passed as such.

## Queries

