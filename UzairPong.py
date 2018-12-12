from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)


bat_y = 4
ball_position = [3,3]
ball_velocity = [1,1]


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
    total = 0
    count = 0
    sense.set_pixel(ball_position[0], ball_position[1], white)
    ball_position[0] += ball_velocity[0]
    if ball_position[0] == 7 or ball_position[0] == 0:
        ball_velocity[0] = -ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[1] == 7 or ball_position[1] == 0:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 1 and (bat_y - 1) <= ball_position[1] <= (bat_y + 1):
        ball_velocity[0] = -ball_velocity[0]
        total = count += 1
    if ball_position[0] == 0:
        sense.show_message("You Lose",)
        sense.show_message(str(total))

    

# Main program
while True:
    draw_bat()
    sleep(0.5)
    sense.stick.direction_up = move_up
    sense.clear(0, 0, 0)
    sense.stick.direction_down = move_down
    draw_ball()



