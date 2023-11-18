import pygame
import sys
import screen_builder
from button import Button


class GameOver:
    def GameOverScreen(self, score, level):
        pygame.display.set_caption("Game Over")
        screen_builder.WINDOW.fill("black")
        new_background = pygame.image.load(
            "assets/gameover_background.jpg"
        )  # load the background for the option
        new_background = pygame.transform.scale(
            new_background, (screen_builder.SCREENWIDTH, screen_builder.SCREENHEIGHT)
        )  # scale the new background
        text_level = screen_builder.FONT.render(f"YOUR LEVEL: {level}", "black", True)

        text_score = screen_builder.FONT.render(f"YOUR SCORE: {score}", "black", True)

        while True:
            mouse_pos = pygame.mouse.get_pos()

            screen_builder.WINDOW.blit(new_background, (0, 0))
            screen_builder.WINDOW.blit(text_score, (280, 100))
            screen_builder.WINDOW.blit(text_level, (280, 150))
            game_over_text = screen_builder.FONT.render(
                "Game over!", True, "red", "darkgreen"
            )  # add a gameover text to the screen
            game_over_text_rect = game_over_text.get_rect(
                center=(360, 30)
            )  # text position

            # create replay and back buttons
            replay_button = Button(
                image=screen_builder.BUTTONSCALE,
                pos=(360, 250),
                text_input="Replay",
                font=screen_builder.get_font(50),
                main_color="white",
                hovering_color="green",
            )
            back_button = Button(
                image=screen_builder.BUTTONSCALE,
                pos=(360, 450),
                text_input="Back",
                font=screen_builder.get_font(50),
                main_color="white",
                hovering_color="green",
            )

            screen_builder.WINDOW.blit(game_over_text, game_over_text_rect)

            for button in [replay_button, back_button]:
                button.ChangeColor(mouse_pos)
                button.Update(screen_builder.WINDOW)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if replay_button.ClickCheck(
                        mouse_pos
                    ):  # play again if the clicked button is replay
                        import play_screen

                        play = play_screen.Play()
                        play.PlayScreen()
                    elif back_button.ClickCheck(
                        mouse_pos
                    ):  # go back to main menu if the clicked button is back
                        import main_ui

                        main = main_ui.MainScreen()
                        main.MainMenuScreen()
            pygame.display.update()
