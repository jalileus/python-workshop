import pygame
import sys
import screen_builder
import screen_builder
from creat_buttons import CreatButtons

COLOR = "black"


class Options:
    def ChangeColor(self, new_color):
        global COLOR
        COLOR = new_color

    def OptionScreen(self):  # option screen
        pygame.display.set_caption("Options")
        screen_builder.WINDOW.fill("black")
        option_background = pygame.image.load("assets/options_background.jpg")
        option_background = pygame.transform.scale(
            option_background, (screen_builder.SCREENWIDTH, screen_builder.SCREENHEIGHT)
        )  # scale the new background

        while True:
            mouse_pos = pygame.mouse.get_pos()

            screen_builder.WINDOW.blit(
                option_background, (0, 0)
            )  # put the background of the screen

            color_text = screen_builder.FONT.render(
                "choose the color of the snake:", True, "green", "darkgreen"
            )  # add color change text to the screen
            color_text_rect = color_text.get_rect(center=(200, 30))  # text position

            # creat buttons
            back_button = CreatButtons.BackButton()

            color_button_1 = CreatButtons.ColorButton1()

            color_button_2 = CreatButtons.ColorButton2()

            color_button_3 = CreatButtons.ColorButton3()

            screen_builder.WINDOW.blit(color_text, color_text_rect)

            # check hovering over the buttons
            for button in [back_button, color_button_1, color_button_2, color_button_3]:
                button.ChangeColor(mouse_pos)
                button.Update(screen_builder.WINDOW)

            for event in pygame.event.get():
                global COLOR
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.ClickCheck(
                        mouse_pos
                    ):  # play again if the clicked button is replay
                        import main_ui

                        main = main_ui.MainScreen()
                        main.MainMenuScreen()
                    elif color_button_1.ClickCheck(mouse_pos):
                        self.ChangeColor("black")
                        print("color changed to black")

                    elif color_button_2.ClickCheck(mouse_pos):
                        self.ChangeColor("blue")
                        print("color changed to blue")

                    elif color_button_3.ClickCheck(mouse_pos):
                        self.ChangeColor("violet")
                        print("color changed to violet")

            pygame.display.update()
