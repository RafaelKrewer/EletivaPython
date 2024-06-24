import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

pos_x=640
pos_y=320

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:  # Verifica se a tecla para cima foi pressionada
                pos_y -= 10  # Move a posição y para cima
        
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                pos_y += 10

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                pos_x += 10

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                pos_x -= 10

    screen.fill("purple")
    pygame.draw.circle(screen,"green",(pos_x,pos_y),5)
    pygame.display.flip()

clock.tick(60)  
pygame.quit()