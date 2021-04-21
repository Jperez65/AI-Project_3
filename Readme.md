# Assignment 3: problem 3

## Compiling Program
To compile file you must have python 3.8.5 ver installed in your system environment or use any other IDE programs. 
After that you must go to the directory where the program is located and write 

''' 
python Project3.py
'''

to your console terminal

## Running Program

When running the program it will output a this message:


>Welcome to my Hexagon game:
>Which player would you be the ai? Player 1 or Player 2 
>

You will need to designate which player the ai would start, as 1 represent solid line and 2 represent dashe line. You as the player would be pick the opposite from the ai. Afterward, the terminal will output the turn of the player based on the ordering it has been assign to:


>AI turn

or 


>Your turn now:


When it the players turn it would ask two vertex from where to form a line and show the matrix map to see which point are available. Index that are 0 means that it is a valid move, 1 for player 1 and 2 for player 2.


>Your turn now:
>
>Map:
>
>[0, 1, 0, 0, 2, 0]
>
>[1, 0, 1, 0, 2, 0]
>
>[0, 1, 0, 2, 0, 0]
>
>[0, 0, 2, 0, 0, 0]
>
>[2, 2, 0, 0, 0, 2]
>
>[0, 0, 0, 0, 2, 0]


If the player or Ai makes a move that leads it to lose the it output the player or ai has one.


>You won the game
>
>[0, 1, 1, 0, 2, 1]
>
>[1, 0, 1, 0, 2, 0]
>
>[1, 1, 0, 2, 0, 0]
>
>[0, 0, 2, 0, 0, 0]
>
>[2, 2, 0, 0, 0, 2]
>
>[1, 0, 0, 0, 2, 0]

Fair warning for when it is turn of the Ai there is no alpha beta prunning or depth limit thus it may take more than a minute for the ai to compute a designated move set. While the ai player is searching for a move it would output this message


>Ai is thinking of a move


To let the human player that it still in the process of thinking. However to verify if its functionality are in working condition you can change the initial game chart to one that has already move set up as it reduce the time it checks for move set.

## Classes and function

File only contain one class, Hexagon class, where it contain all the necessary function to create a minimax algorithm game

### Class Hexagon

##### cycle_check

Fucntion check from given array, that has a list of position that are connected to a single node, and check from it if other nodes are connected to the player.

##### check_win

Function verify on the board graph if player 1 or player 2 has form a triangle connection


##### minimax

Function follow rules based on minimax algorithm for which it returns value that represent the best option for the player to branch out for the next state

##### next_moved

Function begins the process of calcualtion the best moves to picked based by calculating it from minimax function. When move is found it is then added to the graph

##### player_dec

Function assign the player roles between the ai and human player

##### human_moved

Function checks the input  values, representing vertexes, from the human player if their are valid or not

##### print_graph

Function that prints the graph to show the current state of the game

##### play_session

Main function that where the players will be inputing and initiating move action in the game.

### Author
Josue Perez

