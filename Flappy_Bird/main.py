import pygame
from pygame.locals import *
import random

pygame.init()
screen_width = 764
screen_height = 936
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy bird by AD_LiN")
bg = pygame.image.load("Flappy_Bird/assets/bg_5.png").convert_alpha()
bg = pygame.transform.scale(bg, (screen_width, screen_height ))
ground_image = pygame.image.load("Flappy_Bird/assets/ground.png").convert_alpha()
button_image = pygame.image.load("Flappy_Bird/assets/restart.png").convert_alpha()
#ground_image = pygame.transform.scale(ground_image, (864, 936))

running = True

# font for text
font = pygame.font.SysFont('Bauhaus 93', 60)

# for the color
white = (255, 255, 255)

# Game variables
fps = 60
ground_scroll = 0
scroll_speed = 4
ground_height = int(screen_height * 0.28)
playable_height = screen_height - ground_height
ground_y = 600
flying = False
game_over = False
pipe_gap = int(screen_height * 0.23)
pipe_width = int(screen_width * 0.13)
pipe_height = int(screen_height * 0.58)
pipe_frequency = 1500 #miliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

# Keep the ground image wide enough to scroll smoothly and anchor it to the bottom edge.
ground_image = pygame.transform.scale(ground_image, (screen_width + 120, ground_height))

# For score and other funct
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# reset game
def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen.get_height()/2) - 150 
    score = 0
    return score
   


# class for the bird
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        # list of images for the animations
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'Flappy_Bird/assets/bird{num}.png')
            # transform the image to a smaller size
            img =  pygame.transform.scale(img, (50, 50)) 
            self.images.append(img)
        
        self.image = self.images[self.index]
      
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.velocity = 0
        self.click = False

    def update(self):
    # The bird Physics

        if flying == True:
            # Gravity
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8

            if self.rect.bottom < ground_y:
                self.rect.y += int(self.velocity)
        if game_over == False:
            # Jumping 
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.velocity = -10
                self.click = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False


        # animation handling

            self.counter += 1
            flap_cooldown = 5

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

        # Rotate bird handling
            self.image = pygame.transform.rotate(self.images[self.index], self.velocity * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Flappy_Bird/assets/pipe.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (pipe_width, pipe_height))
        self.rect = self.image.get_rect()
        # position 1 is from the top -1 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
        if position == -1:
            self.rect.topleft = (x, y + int(pipe_gap / 2))

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        
        mou_clicked = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check if mouse is over button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                mou_clicked = True

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return mou_clicked

# create a group for the bird and the pipes
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100, int(screen.get_height()/2) - 150 )

# add the bird to the group
bird_group.add(flappy)

# button instnace
button = Button(screen_width // 2 - 50, screen_height / 2 - 180, button_image)


while running:
    clock.tick(fps)
    
    # Draw the background
    screen.blit(bg, (0,0))

    # Draw the bird
    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)

    # Draw the ground
    screen.blit(ground_image, (ground_scroll, ground_y))

    # check the score
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and pass_pipe == False:
            pass_pipe = True
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False
    
    score_dis = f'YOUR SCORE : {score}'

    draw_text(score_dis, font, white, int(screen.get_height()/2) - 100, 20)


    # look for collision
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True
        
    
    # Check if bird has hit the ground
    if flappy.rect.bottom >= ground_y:
        game_over = True
        flying = False

    if game_over == False and flying == True:
        # generate new pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            gap_y = random.randint(int(playable_height * 0.25), int(playable_height * 0.7))
            btm_pipe = Pipe(screen_width, gap_y, -1)
            top_pipe = Pipe(screen_width, gap_y, 1)

            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

        # Scroll the ground
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > ground_image.get_width() - screen.get_width():
            ground_scroll = 0

        pipe_group.update()


    #check for gameover to reset
    if game_over == True:
       if button.draw() == True:
           game_over = False
           score = reset_game()



    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    pygame.display.flip()
    pygame.display.update()    

pygame.quit()