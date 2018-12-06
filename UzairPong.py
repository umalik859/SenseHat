from sense_hat import SenseHat
sense = SenseHat()

white = (255, 255, 255)

bat_y = 4

# Functions
def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)

def move_up(event):
    global bat_y
    if event.action == 'pressed':
        bat_y -= 1


# Main program
draw_bat()

sense.stick.direction_up = move_up
sense.clear
