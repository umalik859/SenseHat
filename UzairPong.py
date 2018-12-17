from sense_hat import SenseHat
from time import sleep
from random import choice

sense = SenseHat()

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)


bat_y = 4
ball_position = [3,3]
ball_velocity = [1,1]
total = 0

sense.show_message("What Will Be Your Highscore?", text_colour=green, scroll_speed=0.06)

for i in range(5, -1, -1):
        sense.show_letter(str(i), red)
        sleep(1)
        

# Functions
def draw_bat():
    sense.set_pixel(0, bat_y, blue)
    sense.set_pixel(0, bat_y + 1, blue)
    sense.set_pixel(0, bat_y - 1, blue)

def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y >1:
        bat_y -= 1

def move_down(event):
    global bat_y
    if event.action == 'pressed' and bat_y < 6:
        bat_y +=1
def draw_ball():
    global total
    sense.set_pixel(ball_position[0], ball_position[1], white)
    ball_position[0] += ball_velocity[0]
    if ball_position[0] == 7 or ball_position[0] == 0:
        ball_velocity[0] = -ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[1] == 7 or ball_position[1] == 0:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 1 and (bat_y - 1) <= ball_position[1] <= (bat_y + 1):
        ball_velocity[0] = -ball_velocity[0]
        total = total + 1
    if ball_position[0] == 0:
        sense.show_message("Game Over", text_colour = green)
        sense.show_message(str(total), text_colour = blue, back_colour = green)
def ball_reset():
    if ball_position[0] == 0 and not (bat_y - 1) <= ball_position[1] <= (bat_y + 1):
        ball_position[0] == 3
        ball_position[1] == 3
    

# Main program
while True:
    draw_bat()
    sleep(0.3)
    sense.stick.direction_up = move_up
    sense.clear(0, 0, 0)
    sense.stick.direction_down = move_down
    draw_ball()
    print (total)
    ball_reset()
    



