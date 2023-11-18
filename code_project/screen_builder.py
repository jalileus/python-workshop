import pygame
from button import Button

pygame.init()

SCREENWIDTH = 720  # set the screen width to 720
SCREENHEIGHT = 720  # set the screen height to 720
GRIDSIZE = 20  # set the grid size to 20
GRIDWIDTH = 720 / GRIDSIZE  # set the grid width
GRIDHEIGHT = 720 / GRIDSIZE  # set the grid height

WINDOW = pygame.display.set_mode(
    (SCREENWIDTH, SCREENHEIGHT)
)  # set the screen resolutin
FONT = pygame.font.SysFont("bahnschrift", 25)  # set text font
BUTTONSCALE = pygame.image.load("assets/button_image.png")  # load the button image
BUTTONSCALE = pygame.transform.scale(BUTTONSCALE, (230, 90))  # scale the button


def get_font(size):
    return pygame.font.Font("assets/The Augusta.otf", size)


def get_button(image, pos, text, size, main_color, hovering_color):
    return Button(
        image=image,
        pos=pos,
        text_input=text,
        font=get_font(size),
        main_color=main_color,
        hovering_color=hovering_color,
    )
