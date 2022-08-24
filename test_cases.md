# Test Cases

## Prerequisites

1. Upon running the program, the tester should log in using 'admin' username.
2. The steps described in the test steps should be implemented in the given order. The numbers in parentheses indicate the option number in the interaction menu. 
3. Once all steps are executed, car log should be checked and compared against the desired end state. Car log can be accessed at the Main Menu > Get information about the car (1) > Check car log (2) 
4. Any discrepancies should be reported to eg22518@essex.ac.uk

## Test Case #1 (Obstacle-oriented)

### Test steps:

1. Start the car (1)
2. Place an obstacle on the road (5).
3. Rock (1)
4. Lane 1 (1)
5. Place an obstacle on the road (5).
6. Pedestrian (2)
7. Lane 3 (3)
8. Place an obstacle on the road (5).
9. Animal (3)
10. Lane 2 (2)
11. Place an obstacle on the road (5).
12. Trash (4)
13. Lane 1 (1)
14. Accelerate (2)
15. Accelerate (2)
16. Accelerate (2)
17. Accelerate (2)
18. Accelerate (2)
19. Place an obstacle on the road (5).
20. Traffic cone (5)
21. Lane 2 (2)

### Desired end state:

The car log should read as follows:

INCIDENT                                                                             DATE AND TIME
Traffic cone on lane 2 is detected. The car changed its lane from 2 to 3.            [TIMESTAMP]      
The car has been accelerated. The car's speed is set to 100 km/h.                    [TIMESTAMP]      
The car has been accelerated. The car's speed is set to 90 km/h.                     [TIMESTAMP]      
The car has been accelerated. The car's speed is set to 80 km/h.                     [TIMESTAMP]      
The car has been accelerated. The car's speed is set to 70 km/h.                     [TIMESTAMP]      
The car has been accelerated. The car's speed is set to 60 km/h.                     [TIMESTAMP]      
Trash on lane 1 is detected. The car changed its lane from 1 to 2.                   [TIMESTAMP]      
Animal on lane 2 is detected. The car changed its lane from 2 to 1.                  [TIMESTAMP]      
Pedestrian on lane 3 is detected. No action is taken (different lane).               [TIMESTAMP]      
Rock on lane 1 is detected. The car changed its lane from 1 to 2.                    [TIMESTAMP]      
The car has been activated. The car's speed is set to 50 km/h.                       [TIMESTAMP]      
The user 'admin' has been authorized to use the system.                              [TIMESTAMP]  
                                    

## Test Case #2 (Sign-oriented)

### Test steps:

### Desired end state:

The car log should read as follows:

INCIDENT                            TIMESTAMP
                                    [TIMESTAMP]

## Test Case #3 (Vehicle-oriented)

### Test steps:

### Desired end state:

The car log should read as follows:

INCIDENT                            TIMESTAMP
                                    [TIMESTAMP]

## Test Case #4 (Car-oriented)

### Test steps:

### Desired end state:

The car log should read as follows:

INCIDENT                            TIMESTAMP
                                    [TIMESTAMP]
## Test Case #5 (User-oriented)

### Test steps:

### Desired end state:

The car log should read as follows:

INCIDENT                            TIMESTAMP
                                    [TIMESTAMP]


## Test Case #6 (Complex)

### Test steps:

### Desired end state:

The car log should read as follows:

INCIDENT                            TIMESTAMP
                                    [TIMESTAMP]