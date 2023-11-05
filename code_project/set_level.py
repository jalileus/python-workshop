import pygame


class Level:
    def get_speed(curr_level):  # method to change the speed of the snake
        clock = pygame.time.Clock()  # clock counter
        if curr_level == 0:
            return clock.tick(5)
        if curr_level == 1:
            return clock.tick(10)
        elif curr_level == 2:
            return clock.tick(13)
        elif curr_level == 3:
            return clock.tick(15)
        elif curr_level == 4:
            return clock.tick(20)
        elif curr_level == 5:
            return clock.tick(30)
        elif curr_level == 6:
            return clock.tick(40)
        elif curr_level == 7:
            return clock.tick(50)
        elif curr_level == 8:
            return clock.tick(60)

    def get_level(curr_score):  # method to get the current level
        if curr_score >= 0 and curr_score <= 8:
            return 1
        elif curr_score > 8 and curr_score <= 15:
            return 2
        elif curr_score > 15 and curr_score <= 25:
            return 3
        elif curr_score > 25 and curr_score <= 35:
            return 4
        elif curr_score > 35 and curr_score <= 45:
            return 5
        elif curr_score > 45 and curr_score <= 70:
            return 6
        elif curr_score > 70 and curr_score < 100:
            return 7
        elif curr_score > 100:
            return 8
