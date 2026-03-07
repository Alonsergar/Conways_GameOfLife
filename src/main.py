# Example file showing a circle moving on screen
import pygame
#Usamos get_monitors para sacar la altura y la anchura para hacer que la ventana ocupe toda la pantalla
from grid import create_grid,redo_grid
from tile import Tile,get_tiles_preset1,next_age,alive_in_map,draw_tiles,get_tiles_dead
import time
from font import draw_text
pygame.init()
gen=0
height=720
width=1280
length_tiles=20


screen=create_grid(height,width,length_tiles)
font=pygame.font.SysFont("Arial",20)


tiles=get_tiles_dead(length_tiles,height,width)

clock = pygame.time.Clock()
running = True
started=False

def game_loop():
    global gen
    redo_grid(height,width,length_tiles,screen)
    next_age(tiles,screen)
    draw_tiles(tiles,screen)
    draw_text(font,alive_in_map(tiles),gen,screen)
    
    
    gen+=1
   
    clock.tick(10)  # 10 generaciones por segundo
    

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    if started:
        game_loop()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_s] and started==False:
        started=True
        game_loop()
        

    if pygame.mouse.get_pressed()[0] and started==False:
        x,y= pygame.mouse.get_pos()
        #ahora tenemos que poner como vivo la zona en la que se hizo click
        x=x//length_tiles
        y=y//length_tiles
        tile=tiles[y][x]
        tile.set_alive(screen)
        tiles[y][x]=tile

    
    # flip() the display to put your work on screen
    pygame.display.flip()
  

   

pygame.quit()