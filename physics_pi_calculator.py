import pygame

screen = pygame.display.set_mode((1200, 500))
pygame.font.init()
pygame.mixer.init()

click_sound = pygame.mixer.Sound('click.wav')

running = True

digits = 4

class box:
    def __init__(self, mass, velocity, pos):
        self.mass = mass
        self.velocity = velocity
        self.pos = pos

box1 = box(1, 0, 300)
box2 = box(100**(digits-1), -0.00005, 500)

collusions = 0

font = pygame.font.Font('freesansbold.ttf', 50)

text = font.render(str(collusions), True, (255, 255, 255))

timesteps = 10000

while running:
    screen.fill((0, 0, 0))

    text = font.render(str(collusions), True, (255, 255, 255))

    screen.blit(text, (100, 0))
    if box1.pos > 0:
        pygame.draw.rect(screen, (255, 0, 0), (box1.pos, 460, 40, 40))
    else:
        pygame.draw.rect(screen, (255, 0, 0), (0, 460, 40, 40))
    if box2.pos > 40:
        pygame.draw.rect(screen, (0, 255, 0), (box2.pos, 500-digits*40, digits*40, digits*40))
    else:
        pygame.draw.rect(screen, (0, 255, 0), (40, 500-digits*40, digits*40, digits*40))

    for i in range(timesteps):

        box1.pos += box1.velocity
        box2.pos += box2.velocity

        if box1.pos+40 >= box2.pos:
            box1_vel = box1.velocity
            box1.velocity = ((box1.mass-box2.mass)/(box1.mass+box2.mass))*box1.velocity + (2*box2.mass/(box1.mass+box2.mass))*box2.velocity
            box2.velocity = ((box2.mass-box1.mass)/(box1.mass+box2.mass))*box2.velocity + (2*box1.mass/(box1.mass+box2.mass))*box1_vel

            collusions += 1

            pygame.mixer.Sound.play(click_sound)

        if box1.pos <= 0:
            pygame.mixer.Sound.play(click_sound)
            box1.velocity *= -1
            collusions += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

print(collusions)