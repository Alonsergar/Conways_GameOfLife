#abría que tener en el tiles algo de padding para cuando las celulas se acerquen al límite


import pygame
class Tile():
    #state: 1=alive 0=dead
    def __init__(self,alive:bool,pos:tuple[int,int],lenght):
        #each position is given by the right top corner position, from that we calculate the rest
        self.pos=pos
        self.alive=alive
        self.lenght=lenght
    def __repr__(self):
        return f"Pos=[x={self.pos[0]} y={self.pos[1]}] alive={self.alive}"
    
    def set_alive(self,screen):
        self.alive=True
        pygame.draw.rect(surface=screen,rect=((self.pos[0]+1,self.pos[1]+1),(self.lenght-1,self.lenght-1)),color="white")
    
    def set_dead(self,screen):
        self.alive=False
        pygame.draw.rect(surface=screen,rect=((self.pos[0]+1,self.pos[1]+1),(self.lenght-1,self.lenght-1)),color="black")


def get_tiles_dead(lenght,height,width):
    tiles=[]
    for h in range (0,int(height/lenght)):
        new_row=[]
        for w in range(0,int(width/lenght)):
            new_row.append(Tile(False,(w*lenght,h*lenght),lenght=lenght))
        tiles.append(new_row)
    return tiles

def get_tiles_preset1(lenght,height,width,screen):
    tiles=[]
    for h in range (0,int(height/lenght)):
        new_row=[]
        for w in range(0,int(width/lenght)):
            new_row.append(Tile(False,(w*lenght,h*lenght),lenght=lenght))
        tiles.append(new_row)
    
    #setting preset
    acorn = [(18, 31),(19, 33),(20, 30), (20, 31), (20, 34), (20, 35), (20, 36)]
    glider = [(1, 2),(2, 3),(3, 1), (3, 2), (3, 3),
]
    for i in acorn:
        tiles[i[0]][i[1]].set_alive(screen)
    return tiles
#aqui tenemos que implementar la lógica del juego para cada iteración
def calculate_alive_neighbours(tiles,cercanos):
    count=0
    for cercano in cercanos:
        if 0<= cercano[0] <len(tiles) and 0<=cercano[1]<len(tiles[0]):
            if tiles[cercano[0]][cercano[1]].alive:
                count+=1
    return count



def next_age(tiles,screen):
    list_to_setAlive=[]
    list_to_setDead=[]
    for row in range(0,len(tiles)):
        for col in range(0,len(tiles[0])):
            cercanos = [(row-1, col-1), (row-1, col), (row-1, col+1),(row,   col-1),(row,   col+1),(row+1, col-1), (row+1, col), (row+1, col+1)]
            alive_neighbour=calculate_alive_neighbours(tiles,cercanos)
            if tiles[row][col].alive:
                if alive_neighbour<2 or alive_neighbour>3:
                    list_to_setDead.append(tiles[row][col])
            elif not tiles[row][col].alive:
                if alive_neighbour==3:
                    list_to_setAlive.append(tiles[row][col])
    
    
    
    
    for t in list_to_setDead:
        t.alive = False
    for t in list_to_setAlive:
        t.alive = True

def alive_in_map(tiles):
    count=0
    for row in tiles:
        for tile in row:
            if tile.alive:
                count+=1
    return count


def draw_tiles(tiles, screen):
    for row in tiles:
        for tile in row:
            if tile.alive:
                pygame.draw.rect(surface=screen,rect=((tile.pos[0]+1,tile.pos[1]+1),(tile.lenght-1,tile.lenght-1)),color="white")
            else:
                pygame.draw.rect(surface=screen,rect=((tile.pos[0]+1,tile.pos[1]+1),(tile.lenght-1,tile.lenght-1)),color="black")