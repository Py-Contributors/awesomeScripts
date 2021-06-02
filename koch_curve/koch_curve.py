# Koch curve

import turtle   # Importing turtle standard graphics library

# function to create koch curve or koch snowflake
def snowflake(length, level):
    if level == 0:
        t.forward(length)
        return
    
    length = length / 3.0
    snowflake(length, level - 1)
    t.left(60)
    snowflake(length, level - 1)
    t.right(120)
    snowflake(length, level - 1)
    t.left(60)
    snowflake(length, level - 1)

# main function
if __name__ == "__main__":
    t = turtle.Pen()
    t.speed(0)          # defining the speed of turtle
    length = 300.0
    t.penup()           # No drawing while moving
    t.backward(length / 2.0)    # Moving the turtle backward by distance opposite to the direction of the turtle
                                # without changing turtle's heading.

    t.pendown()         # drawing while moving

    for i in range(3):
        snowflake(length, 4)
        t.right(120)

turtle.mainloop()