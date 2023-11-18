import pygame
import object
import gameover_screen
import screen_builder
from set_level import Level


class Play:
    def DrawGrid(self, surface):  # function to draw a grid
        gh = screen_builder.GRIDHEIGHT
        gw = screen_builder.GRIDWIDTH
        gs = screen_builder.GRIDSIZE
        for y in range(0, int(gh)):
            for x in range(0, int(gw)):
                if (x + y) % 2 == 0:
                    rect_1 = pygame.Rect((x * gs, y * gs), (gs, gs))
                    pygame.draw.rect(surface, ("forestgreen"), rect_1)  # draw a square
                else:
                    rect_2 = pygame.Rect((x * gs, y * gs), (gs, gs))
                    pygame.draw.rect(
                        surface, ("limegreen"), rect_2
                    )  # draw a darker square

    def PlayScreen(self):
        screen = pygame.display.set_mode(
            (screen_builder.SCREENWIDTH, screen_builder.SCREENHEIGHT)
        )
        pygame.display.set_caption("Snake game is running")
        print("you are playing")

        surface = pygame.Surface(
            screen.get_size()
        )  # get the surface to draw a grid on it
        surface = surface.convert()

        self.DrawGrid(screen)
        from options_screen import COLOR

        snake_color = COLOR
        snake = object.Snake(color=snake_color)
        food = object.Food()

        score = 0
        counter = 0

        pygame.display.update()
        while True:  # run the game
            new_level = Level.get_level(score)  # get the new level
            level = new_level
            Level.get_speed(level)  # get the speed of the snake
            snake.Control()  # call the method to control the snake
            self.DrawGrid(screen)
            # move the snake
            current_head_pos = snake.GetHead()
            x, y = snake.direction
            new_head_pos = (
                (
                    (current_head_pos[0] + (x * screen_builder.GRIDSIZE))
                    % screen_builder.SCREENWIDTH
                ),
                (
                    (current_head_pos[1] + (y * screen_builder.GRIDSIZE))
                    % screen_builder.SCREENHEIGHT
                ),
            )
            if (
                len(snake.pos) > 2 and new_head_pos in snake.pos[2:]
            ):  # if there is an overlabing between the snake and other part of it
                pygame.time.delay(1000)
                print("game over!,you lost")
                print("your score = ", score)
                print("your level = ", level)
                game = gameover_screen.GameOver()
                game.GameOverScreen(score, level)
            else:
                snake.pos.insert(0, new_head_pos)  # add the new head positon
                if len(snake.pos) > snake.length:
                    snake.pos.pop()  # pop the last element
            if (
                snake.GetHead() == food.pos_food
            ):  # if the head of the snake touched the food
                snake.length += 1  # increment the length of the snake
                score += 1  # increment the score
                food.RandomizeFood()  # randomize the position of the next food object
            if snake.GetHead() == food.pos_bouns:
                snake.length += 2
                score += 3
                food.RandomizeBouns()
            snake.DrawSnake(screen, snake_color)  # draw snake
            food.DrawFood(screen)  # draw food
            food.SlowBonus(screen, score)
            screen.blit(screen, (0, 0))
            text = screen_builder.FONT.render("Score {0}".format(score), 1, (0, 0, 0))
            screen.blit(text, (5, 10))
            text_level = screen_builder.FONT.render(f"Level = {level}", "black", True)
            screen.blit(text_level, (620, 10))
            pygame.display.update()
