import turtle as trtl
from PIL import ImageGrab


#Setup
msg = input("Enter your long message: ")
block_size = 15
blocks_per_row = 20
start_x = -200
start_y = 200


#Data prep
while len(msg) % 3 != 0:
    msg += " "


#Setup for drawing
screen = trtl.getscreen()
screen.setup(1.0, 1.0)
screen.colormode(255)
painter = trtl.Turtle()
painter.speed(0)
painter.penup()


curr_x = start_x
curr_y = start_y


#Loop through message 3 characters at a time
for i in range(0, len(msg), 3):
    # Convert 3 characters to RGB
    r = ord(msg[i])
    g = ord(msg[i+1])
    b = ord(msg[i+2])
   
    #Move and draw
    painter.goto(curr_x, curr_y)
    painter.fillcolor(r, g, b)
    painter.begin_fill()
    for side in range(4):
        painter.forward(block_size)
        painter.right(90)
    painter.end_fill()
   
    #Move to next column
    curr_x += block_size
   
    #If row is full, go to next line
    blocks_drawn = (i // 3) + 1
    if blocks_drawn % blocks_per_row == 0:
        curr_x = start_x
        curr_y -= block_size


#Save
print("Encoding complete. Take a screenshot or use ImageGrab.")
trtl.done()
