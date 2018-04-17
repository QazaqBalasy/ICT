import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
done = False
is_blue = True
points = [400,100]
width = 100
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: points[1] -= 3
    if pressed[pygame.K_DOWN]: points[1] += 3
    if pressed[pygame.K_LEFT]: points[0] -= 3
    if pressed[pygame.K_RIGHT]: points[0] += 3
    if pressed[pygame.K_u]:width += 1
    if pressed[pygame.K_d]:width -= 1

    screen.fill((0, 0, 0))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)

    pygame.draw.circle(screen, color,points,width);
    pygame.display.flip();
    clock.tick(75);