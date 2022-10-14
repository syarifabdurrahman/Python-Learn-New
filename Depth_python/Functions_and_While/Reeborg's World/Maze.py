def turn_right():
    turn_left()
    turn_left()
    turn_left()

def near_wall():    
    while front_is_clear():
        move()
        
        if not right_is_clear():
            turn_left()
        
    if wall_in_front() and not wall_on_right():
        turn_right()
        
    elif wall_in_front() and wall_on_right():
        turn_left()        
        
    elif not wall_in_front() and wall_on_right():
        turn_left()
        move()
        turn_left()
        move()
        turn_left()


    
while not at_goal():
    near_wall()

       
           
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
