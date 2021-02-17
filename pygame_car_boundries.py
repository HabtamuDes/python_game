import pygame

pygame.init()

display_width = 800
display_height = 800

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 318
car_hight = 159

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit racey')

clock = pygame.time.Clock()
carImg = pygame.image.load("/home/warcraft/Videos/pygame_code/beatle.jpg")

def car(x, y):
    gameDisplay.blit(carImg,(x, y))

def  game_loop():
        
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5   
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0             
        
        x += x_change

        gameDisplay.fill(white)        
        car(x, y)

        if x > display_width - car_width or x < 0:
            gameExit = True

        pygame.display.update()
        
        clock.tick(60)
game_loop()
pygame.quit()
quit()    