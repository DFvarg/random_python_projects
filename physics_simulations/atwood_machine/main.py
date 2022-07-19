import pygame
import math

class Object:
    def __init__(self, mass):
        self.mass = mass
        self.velocity = 0
        self.acceleration = 0
        self.force = 0
        self.location = [0, 0]
        self.hitbox = 0

def triangle_points(starting_x, starting_y):
    point2 = (starting_x + (HYPOTENUSE*math.cos(alterable_variables['incline_amount'])), starting_y - (HYPOTENUSE*math.sin(alterable_variables['incline_amount'])))
    point3 = (point2[0], starting_y)

    return((starting_x, starting_y), point2, point3)

def write(display, message, pos, color):
    message_to_write = font.render(message, 1, color)
    display.blit(message_to_write, pos)

def draw_atwood_machine(display):
    tri_coordinates = triangle_points(X, Y)

    # Base
    pygame.draw.polygon(display, MAROON, tri_coordinates)

    # Pulley and stem
    hyp_len = HYPOTENUSE + 60
    center_of_pulley = (X + (hyp_len*math.cos(alterable_variables['incline_amount'])), Y - (hyp_len*math.sin(alterable_variables['incline_amount'])))
    pulley_radius = 10
    pygame.draw.circle(display, DARK_PURPLE, center_of_pulley, pulley_radius)

    pygame.draw.line(display, DARK_PURPLE, tri_coordinates[1], center_of_pulley, 3)
    

    if move == False:
        object_one.location = [(tri_coordinates[0][0] + tri_coordinates[1][0])/2 - 7, (tri_coordinates[0][1] + tri_coordinates[1][1])/2 - 7]
        object_two.location = [center_of_pulley[0], center_of_pulley[1] + 100] # Change Length of string 2


    object_one.hitbox = pygame.Rect(object_one.location[0] - 10, object_one.location[1] - 10, 20, 20)
    object_two.hitbox = pygame.Rect(object_two.location[0] - 10, object_two.location[1] - 10, 20, 20)
    pulley_hitbox[0] = pygame.Rect(center_of_pulley[0] - 10, center_of_pulley[1] - 10, 20, 20)

    len_of_string = math.sqrt((center_of_pulley[0] - object_one.location[0])**2+(center_of_pulley[1]-object_one.location[1])**2)


    # Mass 1
    pygame.draw.circle(display, (255, 0, 0), object_one.location, 10)

    # Mass 2
    pygame.draw.circle(display, (255, 0, 0), object_two.location, 10)

    # String
    string_on_pulley = (object_one.location[0] + (len_of_string*math.cos(alterable_variables['incline_amount'])), object_one.location[1] - (len_of_string*math.sin(alterable_variables['incline_amount'])))
    pygame.draw.line(display, (0, 0, 0), object_one.location, string_on_pulley)

    # String 2
    pygame.draw.line(display, (0, 0, 0), center_of_pulley, object_two.location)

    # pygame.draw.rect(display, (0, 0, 0), object_one.hitbox, 1)
    # pygame.draw.rect(display, (0, 0, 0), object_two.hitbox, 1)
    # pygame.draw.rect(display, (0, 0, 0), pulley_hitbox, 1)

def reset():
    object_one.velocity = 0
    object_one.acceleration = 0
    alterable_variables['mass_one'] = 55
    object_two.velocity = 0
    object_two.acceleration = 0
    alterable_variables['mass_two'] = 55


def draw_display(display, move):
    display.fill(LIGHT_BLUE)

    draw_atwood_machine(display)
    
    radians = math.pi/alterable_variables['incline_amount']
    degrees = alterable_variables['incline_amount']*180/math.pi
    write(display, f"inclination : pi/{radians:.2f} radians     or     {degrees:.2f} degrees", (500, 100), (255, 0, 0))
    write(display, f"exact: {alterable_variables['incline_amount']} degrees {degrees}", (100, 100), (255, 0, 0))
    y = 130
    x = 500
    for k, v in alterable_variables.items():
        write(display, f"{k}: {v}", (x, y), (255, 0, 0))
        y += 30
    
    x = 500
    y = 500
    for k, v in calculated_variables.items():
        write(display, f"{k}: {v:.2f}", (x, y), (255, 0, 0))
        y += 30

    if move:
        write(display, "Simulation Started", (100, 600), (0, 0, 0))
        write(display, f"Mag of Velocity: {abs(object_one.velocity):.2f} m/s^2", (50, 300), (0, 0, 0))
        write(display, f"Looks like: {abs(object_one.velocity/20):.2f} m/s^2", (50, 320), (0, 0, 0))
    else:
        write(display, "Mag of Velocity: 0.00 m/s^2", (50, 300), (0, 0, 0))
        write(display, "Press space to begin simulation", (100, 600), (0, 0, 0))

    write(display, "Press 'r' to reset the simulation", (100, 650), (0, 0, 0))

    write(display, f"{alterable_variables['mass_one']} kg", (object_one.hitbox.x - 30, object_one.hitbox.y - 20), (0, 0, 0))
    write(display, f"{alterable_variables['mass_two']} kg", (object_two.hitbox.x + 30, object_two.hitbox.y - 20), (0, 0, 0))
    write(display, "'a' and 'd' change the mass of object one. left and right arrow keys change the mass of object two", (100, 700), (0, 0, 0))
    write(display, "Up and down arrow keys increase and decrease incline", (100, 730), (0, 0, 0))
    pygame.display.update()

def calc_variables():
    calculated_variables['mass1_normal'] = alterable_variables['mass_one'] * GRAVITY * math.cos(alterable_variables['incline_amount'])
    calculated_variables['mass1_sfriction'] = alterable_variables['coefficient_static_friction'] * calculated_variables['mass1_normal']
    calculated_variables['mass1_kfriction'] = alterable_variables['coefficient_kinetic_friction'] * calculated_variables['mass1_normal']
    calculated_variables['mass1_pforce'] = alterable_variables['mass_one'] * GRAVITY * math.sin(alterable_variables['incline_amount'])


    calculated_variables['mass2_weight'] = alterable_variables['mass_two'] * GRAVITY

    calculated_variables['MAGNITUDE_SIGMA_FORCE'] = calculated_variables['mass2_weight'] - calculated_variables['mass1_pforce']
    calculated_variables['MAGNITUDE_ACCELERATION'] = calculated_variables['MAGNITUDE_SIGMA_FORCE']/(alterable_variables['mass_one'] + alterable_variables['mass_two'])
    
    object_one.acceleration = calculated_variables['MAGNITUDE_ACCELERATION']
    object_one.force = calculated_variables['MAGNITUDE_SIGMA_FORCE']
    object_two.acceleration = calculated_variables['MAGNITUDE_ACCELERATION']
    object_two.force = calculated_variables['MAGNITUDE_SIGMA_FORCE']

def calc_displacement(vel):
    magnitude = vel[0]
    direction = vel[1]

    x_comp = magnitude*math.cos(direction)
    y_comp = magnitude*math.sin(direction)
    return(x_comp, y_comp)

def calc_movement():
    if object_one.hitbox.colliderect(pulley_hitbox[0]) or object_two.hitbox.colliderect(pulley_hitbox[0]):
        pass
    else:
        object_two.velocity += object_two.acceleration
        object_two.location[1] += object_two.velocity/20

        object_one.velocity += object_one.acceleration
        displacement = calc_displacement([object_one.velocity, alterable_variables['incline_amount']])
        object_one.location[0] += displacement[0]/20
        object_one.location[1] -= displacement[1]/20

MAROON = '#72110a'
LIGHT_BLUE = '#87CEFA'
DARK_PURPLE = '#2d0168'
HEIGHT = 800
WIDTH = 800
GRAVITY = 9.8
HYPOTENUSE = 300
X = 150
Y = 500
move = False
pulley_hitbox = [0]
alterable_variables = {'incline_amount': math.pi/7.9,
                        'coefficient_static_friction': .5,
                        'coefficient_kinetic_friction': .3,
                        'mass_one': 55,
                        'mass_two': 55}

calculated_variables = {}

pygame.init()
font = pygame.font.SysFont("Arial", 14)
display = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock()

object_one = Object(alterable_variables['mass_one'])
object_two = Object(alterable_variables['mass_two'])


run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    draw_display(display, move)

    calc_variables()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and alterable_variables['incline_amount'] < math.pi/2 -.01 and move == False:
        alterable_variables['incline_amount'] += .01
    elif keys[pygame.K_DOWN] and alterable_variables['incline_amount'] > .01 and move == False:
        alterable_variables['incline_amount'] -= .01


    if keys[pygame.K_a] and alterable_variables['mass_one'] > 1 and move == False:
        alterable_variables['mass_one'] -= 1
    elif keys[pygame.K_d] and move == False:
        alterable_variables['mass_one'] += 1
    elif keys[pygame.K_LEFT] and alterable_variables['mass_two'] > 1 and move == False:
        alterable_variables['mass_two'] -= 1
    elif keys[pygame.K_RIGHT] and move == False:
        alterable_variables['mass_two'] += 1
        
    if keys[pygame.K_SPACE]:
        move = True

    if keys[pygame.K_r]:
        move = False
        reset()
    
    if move:
        calc_movement()

    
pygame.quit()
