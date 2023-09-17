**HOW TO MOVE:**

-   Use UP and DOWN arrow keys to navigate around main screen and settings.
-   Use ENTER key to select an option.
-   Use LEFT and RIGHT arrow keys to change settings

**GRID SIZE:**

-   Changes the size of the maze, ranges from 10 - 35 units.

**SIDE LENGTH:**

-   Scales the size of the screen, ranges from 10 - 15 units

**GAME MODES:**

_1. Solo_

-   Timed single player game mode, start from one corner to maze and try to get to the end.

_2. Two Player_

-   Play against opponent, both starting at opposing corners and attempt to get to each others starting position. Player one (Green) uses the arrow keys to move and player two (Blue) uses WASD to move.

_3. Race_

-   Similar to two player mode except you are racing against a bot. Player starts at one end and has to get to the other end before the bot.

_4. Chase_

-   Player and bot start at the same position, player is given a couple seconds to get away beforethe bot begins to chase you. If you are touched by the bot, you lose. If you make it to other side of the without touching the bot, you win.

_5. Escape_

-   Similar to chase except there are 8 keys that must be collected before the end point opens up. The bot will start chasing you after a couple seconds, the bot will speed up every 2 keys collected. The player starts has a WB (wall break) item and can break a single wall by holding down the direction you want to break and holding the SPACEBAR down. Player also receives a wall break item after every 2 keys collected.

**NOTES:**

-   Once a game has been played, the settings will not be saved and will have to be selected again.
-   Use ESC key to exit current game.

# CODE STRUCTURE

**main.py:**

-   Contains game mechanics and maze generation

**astar.py:**

-   astar algorithm that is used to calculate shortest path, running time of O(|E|log|E|)

**character.py:**

-   Contains character class for movement of character and game objectives

**ui_file.py:**

-   Contains code for main screen, settings and end game screen

**graph.py**

-   From lecture, aids in the generation of the maze.

# HOW TO RUN

1. If pygame is not installed, install pygame package by calling 'sudo pip3 install pygame' for systems running Ubuntu
2. run by calling 'python3 main.py' in terminal
