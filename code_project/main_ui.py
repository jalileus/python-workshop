import pygame
import sys
import screen_builder
from creat_buttons import CreatButtons


class MainScreen:  # main menu screen
    def MainMenuScreen(self):
        pygame.display.set_caption("Main Menu")
        main_screen_background = pygame.image.load(
            "assets/game_background.jpg"
        )  # upload image for the backround

        main_screen_background = pygame.transform.scale(
            main_screen_background,
            (screen_builder.SCREENWIDTH, screen_builder.SCREENHEIGHT),
        )  # scale the main screen background
        print("welcome to the snake game!")
        while True:
            screen_builder.WINDOW.blit(
                main_screen_background, (0, 0)
            )  # set the main screen background on the screen

            mouse_pos = pygame.mouse.get_pos()  # get the mouse position

            menu_text = screen_builder.FONT.render(
                "WELCOME TO THE SNAKE GAME", True, "green", "darkgreen"
            )  # add a text to the screen
            menu_rect = menu_text.get_rect(center=(360, 30))  # text_menu position

            # creating buttons from Button class
            start_button = CreatButtons.StartButton()

            option_button = CreatButtons.OptionButton()

            quit_button = CreatButtons.QuitButton()

            screen_builder.WINDOW.blit(menu_text, menu_rect)  # initilize the screen

            for button in [start_button, option_button, quit_button]:
                button.ChangeColor(mouse_pos)
                button.Update(screen_builder.WINDOW)

            for (
                event
            ) in pygame.event.get():  # iteration through all the events in pygame
                if event.type == pygame.QUIT:  # if we pressed the ECS button
                    pygame.quit()  # quit the screen
                    sys.exit()
                elif (
                    event.type == pygame.MOUSEBUTTONDOWN
                ):  # if we clicked the mouse button
                    if start_button.ClickCheck(mouse_pos):
                        import play_screen

                        play = play_screen.Play()
                        play.PlayScreen()
                    elif option_button.ClickCheck(mouse_pos):
                        import options_screen

                        option = options_screen.Options()
                        option.OptionScreen()
                    elif quit_button.ClickCheck(mouse_pos):
                        print("good bye!")
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
