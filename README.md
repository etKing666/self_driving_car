# Smart Car Information and Interaction System

## Introduction

## Usage

## Features

### Information Features

### Interactive Features

## Development Methodology

### Design and UML Models

A use case diagram, sequence diagrams, an activity diagram, a state transition diagram, and a class diagram were prepared in the design phase. Please check out the project design document from here: https://github.com/etKing666/eportfolio/blob/main/files/System%20Design%20v1.0.pdf

### Data Structures

As pointed out in the project design document, the main data structures used in the project are:

1. Lists: Lists are used to simulate databases to store detected obstacles or vehicles.
2. Dictionaries: Dictionaries are used to store predefined types of objects in a key:pair format, such as traffic sign or vehicle types.
3. Sets: Sets are mainly used for membership testing (e.g. checking if the username already exists in the user database).
4. Stacks: The car log is designed as a stack. It displays the most recent message first and goes through the older ones.

### Interfaces and Classes

### Objects and the Information Flow

There are two different kinds of objects that are used in the project:

#### Permanent Objects

These objects are created in compile time. For example, car, control unit, LiDAR, Traffic Sign Recognition System and V2V Communication Module are permanent objects and they live as long as the program runs. Because of this, in order to pass information to these objects, direct reference to object methods are used in the method definitions of classes.

#### Temporary Objects

Temporary objects are created in run time. For example, an Obstacle object is instantiated based on user input when the user decides to put an obstacle on the road. Apart from obstacles, vehicles and traffic signs are temporary objects which might be instantiated for arbitrary number of times, depending on user preference and input. 

The most important function of the temporary objects are encapsulating information. For example, instead of passing vehicle's type, speed, lane and direction individually to control unit for evaluation, all data is encapsulated in an object and passed as such.

## Queries

