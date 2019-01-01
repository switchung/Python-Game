A description of your program and its features:
    My program is a tactical strategy game inspired by other games including Fire Emblem and Advanced Wars!
    There are 5 levels total, each with different units, enemies, obstacles, and strategies. Levels are not particularly balanced and fair to the point I am comfortable with. Click to select units and to attack (or not) when prompted, and use keyboard inputs to move. It is a 1 player game against a simple AI.
    
Instructions for how to run your program, especially if you submit multiple Python files:
    Simply run invasion_tactics.py, and click of any level to begin playing.
    This program also uses graphics.py and Button.py
    Button.py is a modified version, so the original in class version will NOT suffice.
    
A brief description and justification of how it is constructed (classes, functions, etc.):
    The program was constructed mainly based off of two classes: Pieces and GameBoard
    GameBoard drew the board and obstacles dependent on the level selected, and
    Pieces constructed the units, stored the unit values for both the player and AI,
    and contained the methods for unit/game functionality
    
A brief reflection on the greatest design or implementation challenge you faced and how you responded to it:
    This was a fairly large endeavor for me, and so the greatest challenge was the time constraint. Although the program is fully functional and there are no game-breaking bugs, the time constraint had me a little rushed and so I was forced to cram in bug fixes that may not have been as efficient as I would have liked. The program also ended up being a little bit larger than I would have thought, and so I do believe that with more time or even a better plan I could have the program running much more efficiently.

A discussion of the current status of your program. In particular, report any known bugs:
    No known bugs, although certain bugs such as the text disappearing on redrawn buttons forced me to implement certain workarounds such as repeated reinitializions of the button. Otherwise, this is a fully functional program. Level design may not be particularly balanced, and ai pathfinding may be flawed/ a bit laggy at times.

Game Walkthrough / Info:
    After all enemy units have been destroyed, the player must manually end his/her turn to exit the level
  
    All levels have been beaten by me on the normal difficulty.
    
    Level 1 walkthrough/tip:
        Use the black wall as cover and lure the enemy in. Attack the enemy over the wall with your archer while the blue and brown units defend the flanks
        
    Level 2 walkthrough/tip:
        Send all the units to the south. Have the archer and blue units combo to destroy the units on the south, while the brown units take position to defend the archer from the other enemies
        
    Level 3 walkthrough/tip:
        Use your archer to pick off the enemies over the wall. Have your brown units cover up the entrance if the enemy tries to exit while the archers go to work. Do not enter until the number of enemies is small enough to engage comfortably.
        
    Level 4 walkthrough/tip:
        Send all your units to the bottom left corner. Protect your archer, and try not to initiate attacks with your melee units unless battle will result in 0 damage taken for your unit. Near the end of the battle when there are only 1-2 player units remaining, use your unit's higher movement to runaway from the enemy for the remaining turns.
        
    Level 5 walkthrough/tip: This level is unique in that the ai will stay put unless a player unit gets within a      certain range. Use this to your advantage by first destroying the small pack of enemy troops to the          left. While engaging the army to the left, be sure to continue to attack with your archer and rotate          your blue units to keep them fresh and alive. Strategy and unit health management is critical in this        level. Preserve your brown troops to take on the final boss(cyan). After defeating the army to the left,      make your way right to take on the boss alone, before moving on to destroy the army on the right.
        
        
        
        
        
        