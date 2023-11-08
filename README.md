# about python-workshop:
This repository contains Python project of the famous game the Snake game, the repository contains 2 folders:

1.assets folder contains the assets required for the game(backgrounds images,button imgages,font file of the text).
2.code_project folder contains all the code scripts:

`main_ui.py`(script for the main menu)
//`creat_buttons.py`(script used to create the buttons on the screen using the button script)
//`button.py`(script contains a class Button to creat a button and change its color and check for clicks),
//`gameover_screen.py`(script that initialize the screen menu when the game is over and it has methods to replay or to go back to the main menu)
//`screen_builder.py`(script that initialize the main screen of pygame it contains constants like screen width and height etc..)
//`play_screen.py`(script that initialize the screen for the play mode game and move the snake and draw the background and the food etc.., in addition record the score and the level of the game)
//`set_level.py`(script that increase the acceleration of the snake, and set the level for the game)
//`obeject.py`(script contains two classes Snake and Food, it initializr the food and the snake inside the game)
//`options.py`(script contains the options screen in which it has methods to change the color of the snake)
//`main.py`(script main or the code caller)

# how to run:
1.you need to download `pygame` version: `2.5.2` :
linux: open the terminal and type the comand: `sudo apt-get install python3-pygame`
windows: open windows powershell and type the comand: `pip install pygame`
Note: if you are facing a trouble downloading pygame you can have a look at the link : `https://www.pygame.org/wiki/GettingStarted`
2.after downloading pygame you can run the main.py code in the platform you using preferably (Visual Studio 1.84.0) but it should work in any other plateforms

# how to play:
when you run the code that will take you to a screen the main menu screen of the game, you have three buttons (play,otions,quit)
quit: exit the game
options: allow you to choose the color of the snake (you can choose one of the three colors(black,violet,blue)) in case you did not choose a color the defualt color is black
play: start the game, you start the game where the snake is moving on a surface and the food appears in a red color you have score and level the more you score the more your level will increase and when the level increase the snake will speed up more, the snake gets longer the more you eat, each one piece of food you eat increase your score by one and the max level you can get is 8,from time to time a green piece will appear its a bouns! eat it,don't be afraid it will increase your length twice and your score as well, or you can just avoid it but it will disappear
