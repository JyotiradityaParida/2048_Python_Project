2048 GAME
-----------

We made a simple CLI version of the 2048 game.
It includes sliding and merging logic, random tile generation, victory and game-over detection, a complete save/load system, high-score tracking and RNG state saving for reproducibility.
It has a modular structure with separate files for board display, game logic, and data handling.

Features-  
--------
• 4x4 2048 board  
• Sliding and merging (left,right,up,down)  
• Random tile generation (2 or 4)  
• Victory detection when 2048 tile appears  
• Game over detection  
• Save and load game state (board,score,moves)  
• High score saved separately  
• Simple CLI interface  
• Modular Python files  

Directory Structure-  
------------------
• main.py - main program  
• board.py - board creation and printing  
• game_logic.py - movement, merging, rotation, random tile spawning  
• file_manager.py - save/load system and high score  
• README.md - documentation  
• data/ - folder for save file and highscore  
  2048_save.txt  
  highscore.txt  

Controls-  
---------
• W - Move Up  
• A - Move Left  
• S - Move Down  
• D - Move Right  
• K - Save Game  
• L - Load Game  
• P - Reset High Score  
• Q - Quit  

Persistence (Save/Load System)-  
-------------------------------
• Game state is saved as JSON into:  
data/2048_save.txt  

• The saved data includes:  
board, score, moves  

• High score is saved in:  
data/highscore.txt  

• Both files are created automatically if missing.  

• It also saves/loads RNG state for reproducibility

Gameplay Logic Summary-  
---------------------
Movement works by:  
• slide(row) - pushes non-zero tiles to the left  
• merge(row) - merges equal tiles once per move  
• slide(row) again  

• move_left(board) - full left movement  
• rotate(board) - rotate board to reuse left-move logic  
• move_board(board, key) - handles W/A/S/D using rotation  

Random tile generation:  
• 90% chance of generating 2  
• 10% chance of generating 4  

Game over condition:  
• No empty cell  
• No possible adjacent merges  

Victory:  
• The game displays a victory message when a 2048 tile is created.  

Requirements-  
-----------
• No external libraries needed.  
• Uses only Python modules: random, os, json, time  

Setup Instructions-  
---------------
• Download the repository  
• Open a terminal inside the project folder  
• Run: python main.py  
