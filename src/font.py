import pygame
from grid import redo_grid
from tile import next_age


def draw_text(font,alive,generation,screen):
    text=f"Cells: {alive} Generation: {generation}"
    img=font.render(text,True,"white")
    size=(screen.get_width(),screen.get_height())
    center=size[0]/2
    max_h=size[1]

    screen.blit(img,(center,max_h-100))