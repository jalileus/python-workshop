class Button:
    def __init__(self, image, pos, text_input, font, main_color, hovering_color):
        self.image = image  # the shape of the button
        self.x_pos = pos[0]  # the x-position of the button
        self.y_pos = pos[1]  # the y-postion of the button
        self.font = font  # the font of the text
        self.main_color = main_color  # the color of the text
        self.hovering_color = hovering_color  # the changed color of the text when we hover over the button
        self.text_input = text_input  # the text of the button
        self.text = self.font.render(
            self.text_input, True, self.main_color
        )  # initialize the text with font and color
        if (
            self.image is None
        ):  # if we don't pass an image then just make it a text button
            self.image = self.text
        self.rect = self.image.get_rect(
            center=(self.x_pos, self.y_pos)
        )  # to check the input later
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def Update(self, window):
        if self.image is not None:
            window.blit(
                self.image, self.rect
            )  # put the button image on the screen using rect for the position
        window.blit(self.text, self.text_rect)  # put the text on the button

    def ClickCheck(self, position):  # method to check if we are clicking the button
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1
        ] in range(
            self.rect.top, self.rect.bottom
        ):  # we are hovering over the button
            return True
        return False

    def ChangeColor(
        self, position
    ):  # method to change the color of the text when we hover over the button
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1
        ] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.main_color)
