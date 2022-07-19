import pygame
import ball_2d

pygame.init()
display = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
GRAVITY = 2
ball = ball_2d.ball(100, 370, 10, 10, GRAVITY)
clicked = False
objects = []

def draw_display(display):
    display.fill((24, 35, 125))
    pygame.draw.line(display, (255, 255, 255), (0, 400), (800, 400), 1) # floor
    pygame.draw.line(display, (255, 255, 255), (750, 0), (750, 400), 1) # right wall
    pygame.draw.line(display, (255, 255, 255), (50, 0), (50, 400), 1) # left wall
    pygame.draw.line(display, (255, 255, 255), (0, 10), (800, 10), 1) # ceiling
    ball.draw(display)

    for i in objects:
        pygame.draw.rect(display, (255, 255, 255), i)
        # pygame.draw.line(display, (0, 0, 255), (i.left, 0), (i.left, 400))

    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.line(display, (255, 255, 255), (ball.x, ball.y), (mouse_pos[0], mouse_pos[1]))



    # pygame.draw.line(display, (0, 0, 255), (ball.col_rect.right, 0), (ball.col_rect.right, 400))
def collision_type(rect):
    if ball.x + ball.radius > rect.x and ball.x + ball.radius < rect.x + rect.width/1.1 and ball.y > rect.y and ball.y - ball.radius < rect.y + rect.height/1.1:
        ball.x = rect.x - ball.radius
        ball.wall_collision()
    elif ball.x - ball.radius < rect.x + rect.width and ball.x + ball.radius > rect.x + rect.width/1.1 and ball.y > rect.y and ball.y - ball.radius < rect.y + rect.height/1.1:
        ball.x = rect.x + rect.width + ball.radius
        ball.wall_collision()        
    elif ball.x + ball.radius > rect.x and ball.x - ball.radius < rect.x + rect.width and ball.y + ball.radius > rect.y and ball.y - ball.radius < rect.y + rect.height/1.1:
        ball.normal_force[1] = ball.mass*GRAVITY
        ball.surface_kinetic_mew = .5
        ball.y = rect.y - ball.radius
        if ball.velocity[1] > 1 or ball.velocity[1] < -1:
            ball.ground_collision()
    elif ball.x + ball.radius > rect.x and ball.x - ball.radius < rect.x + rect.width and ball.y - ball.radius < rect.y + rect.height and ball.y + ball.radius > rect.y:
        ball.y = rect.y + rect.height + ball.radius
        ball.ground_collision()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    draw_display(display)
    ball.move(.1)


    if ball.y >= 400 - ball.radius:
        ball.normal_force[1] = ball.mass*GRAVITY
        ball.surface_static_mew = .6
        ball.surface_kinetic_mew = .5
        ball.y = 400-ball.radius
        if ball.velocity[1] > 1 or ball.velocity[1] < -1:
            ball.ground_collision()
    else:
        ball.normal_force[1] = 0

    if ball.y - ball.radius <= 10:
        ball.y = 10+ball.radius
        ball.roof_collision()
    
    if ball.x + ball.radius >= 750:
        ball.x = 750 - ball.radius
        ball.wall_collision()

    elif ball.x - ball.radius <= 50:
        ball.x = 50 + ball.radius
        ball.wall_collision()

    # Check for collisions with new objects
    for i in objects:
        collision_type(i)

    if pygame.mouse.get_pressed()[0] and clicked == False:
        mouse_pos = pygame.mouse.get_pos()
        ball.forces[0] = (mouse_pos[0] - ball.x)*2.5
        ball.forces[1] = (ball.y - mouse_pos[1])*2.5
        clicked = True
    else:
        ball.forces[0] = 0
        ball.forces[1] = 0

    if pygame.mouse.get_pressed()[0] != True:
        clicked = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        mouse_pos = pygame.mouse.get_pos()
        objects.append(pygame.Rect(mouse_pos[0], mouse_pos[1], 30, 30))
    if keys[pygame.K_2]:
        mouse_pos = pygame.mouse.get_pos()
        objects.append(pygame.Rect(mouse_pos[0], mouse_pos[1], 60, 40))
    if keys[pygame.K_3]:
        mouse_pos = pygame.mouse.get_pos()
        objects.append(pygame.Rect(mouse_pos[0], mouse_pos[1], 100, 150))
    if keys[pygame.K_4]:
        mouse_pos = pygame.mouse.get_pos()
        objects.append(pygame.Rect(mouse_pos[0], mouse_pos[1], 300, 30))

    pygame.display.update()

    
pygame.quit()
