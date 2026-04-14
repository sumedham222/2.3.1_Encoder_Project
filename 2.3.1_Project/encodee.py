import turtle as trtl
from PIL import ImageGrab


#Setup
msg = input("Enter your long message: ")
BLOCK_SIZE = 15
BLOCKS_PER_ROW = 20
START_X = -200
START_Y = 200


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


curr_x = START_X
curr_y = START_Y


#Loop through message 3 characters at a time
for i in range(0, len(msg), 3):
    # Convert 3 chars to RGB
    r = ord(msg[i])
    g = ord(msg[i+1])
    b = ord(msg[i+2])
   
    #Move and draw
    painter.goto(curr_x, curr_y)
    painter.fillcolor(r, g, b)
    painter.begin_fill()
    for side in range(4):
        painter.forward(BLOCK_SIZE)
        painter.right(90)
    painter.end_fill()
   
    #Move to next column
    curr_x += BLOCK_SIZE
   
    #If row is full, go to next line
    blocks_drawn = (i // 3) + 1
    if blocks_drawn % BLOCKS_PER_ROW == 0:
        curr_x = START_X
        curr_y -= BLOCK_SIZE


#Save
print("Encoding complete. Take a screenshot or use ImageGrab.")
trtl.done()
