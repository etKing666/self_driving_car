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

INCIDENT                                                                             
Traffic cone on lane 2 is detected. The car changed its lane from 2 to 3.               
The car has been accelerated. The car's speed is set to 100 km/h.                         
The car has been accelerated. The car's speed is set to 90 km/h.                           
The car has been accelerated. The car's speed is set to 80 km/h.                          
The car has been accelerated. The car's speed is set to 70 km/h.                           
The car has been accelerated. The car's speed is set to 60 km/h.                         
Trash on lane 1 is detected. The car changed its lane from 1 to 2.                        
Animal on lane 2 is detected. The car changed its lane from 2 to 1.                       
Pedestrian on lane 3 is detected. No action is taken (different lane).                    
Rock on lane 1 is detected. The car changed its lane from 1 to 2.                          
The car has been activated. The car's speed is set to 50 km/h.                          
The user 'admin' has been authorized to use the system.

## Test Case #2 (Sign-oriented)

### Test steps:

1. Start the car (1)
2. Put a traffic sign (6)
3. Stop (3)
4. Accelerate (2)
5. Accelerate (2)
6. Accelerate (2)
7. Put a traffic sign (6)
8. Minimum Speed Limit (60 km/h) (5)
9. Accelerate (2)
10. Accelerate (2)
11. Accelerate (2)
12. Accelerate (2)
13. Put a traffic sign (6)
14. Speed Limit (90 km/h) (2)
15. Put a traffic sign (6)
16. Slippery Road (4)

### Desired end state:

The car log should read as follows:

INCIDENT                            
Slippery Road sign detected. The speed is reduced 30% and set to 62.99999999999999.     
Speed Limit (90 km/H) sign detected. Car's speed is set to 90 km/h.                       
The car has been accelerated. The car's speed is set to 100 km/h.                      
The car has been accelerated. The car's speed is set to 90 km/h.                          
The car has been accelerated. The car's speed is set to 80 km/h.                         
The car has been accelerated. The car's speed is set to 70 km/h.                         
Minimum Speed Limit (60 km/h) sign detected. Car's speed is set to 60.               
The car has been accelerated. The car's speed is set to 30 km/h.                         
The car has been accelerated. The car's speed is set to 20 km/h.                          
The car has been accelerated. The car's speed is set to 10 km/h.                    
Stop sign detected. Car has been stopped.                                              
The car has been activated. The car's speed is set to 50 km/h.                            
The user 'admin' has been authorized to use the system.   

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