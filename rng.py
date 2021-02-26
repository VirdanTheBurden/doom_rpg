import random as rand

# creates a global list to allow for various operations
RNG_LIST = []

# creates a "count" variable for persistence through function calls
count = 0

"""

On call, this function generates a random list of values between int 0-255 for 
various RNG calls made during gameplay. Guarantees no two play sessions will ever be
similar, unlike DOOM or DOOM II. If certain values are already in the list, the 
function will only generate the difference of 255 and the length of the list.

"""

def create_table():

    global RNG_LIST

    # check if the table already exists, if so, then tell the user to fuck right off
    if RNG_LIST:
        raise RuntimeError("The table already exists.")
    
    # loop 256 times to insert a new value into RNG_LIST
    for value in range((255 - len(RNG_LIST))):
    
        # constantly loop through current iteration of for loop until the number 
        # generated is unique to the RNG_LIST
        while True:
        
            # creates new int and sets to num for comparison
            num = rand.randint(0, 255)

            # if the num is not in RNG_LIST, add it and break out of the while loop
            # for a new number for RNG_LIST
            if num not in RNG_LIST:
                
                RNG_LIST.append(num)
                break
        
            # otherwise, continue to the next iteration in while loop to try again 
            # for a new number
            else:
            
                continue

"""

This function accesses a value on the table and returns it for an RNG call.

"""

def get_value():

    global RNG_LIST
    
    grabbed = RNG_LIST[count]
    count += 1
    return grabbed