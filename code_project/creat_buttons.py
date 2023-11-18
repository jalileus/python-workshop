import screen_builder


# class to creat buttons
class CreatButtons:
    def ColorButton1():
        return screen_builder.get_button(
            screen_builder.BUTTONSCALE,
            (150, 100),
            "black",
            50,
            "white",
            "black",
        )

    def ColorButton2():
        return screen_builder.get_button(
            screen_builder.BUTTONSCALE,
            (150, 200),
            "blue",
            50,
            "white",
            "blue",
        )

    def ColorButton3():
        return screen_builder.get_button(
            screen_builder.BUTTONSCALE,
            (150, 300),
            "violet",
            50,
            "white",
            "violet",
        )

    def BackButton():
        return screen_builder.get_button(
            screen_builder.BUTTONSCALE,
            (360, 600),
            "back",
            50,
            "white",
            "green",
        )

    def StartButton():
        return screen_builder.get_button(
            screen_builder.BUTTONSCALE,
            (360, 250),
            "PLay",
            50,
            main_color="white",
            hovering_color="green",
        )

    def OptionButton():
        return screen_builder.get_button(
            screen_builder.BUTTONSCALE,
            (360, 350),
            "Options",
            50,
            "white",
            "green",
        )

    def QuitButton():
        return screen_builder.get_button(
            screen_builder.BUTTONSCALE,
            (360, 450),
            "Quit",
            50,
            "white",
            "red",
        )
