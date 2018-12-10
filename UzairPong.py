from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

white = (255, 255, 255)
blue = (0, 0, 255)

bat_y = 4
ball_position = [3,3]
ball_velocity = [1,1]


# Functions
def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)

def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y >1:
        bat_y -= 1

def move_down(event):
    global bat_y
    if event.action == 'pressed' and bat_y < 6:
        bat_y +=1


# Main program
while True:
    draw_bat()
    sleep(0.5)
    sense.stick.direction_up = move_up
    sense.clear(0, 0, 0)
    sense.stick.direction_down = move_down

