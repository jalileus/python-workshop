import pygame
import random
import sys
import screen_builder

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self, color):
        self.length = 1  # starting length of the snake
        self.pos = [
            (int(screen_builder.SCREENHEIGHT / 2), int(screen_builder.SCREENHEIGHT / 2))
        ]  # x and y position of the snake(center of the screen)
        self.direction = random.choice(
            [UP, DOWN, LEFT, RIGHT]
        )  # random direction of the head of the snake
        self.color = color

    def GetHead(self):  # method to return the position of the head of the snake
        return self.pos[0]

    def Turn(self, point):  # method to check how the snake can turn
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def DrawSnake(self, window, snake_color):  # method to draw the snake on the screen
        for position in self.pos:
            rect = pygame.Rect(
                (position[0], position[1]),
                (screen_builder.GRIDSIZE, screen_builder.GRIDSIZE),
            )
            pygame.draw.rect(window, self.color, rect)
            pygame.draw.rect(window, snake_color, rect, 1)

    def Control(self):  # method to control the snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.Turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.Turn(DOWN)
                elif event.key == pygame.K_RIGHT:
                    self.Turn(RIGHT)
                elif event.key == pygame.K_LEFT:
                    self.Turn(LEFT)


class Food:
    def __init__(self):
        self.pos_food = (0, 0)  # position of the food
        self.pos_bouns = (0, 0)  # position of the bouns
        self.color_food = "red"  # color of the food
        self.color_bouns = "green"  # color of bouns
        self.RandomizeFood()
        self.RandomizeBouns()

    def RandomizeFood(self):  # method to randomize the poition of the food
        self.pos_food = (
            random.randint(0, screen_builder.GRIDWIDTH - 1) * screen_builder.GRIDSIZE,
            random.randint(0, screen_builder.GRIDHEIGHT - 1) * screen_builder.GRIDSIZE,
        )

    def RandomizeBouns(self):  # method to randomize the poition of the food
        self.pos_bouns = (
            random.randint(0, screen_builder.GRIDWIDTH - 1) * screen_builder.GRIDSIZE,
            random.randint(0, screen_builder.GRIDHEIGHT - 1) * screen_builder.GRIDSIZE,
        )

    def DrawFood(self, window):  # method to draw the obejct of the food
        rect = pygame.Rect(
            (self.pos_food[0], self.pos_food[1]),
            (screen_builder.GRIDSIZE, screen_builder.GRIDSIZE),
        )
        pygame.draw.rect(window, self.color_food, rect)
        pygame.draw.rect(window, "red", rect, 1)

    def SlowBonus(self, window, scour):
        if scour == 5 or scour == 15 or scour == 20 or scour == 45:
            rect = pygame.Rect(
                (self.pos_bouns[0], self.pos_bouns[1]),
                (screen_builder.GRIDSIZE, screen_builder.GRIDSIZE),
            )
            pygame.draw.rect(window, self.color_bouns, rect)
            pygame.draw.rect(window, "black", rect, 1)
        else:
            return
