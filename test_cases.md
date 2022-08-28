# Test Cases

## Instructions

1. Each test starts with logging in as admin (username: 'admin') and selecting 'Interact with the car' (2)
2. The steps described in the test steps should be implemented in the given order. The numbers in parentheses indicate the option number in the interaction menu. 
3. Once all steps are executed, car log should be checked and compared against the desired end state. Car log can be accessed at the Main Menu > Get information about the car (1) > Check car log (2) 
4. Any discrepancies should be reported to the developer at eg22518@essex.ac.uk

## Test Case #1 (Obstacle-oriented) 

### Description

In this test case, car's behaviour against the different types of obstacles detected is tested (validation testing). 

### Test steps:

1. Username : admin
2. Interact with the car (2)
3. Start the car (1)
4. Place an obstacle on the road (5).
5. Rock (1)
6. Lane 1 (1)
7. Place an obstacle on the road (5).
8. Pedestrian (2)
9. Lane 3 (3)
10. Place an obstacle on the road (5).
11. Animal (3)
12. Lane 2 (2)
13. Place an obstacle on the road (5).
14. Trash (4)
15. Lane 1 (1)
16. Accelerate (2)
17. Accelerate (2)
18. Accelerate (2)
19. Accelerate (2)
20. Accelerate (2)
21. Place an obstacle on the road (5).
22. Traffic cone (5)
23. Lane 2 (2)

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

### Description:

The focus of the test case is to test the car's behaviour against a set of traffic signs detected (validation testing).

### Test steps:

1. Username : admin
2. Interact with the car (2)
3. Start the car (1)
4. Put a traffic sign (6)
5. Stop (3)
6. Accelerate (2)
7. Accelerate (2)
8. Accelerate (2)
9. Put a traffic sign (6)
10. Minimum Speed Limit (60 km/h) (5)
11. Accelerate (2)
12. Accelerate (2)
13. Accelerate (2)
14. Accelerate (2)
15. Put a traffic sign (6)
16. Speed Limit (90 km/h) (2)
17. Put a traffic sign (6)
18. Slippery Road (4)

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

## Description:

The aim of the test case #3 is to test the behavior of the car's reaction to various vehicles detected on the road (validation testing).

### Test steps:

1. Username : admin
2. Interact with the car (2)
3. Start the car (1)
4. Instantiate a car (7)
5. Car (1)
6. 120 
7. N
8. Lane 1 (1)
9. Accelerate (2)
10. Accelerate (2)
11. Accelerate (2)
12. Change lane (8)
13. Lane 2 (2)
14. Instantiate a car (7)
15. SUV (3)
16. 120
17. N
18. Lane 2 (2)
19. Instantiate a car (7)
20. Van (2)
21. 70
22. S
23. 1

### Desired end state:

The car log should read as follows:

INCIDENT                            
A vehicle (Lane: 1 Direction: S) detected. The car changed its lane from 1 to 2.           
A vehicle (Lane: 2 Direction: N) detected. The car changed its lane from 2 to 1.           
The car's lane has been changed. New lane is: 2.                                          
The car has been accelerated. The car's speed is set to 80 km/h.              
The car has been accelerated. The car's speed is set to 70 km/h.                     
The car has been accelerated. The car's speed is set to 60 km/h.                       
A vehicle (Lane: 1 Direction: N) detected. No action is taken (car on slowest lane).      
The car has been activated. The car's speed is set to 50 km/h.                         
The user 'admin' has been authorized to use the system.  

## Test Case #4 (Car-oriented)

### Description

The aim of this test case is to test the car's own behaviour based on user input. In this test, a couple of user
error are also incorporated to make sure the corner cases are covered (defect testing). 

### Test steps:

1. Username : admin
2. Interact with the car (2)
3. Change direction (U-turn) (4)
4. Start the car (1)
5. Brake (3)
6. Change lane (8)
7. Lane 2 (2)
8. Accelerate (2)
9. Accelerate (2)
10. Change direction (U-turn) (4)
11. Stop the car (9)
12. Brake (3)

### Desired end state:

The car log should read as follows:

INCIDENT
Attempted to reduce the speed the car. The car is already stopped.                      
The car has been stopped.                                                              
The car's direction has been changed. New direction is: S.                            
The car has been accelerated. The car's speed is set to 60 km/h.                          
The car has been accelerated. The car's speed is set to 50 km/h.                      
The car's lane has been changed. New lane is: 2.                                         
The car's speed has been reduced. The car's speed is set to 40 km/h.                      
The car has been activated. The car's speed is set to 50 km/h.                             
Attempted to change the direction without activating the car. No action is taken.          
The user 'admin' has been authorized to use the system.     

## Test Case #5 (User-oriented)

### Description

Test case #5 covers the testing of basic user functionality (validation testing). 

### Test steps:

1. Username : admin
2. Interact with the car (2)
3. Add a user (10)
4. Username: test_user
5. Return to main menu (12)
6. Change user(3)
7. Username: test_user
8. Interact with the car (2)
9. Delete a user (11)
10. Username: admin

### Desired end state:

The car log should read as follows:

INCIDENT                           
The user admin has been deleted.                                                           
The user 'test_user' has been authorized to use the system.                              
The user test_user has been added.                                                      
The user 'admin' has been authorized to use the system.  

## Test Case #6 (Complex)

### Description:

This test case covers a mix of events/functions of various types (validation testing). 

### Test steps:

1. Username : admin
2. Interact with the car (2)
3. Start the car (1)
4. Brake (3)
5. Brake (3)
6. Put a traffic sign (6)
7. Minimum Speed Limit (60 km/h) (5)
8. Instantiate a car (7)
9. Car (1)
10. 120
11. S
12. Lane 1 (1)
13. Accelerate (2)
14. Accelerate (2)
15. Accelerate (2)
16. Accelerate (2)
17. Place an obstacle on the road (5)
18. Rock (1)
19. Lane 2 (2)
20. Change lane (8)
21. Lane 2 (2)
22. Put a traffic sign (6)
23. Speed Limit (50 km/h) (1)
24. Change direction (U-turn) (4)
25. Stop the car (9)

### Desired end state:

The car log should read as follows:

INCIDENT                           
The car has been stopped.                                                                 
The car's direction has been changed. New direction is: S.                                 
Speed Limit (50 km/h) sign detected. Car's speed is set to 50 km/h.                        
The car's lane has been changed. New lane is: 2.                                          
Rock on lane 2 is detected. The car changed its lane from 2 to 3.                         
The car has been accelerated. The car's speed is set to 100 km/h.                         
The car has been accelerated. The car's speed is set to 90 km/h.                           
The car has been accelerated. The car's speed is set to 80 km/h.                          
The car has been accelerated. The car's speed is set to 70 km/h.                           
A vehicle (Lane: 1 Direction: S) detected. The car changed its lane from 1 to 2.         
Minimum Speed Limit (60 km/h) sign detected. Car's speed is set to 60.                  
The car's speed has been reduced. The car's speed is set to 30 km/h.                      
The car's speed has been reduced. The car's speed is set to 40 km/h.                 
The car has been activated. The car's speed is set to 50 km/h.                           
The user 'admin' has been authorized to use the system.     
