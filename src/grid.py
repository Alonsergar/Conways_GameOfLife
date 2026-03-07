import pygame


        
#the screen for now will have a resolution of 1280*720 the top left corner is (0,0)
def create_grid(height,width,lenght_tile):
    screen=pygame.display.set_mode((width+1,height+1))
   
    screen.fill("black")
    for i in range(0,int(width/lenght_tile)+1):
        pygame.draw.line(start_pos=(i*lenght_tile,0),end_pos=(i*lenght_tile,height),surface=screen,color="grey")
    for i in range(0,int(height/lenght_tile)+1):
        pygame.draw.line(start_pos=(0,i*lenght_tile),end_pos=(width,i*lenght_tile),surface=screen,color="grey")
   
    return screen

def redo_grid(height,width,lenght_tile,screen):
    
    screen.fill("black")
    for i in range(0,int(width/lenght_tile)+1):
        pygame.draw.line(start_pos=(i*lenght_tile,0),end_pos=(i*lenght_tile,height),surface=screen,color="grey")
    for i in range(0,int(height/lenght_tile)+1):
        pygame.draw.line(start_pos=(0,i*lenght_tile),end_pos=(width,i*lenght_tile),surface=screen,color="grey")
   
    return screen

def fill_cell(tile):
    pygame.draw.rect(tile.pos,tile.alive)
    