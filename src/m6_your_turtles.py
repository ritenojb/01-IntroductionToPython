"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Jacob Ritenour.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################
import rosegraphics as rg
###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
window = rg.TurtleWindow()
#Draws circles moving right
jim = rg.SimpleTurtle()
jim.pen = rg.Pen('green', 5)
jim.speed = 15
size = 200
for k in range(20):
    jim.draw_circle(size)
    jim.pen_up()
    jim.forward(10)
    jim.pen_down()

pam = rg.SimpleTurtle()
pam.pen = rg.Pen('orange', 15)
pam.speed = 10
size = 150
for k in range(20):
    pam.draw_regular_polygon(5, 100)
    pam.pen_up()
    pam.right(90)
    pam.forward(10)
    pam.pen_down()
    size = size - 5