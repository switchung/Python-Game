
"""
Author username(s): Tristan Chung,
Date: 9/21/17
Final Project
"""

import random
import graphics
from button import *
import time

class GameBoard:
    
    def __init__(self, level):
        self.obstacles = []
        self.x1 = []
        self.x2 = []
        self.y1 = []
        self.y2 = []
        self.o_index = 0
        
        self.board = graphics.GraphWin("Game Board", 800, 800)
        self.draw_board(level)
        
         
       
    def close_board(self):
        """Function to close the board"""
        self.board.getMouse()
        self.board.close()
        
    def draw_board(self, level):
        """Draws the board dependent on level selection"""
        for y in range(40, 600, 40):
            self.line = Line(Point(0,y), Point(800,y))
            self.line.draw(self.board)

        for x in range(40, 800, 40):
            self.line = Line(Point(x, 0), Point(x, 560))
            self.line.draw(self.board)
            
        if level == 1:  #x1, y1, x2, y2
            for block in range(self.block(1), self.block(5), 40):
                self.obstacles.append(self.obstacle(block, self.block(9), block + 40, self.block(10)))
                
        elif level == 2:
            for block in range(self.block(3), self.block(10), 40):
                self.obstacles.append(self.obstacle(self.block(3), block, self.block(4), block+40))
                
        elif level == 3:
            for block in range(0, self.block(6), 40):
                self.obstacles.append(self.obstacle(block, self.block(4), block + 40, self.block(5)))
            for block in range(self.block(7), self.block(11), 40):
                self.obstacles.append(self.obstacle(block, self.block(4), block + 40, self.block(5)))
            for block in range(self.block(4), 0, -40):
                self.obstacles.append(self.obstacle(self.block(10), block, self.block(11), block+40))
            
        elif level == 4:
            for block in range(0, self. block(9), 40):
                self.obstacles.append(self.obstacle(self.block(5), block, self.block(6), block+40))
                self.obstacles.append(self.obstacle(self.block(12), block, self.block(13), block+40))
            for block in range(0, self.block(6), 40):
                self.obstacles.append(self.obstacle(block, self.block(9), block+40, self.block(10)))
            for block in range(self.block(12), self.block(20), 40):
                self.obstacles.append(self.obstacle(block, self.block(9), block+40, self.block(10)))
                
        elif level == 5:
            for block in range(0, self.block(5), 40):
                self.obstacles.append(self.obstacle(self.block(4), block, self.block(5), block + 40))
                self.obstacles.append(self.obstacle(self.block(14), block, self.block(15), block + 40))
            
    def obstacle(self, x1, y1, x2, y2):
        """Creates obstacles for the gameboard for which any unit cannot move onto"""
        self.x1.append(x1)
        self.x2.append(x2)
        self.y1.append(y1)
        self.y2.append(y2)
        
        rect = graphics.Rectangle(Point(x1, y1), Point(x2, y2))
        rect.setFill("black")
        rect.draw(self.board)
        self.o_index += 1 #keeping track of obstacle index
        
    def get_x1(self, index):
        """Returns the first x coordinate value for the obstacle"""
        return self.x1[index]

    def get_y1(self, index):
        """Returns the first y coordinate value for the obstacle"""
        return self.y1[index]
    
    def block(self, num):
        return num * 40 #40 == tile length on gameboard
        
class Pieces:
    
    def __init__(self, level):
        MELEE = 40
        RANGED = 80
        TILE = 20
        self.level = level
        self.unit = []
        self.x = []
        self.y = []
        self.health = []
        self.movement = []
        self.attack = []
        self.range = []
        self.color = []
        self.index = 0
        self.alive_count = 0

        self.ai = []
        self.aix = []
        self.aiy = []
        self.aihealth = []
        self.aimovement = []
        self.aiattack = []
        self.airange = []
        self.ai_index = 0
        self.alive_aicount = 0
        self.ai_color = []
       
        difficulty = Level()
        self.difficulty = difficulty.get_difficulty()
        
        self.grid = GameBoard(level)
        self.o_index = self.grid.o_index #obstacle index

        if level == 1:
            #initializing player units
            #x coord, y coord, color, health, attack, move, range
            self.unit.append(self.init_unit(self.tile(1), self.tile(14), "blue", 5, 3, 5, MELEE))
            self.unit.append(self.init_unit(self.tile(2), self.tile(14), "yellow", 5, 3, 5, RANGED))
            self.unit.append(self.init_unit(self.tile(4), self.tile(12), "green", 3, 2, 7, MELEE))
            self.unit.append(self.init_unit(self.tile(4), self.tile(11), "brown", 10, 3, 2, MELEE))

            #initializing ai units
            for i in range(self.tile(3), self.tile(11), 40):
                self.ai.append(self.init_ai(i, self.tile(6),"red", 5, 3, 3,MELEE))
                
        elif level == 2:
            self.unit.append(self.init_unit(self.tile(5), self.tile(4), "blue", 5, 3, 5, MELEE))
            self.unit.append(self.init_unit(self.tile(7), self.tile(10), "blue", 5, 3, 5, MELEE))
            self.unit.append(self.init_unit(self.tile(7), self.tile(6), "brown", 10, 3, 2, MELEE))
            self.unit.append(self.init_unit(self.tile(7), self.tile(7), "brown", 10, 3, 2, MELEE))
            self.unit.append(self.init_unit(self.tile(8), self.tile(8), "brown", 10, 3, 2, MELEE))
            self.unit.append(self.init_unit(self.tile(8), self.tile(9), "yellow", 5, 3, 5, RANGED))
            
            for tile in range(self.tile(5), self.tile(10), 40):
                self.ai.append(self.init_ai(tile, self.tile(3),"red", 5, 3, 3,MELEE))
              
            for tile in range(self.tile(5), self.tile(9), 40):
                self.ai.append(self.init_ai(self.tile(11), tile,"red", 5, 3, 3,MELEE))
             
            for tile in range(self.tile(5), self.tile(9), 40):
                self.ai.append(self.init_ai(tile, self.tile(12),"red", 5, 3, 3,MELEE))
            
        elif level == 3:
            self.unit.append(self.init_unit(self.tile(13), self.tile(7), "brown", 10, 3, 2, MELEE))
            self.unit.append(self.init_unit(self.tile(11), self.tile(7), "brown", 10, 3, 2, MELEE))
            self.unit.append(self.init_unit(self.tile(14), self.tile(9), "yellow", 5, 3, 5, RANGED))
            self.unit.append(self.init_unit(self.tile(14), self.tile(11), "yellow", 5, 3, 5, RANGED))
            self.unit.append(self.init_unit(self.tile(14), self.tile(12), "green", 3, 2, 7, MELEE))
                
            for tile in range(self.tile(1), self.tile(8), 40):
                self.ai.append(self.init_ai(tile, self.tile(3),"red", 5, 3, 3,MELEE))
                self.ai.append(self.init_ai(tile, self.tile(2),"red", 5, 3, 3,MELEE))
            
        elif level == 4:
            self.unit.append(self.init_unit(self.tile(2), self.tile(12), "brown", 10, 3, 2, MELEE))
            self.unit.append(self.init_unit(self.tile(9), self.tile(12), "brown", 10, 3, 2, MELEE))
            self.unit.append(self.init_unit(self.tile(6), self.tile(13), "blue", 5, 3, 5, MELEE))
            self.unit.append(self.init_unit(self.tile(4), self.tile(14), "yellow", 5, 3, 5, RANGED))
            self.unit.append(self.init_unit(self.tile(19), self.tile(14), "green", 3, 2, 7, MELEE))
            self.unit.append(self.init_unit(self.tile(6), self.tile(14), "blue", 5, 3, 5, MELEE))
            self.unit.append(self.init_unit(self.tile(8), self.tile(13), "blue", 5, 3, 5, MELEE))
 
            for tile in range(self.tile(2), self.tile(7), 40):
                self.ai.append(self.init_ai(self.tile(9), tile,"red", 5, 3, 3,MELEE))
                self.ai.append(self.init_ai(self.tile(10), tile,"red", 5, 3, 3,MELEE))
            self.ai.append(self.init_ai(self.tile(7), self.tile(7),"black", 13, 4, 3,MELEE))
            self.ai.append(self.init_ai(self.tile(10), self.tile(7),"black", 13, 4, 3,MELEE))
            self.ai.append(self.init_ai(self.tile(20), self.tile(12),"black", 13, 4, 3,MELEE))
            self.ai.append(self.init_ai(self.tile(20), self.tile(13),"black", 13, 4, 3,MELEE))
            self.ai.append(self.init_ai(self.tile(19), self.tile(11),"black", 13, 4, 3,MELEE))
            
        elif level == 5:
            self.unit.append(self.init_unit(self.tile(2), self.tile(12), "brown", 10, 3, 2, MELEE))
            self.unit.append(self.init_unit(self.tile(9), self.tile(12), "brown", 10, 3, 2, MELEE))
            self.unit.append(self.init_unit(self.tile(6), self.tile(13), "blue", 5, 3, 5, MELEE))
            self.unit.append(self.init_unit(self.tile(4), self.tile(14), "yellow", 5, 3, 5, RANGED))
            self.unit.append(self.init_unit(self.tile(19), self.tile(14), "green", 3, 2, 7, MELEE))
            self.unit.append(self.init_unit(self.tile(6), self.tile(14), "blue", 5, 3, 5, MELEE))
            self.unit.append(self.init_unit(self.tile(8), self.tile(13), "blue", 5, 3, 5, MELEE))
            self.unit.append(self.init_unit(self.tile(8), self.tile(14), "blue", 5, 3, 5, MELEE))
            #self.unit.append(self.init_unit(self.tile(9), self.tile(13), "yellow", 5, 3, 5, RANGED))
            #self.unit.append(self.init_unit(self.tile(7), self.tile(13), "yellow", 5, 3, 5, RANGED))
            self.unit.append(self.init_unit(self.tile(16), self.tile(14), "green", 3, 2, 7, MELEE))
            self.unit.append(self.init_unit(self.tile(13), self.tile(14), "green", 3, 2, 7, MELEE))
            
            self.ai.append(self.init_ai(self.tile(10), self.tile(1),"cyan", 17, 5, 3, MELEE))
            
            for tile in range(self.tile(1), self.tile(4), 40):
                self.ai.append(self.init_ai(self.tile(2), tile,"red", 5, 3, 3,MELEE))
                self.ai.append(self.init_ai(self.tile(18), tile,"red", 5, 3, 3,MELEE))
                self.ai.append(self.init_ai(self.tile(1), tile,"red", 5, 3, 3,MELEE))
                self.ai.append(self.init_ai(self.tile(19), tile,"red", 5, 3, 3,MELEE))
            self.ai.append(self.init_ai(self.tile(2), self.tile(5),"black", 13, 4, 3,MELEE))
            self.ai.append(self.init_ai(self.tile(18), self.tile(5),"black", 13, 4, 3,MELEE))

        for i in range(self.index):  #drawing all the player units
            self.unit[i].draw(self.grid.board)

        for i in range(self.ai_index):  #drawing all the ai units
            self.ai[i].draw(self.grid.board)
   
        if self.difficulty == 0: #subtracting 1 attack from all enemy units to make game easy 
            for i in range(self.ai_index):
                self.aiattack[i] -= 1
                
    def tile(self, tile_num):
        return (tile_num * 40) - 20
        
    def play(self):
        '''This is the method that plays the game'''
        win = Button(Rectangle(Point(300,300),Point(500,500)),Text(Point(0,0), "You Win!"), 'white')
        lose = Button(Rectangle(Point(300,300),Point(500,500)),Text(Point(0,0), "You Lose!"), 'red')
        turn_counter = 0
        
        while self.alive_count > 0 and self.alive_aicount > 0:
            self.get_unit()
            turn_counter += 1

            if self.level == 4 and turn_counter == 10: #checking the unique win condition for level 4
                self.alive_aicount = 0
            
        if self.alive_aicount == 0: #displays message when level is won/lost
            win.draw(self.grid.board)
        else:
            lose.draw(self.grid.board)
        time.sleep(2)
        self.grid.board.close()
        
    def get_unit(self):
        """Selects unit and manages turns"""
        self.counter = self.alive_count
        self.aicounter = self.alive_aicount
        mcpy = [] #copying movement as to keep original movement values
        aimcpy = []
        self.end = self.end_button() #end turn button
        self.ai_stats = [Text(Point(0,0), ""),Text(Point(0,0), ""),Text(Point(0,0), ""),Text(Point(0,0), ""), Text(Point(0,0), ""), Text(Point(0,0), ""), Text(Point(0,0), ""), Text(Point(0,0), "")]
        
        for index in range(self.index): #making copies of movement
            mcpy.append(self.movement[index])
            
        for index in range(self.ai_index):
            aimcpy.append(self.aimovement[index])
        
         #for loop to ensure that units revert back to normal colors at the beginning of turns
        for i in range(self.index):
            if self.is_dead(i) == False:
                self.unit[i].delete()
                self.unit[i] = self.make_unit(self.x[i], self.y[i], self.color[i])
                self.unit[i].draw(self.grid.board)
                 
        self.end.draw(self.grid.board)
        self.hide_ai_stats() #making sure ai_stats are undrawn
        
        while self.counter > 0:  #While it is still player turn
            click = self.grid.board.getMouse()
            self.hide_ai_stats()
            for i in range(self.ai_index): 
                if self.ai[i].wasClicked(click): #if enemy is clicked on during players turn, show ai stats
                    self.show_ai_stats(i, 600, '',0)
            
            for index in range(self.index):
                if self.movement[index] != 0:
                    check_end = self.end_turn(click)
                    if check_end == 'e':
                        self.counter = 0
                        self.end.delete()
                        for i in range(self.index): #if player chooses to end turn, grey out player units
                            self.unit[i].delete()
                            self.unit[i] = self.make_unit(self.x[i], self.y[i], "grey")
                            self.unit[i].draw(self.grid.board)
                        break
                    else:
                        self.end.delete()
                    
                    if self.is_dead(index) == False: #if the unit is alive and was clicked, move it
                        self.move(index, click)
                        
            #necessary to reinit due to unknown bug where text goes missing
            self.end = self.end_button()
            self.end.draw(self.grid.board)
                    
            if self.counter <= 0:
                self.aicounter = self.alive_aicount
                
        self.hide_ai_stats()
        self.end.delete() # deleting end turn button for ai turn
        
        self.surround = 0 #surround to keep track of failed movements to see if unit is surrounded
        while self.aicounter > 0: #while it is still ai turn
            for index in range(self.ai_index):
                if self.aimovement[index] != 0:
                        self.aimove(index)
                
            if self.counter <= 0:
                self.counter = self.alive_count
        
        for index in range(self.index): #restores originaal movement values for the next turn
            self.movement[index] = mcpy[index]
        
        for index in range(self.ai_index):
            self.aimovement[index] = aimcpy[index]
            
    def init_unit(self, x, y, color, health, attack, movement, ran):
        """Initializes unit statistics
        Parameters:
            x, x coordinate value of Button
            y, y coordinate value
            ran, range of the unit
        """
        self.x.append(x)
        self.y.append(y)
        self.health.append(health)
        self.attack.append(attack)
        self.movement.append(movement)
        self.range.append(ran)
        self.color.append(color)
        self.index+=1
        self.alive_count += 1
        
        return Button(Circle(Point(x, y), 10), Text(Point(0,0), ""),color)
    
    def init_ai(self, x, y, color, health, attack, movement, ran):
        """Initializes ai statistics
        """
        self.aix.append(x)
        self.aiy.append(y)
        self.aihealth.append(health)
        self.aiattack.append(attack)
        self.aimovement.append(movement)
        self.airange.append(ran)
        self.ai_color.append(color)
        self.ai_index+=1
        self.alive_aicount+=1
        
        return Button(Circle(Point(x, y), 10), Text(Point(0,0), ""),color)
                
    def make_unit(self, x, y, color):
        """Creates the button"""
        return Button(Circle(Point(x, y), 10), Text(Point(0,0), ""),color)
    
    def move(self, index, click):
        """Moves the unit that was clicked on
        Parameters, 
            index, the specific index of the unit clicked on
        """
        self.end.delete()

        if self.unit[index].wasClicked(click):
            self.show_unit_stats(index)
            self.attack_command(index, self.range[index]) #checks to see if there is an enemy to attack before movement
            text = Text(Point(60, 580), "Press key w \n to have unit wait")
           
            while(self.movement[index] > 0):
                 interval = 40
                 interval2 = 40
                 text.draw(self.grid.board)
                 key = self.grid.board.getKey()
                
                 if self.is_there(key, index) == True:
                     interval = 1000  #reinitialized so movement is not possible if anything is there 
                     interval2 = -100
                     self.movement[index] += 1
                     #return 0
                 
                 elif self.y[index] > interval and key == "Up":
                     self.y[index]-=40
                 elif self.y[index] < interval2 * 13 + 20 and key == "Down":
                     self.y[index]+=40
                 elif self.x[index] > interval and key == "Left":
                     self.x[index]-=40
                 elif self.x[index] < interval2 + 720 and key == "Right":
                     self.x[index]+=40
                 elif key == 'w':
                     self.shp.undraw() #shp == showing the statistics
                     text.undraw()
                     return 0
            
                 else:
                     self.movement[index] += 1
                 
                 self.movement[index] -= 1
                 self.unit[index].delete()
                 self.unit[index] = self.make_unit(self.x[index], self.y[index], self.color[index])
                 self.unit[index].draw(self.grid.board)
                 text.undraw()
                 self.attack_command(index, self.range[index])
                 
            self.counter -= 1
            self.shp.undraw()
            self.unit[index].delete()
            self.unit[index] = self.make_unit(self.x[index], self.y[index], "grey")
            self.unit[index].draw(self.grid.board)
            return 0
            
    def aimove(self, index):
        """Same function as above, but instead for player units it is for ai units
        and randomizes movement
        """
        x_bound1 = False
        x_bound2 = False
        y_bound1 = False
        y_bound2 = False
        x_range = False
        y_range = False
        
        self.ai_attack_command(index)
        while(self.aimovement[index] > 0):
             #ai weighted movements
             if self.surround > 500: #checks to see if ai is surrounded by other ai
                self.aimovement[index] = 0
                self.aicounter -= 1
                return 0
            
             if self.level == 1 or self.level == 2: #setting defualt ai weights for levels
                 up = 1
                 down = 2
                 left = 1
                 right = 1
             elif self.level == 3:
                 up = 1
                 down = 1
                 left = 1
                 right = 1
             elif self.level == 4:
                 up = 1
                 down = 4
                 left = 3
                 right = 1
             else:
                 up = 0
                 down = 0
                 left = 0
                 right = 0 
             
             ai_weight = ["Up"]*up + ["Down"]*down + ["Left"]*left + ["Right"]*right
             
             
             for i in range(self.index): #attempting to weight the movement based on player unit location
                 x_bound1 = False
                 x_bound2 = False
                 y_bound1 = False
                 y_bound2 = False
                 x_range = False
                 y_range = False
                 
                 #checking to see if unit is within either x range(left, or right), or either y range(up or down)
                 if self.aix[index] + 200 >= self.x[i] and self.x[i] >= self.aix[index]:
                     x_bound1 = True
                     
                 if self.aix[index] - 200 <= self.x[i] and self.x[i] <= self.aix[index]:
                     x_bound2 = True
                     
                 if self.aiy[index] - 200 <= self.y[i] and self.y[i] <= self.aiy[index]:
                     y_bound1 = True
                     
                 if self.aiy[index] + 200 >= self.y[i] and self.y[i] >= self.aiy[index]:
                     y_bound2 = True
                 
                 if x_bound1 == True or x_bound2 == True:
                     x_range = True
            
                 if y_bound1 == True or y_bound2 == True:
                     y_range = True

                 if self.is_dead(i) == False and self.aiy[index] + 200 >= self.y[i] and self.y[i] >= self.aiy[index] and x_range == True:
                     down += 3
                    
                 if self.is_dead(i) == False and self.aiy[index] - 200 <= self.y[i] and self.y[i] <= self.aiy[index] and x_range == True:
                     up += 3
                     
                 if self.is_dead(i) == False and self.aix[index] + 200 >= self.x[i] and self.x[i] >= self.aix[index] and y_range == True:
                     right += 3
                 
                 if self.is_dead(i) == False and self.aix[index] - 200 <= self.x[i] and self.x[i] <= self.aix[index] and y_range == True:
                     left += 3
                     
                 #if no unit is near, then stay put and end turn (if level 5)
                 if left < 3 and right < 3 and up < 3 and down < 3 and self.level == 5 and i == self.index - 1:
                     self.aimovement[index] = 0
                     self.aicounter-=1
                     return 0
                        
             ai_weight = ["Up"]*up + ["Down"]*down + ["Left"]*left + ["Right"]*right 

             key = random.choice(ai_weight)
             if self.ai_is_there(key, index):
                 self.surround += 1
                 return 0

             if self.aiy[index] > 40 and key == "Up":
                 self.aiy[index]-=40
             elif self.aiy[index] < 540 and key == "Down":
                 self.aiy[index]+=40
             elif self.aix[index] > 40 and key == "Left":
                 self.aix[index]-=40
             elif self.aix[index] < 780 and key == "Right":
                 self.aix[index]+=40
             else:
                 self.aimovement[index] += 1

             time.sleep(.3)
             self.aimovement[index] -= 1
             self.ai[index].delete()
             self.ai[index] = self.make_unit(self.aix[index], self.aiy[index], self.ai_color[index])

             if self.is_ai_dead(index) == False:
                 self.ai[index].draw(self.grid.board)
             self.ai_attack_command(index)
        self.aicounter -= 1
        
    def is_there(self, key, ind):
        """Checking to see if the player unit is trying to move either to 
        a slot occupied by another player unit, another ai unit, or an obstacle
        
        Parameters:
            key, keyboard input of user
            ind, index of specific currently active unit"""
        for i in range(self.index): #checking to see if player unit is next to active player unit
            if key == 'Right' and self.x[ind]+40 == self.x[i] and self.y[ind] == self.y[i]:
                return True
            elif key == 'Left' and self.x[ind]-40 == self.x[i] and self.y[ind] == self.y[i]:
                return True
            elif key == 'Up' and self.y[ind]-40 == self.y[i] and self.x[ind] == self.x[i]:
                return True
            elif key == 'Down' and self.y[ind]+40 == self.y[i] and self.x[ind] == self.x[i]:
                return True
            
        for i in range(self.ai_index): #checking to see if ai unit is next to active player unit
            if key == 'Right' and self.x[ind]+40 == self.aix[i] and self.y[ind] == self.aiy[i]:
                return True
            elif key == 'Left' and self.x[ind]-40 == self.aix[i] and self.y[ind] == self.aiy[i]:
                return True
            elif key == 'Up' and self.y[ind]-40 == self.aiy[i] and self.x[ind] == self.aix[i]:
                return True
            elif key == 'Down' and self.y[ind]+40 == self.aiy[i] and self.x[ind] == self.aix[i]:
                return True
        
        for i in range(self.o_index): #checking to see if obstacle is next to active player unit
            ox = self.grid.get_x1(i)
            oy = self.grid.get_y1(i)
            
            if key == 'Right' and self.x[ind]+20 == ox and self.y[ind]-20 == oy:
                return True
            elif key == 'Left' and self.x[ind]-60 == ox and self.y[ind]-20 == oy:
                return True
            elif key == 'Up' and self.y[ind]-60 == oy and self.x[ind]-20 == ox:
                return True
            elif key == 'Down' and self.y[ind]+20 == oy and self.x[ind]-20 == ox:
                return True
        return False
          
            
    def ai_is_there(self, key, ind):
        """Same function as above but for ai"""
        for i in range(self.ai_index):
            if key == 'Right' and self.aix[ind]+40 == self.aix[i] and self.aiy[ind] == self.aiy[i]:
                return True
            elif key == 'Left' and self.aix[ind]-40 == self.aix[i] and self.aiy[ind] == self.aiy[i]:
                return True
            elif key == 'Up' and self.aiy[ind]-40 == self.aiy[i] and self.aix[ind] == self.aix[i]:
                return True
            elif key == 'Down' and self.aiy[ind]+40 == self.aiy[i] and self.aix[ind] == self.aix[i]:
                return True
        
        for i in range(self.o_index):
            ox = self.grid.get_x1(i)
            oy = self.grid.get_y1(i)
            if key == 'Right' and self.aix[ind]+20 == ox and self.aiy[ind]-20 == oy:
                return True
            elif key == 'Left' and self.aix[ind]-60 == ox and self.aiy[ind]-20 == oy:
                return True
            elif key == 'Up' and self.aiy[ind]-60 == oy and self.aix[ind]-20 == ox:
                return True
            elif key == 'Down' and self.aiy[ind]+20 == oy and self.aix[ind]-20 == ox:
                return True
        
        for i in range(self.index):
            if key == 'Right' and self.aix[ind]+40 == self.x[i] and self.aiy[ind] == self.y[i]:
                return True
            elif key == 'Left' and self.aix[ind]-40 == self.x[i] and self.aiy[ind] == self.y[i]:
                return True
            elif key == 'Up' and self.aiy[ind]-40 == self.y[i] and self.aix[ind] == self.x[i]:
                return True
            elif key == 'Down' and self.aiy[ind]+40 == self.y[i] and self.aix[ind] == self.x[i]:
                return True
        return False
    
    def attack_command(self, ind, a_range):
        """Prompts user to attack whenever an enemy is in range
        Parameters,
            ind, specific index of active unit
            a_range, attack range of active unit
        """
        self.attack_bu = Button(Rectangle(Point(60,600), Point(150, 650)) ,Text(Point(0,0), "Attack Up \n (Click)"), 'white')
        self.attack_bd = Button(Rectangle(Point(60,650), Point(150, 700)) ,Text(Point(0,0), "Attack Down \n (Click)"), 'white')
        self.attack_bl = Button(Rectangle(Point(60,700), Point(150, 750)) ,Text(Point(0,0), "Attack Left \n (Click)"), 'white')
        self.attack_br = Button(Rectangle(Point(60,750), Point(150, 800)) ,Text(Point(0,0), "Attack Right \n (Click)"), 'white')
        
        self.attack_tr = Button(Rectangle(Point(150,600), Point(250, 650)) ,Text(Point(0,0), "Attack TR Cnr \n (Click)"), 'white')
        self.attack_tl = Button(Rectangle(Point(150,650), Point(250, 700)) ,Text(Point(0,0), "Attack TL Cnr \n (Click)"), 'white')
        self.attack_bcr = Button(Rectangle(Point(150,700), Point(250, 750)) ,Text(Point(0,0), "Attack BR Cnr \n (Click)"), 'white')
        self.attack_bcl = Button(Rectangle(Point(150,750), Point(250, 800)) ,Text(Point(0,0), "Attack BL Cnr \n (Click)"), 'white')
        
        self.wait = Button(Rectangle(Point(0,730), Point(60, 790)) ,Text(Point(0,0), "No Attack \n (Click)"), 'white')
        count = 0
        ai_num = [0,0,0,0,0,0,0,0]
        is_drawn = [0,0,0,0,0,0,0,0]
        
        for i in range(self.ai_index):
            
            if self.x[ind]+a_range == self.aix[i] and self.y[ind] == self.aiy[i] and self.is_dead(ind) == False:
                self.attack_br.draw(self.grid.board)
                ai_num[0] = i
                is_drawn[0] = True
                count += 1
                self.show_ai_stats(i, 600, "Right", 0)

            if self.x[ind]-a_range == self.aix[i] and self.y[ind] == self.aiy[i] and self.is_dead(ind) == False:
                self.attack_bl.draw(self.grid.board)
                ai_num[1] = i
                count += 1
                is_drawn[1] = True
                self.show_ai_stats(i, 650, "Left", 1)
                
            
            if self.y[ind]-a_range == self.aiy[i] and self.x[ind] == self.aix[i] and self.is_dead(ind) == False:
                self.attack_bu.draw(self.grid.board)
                ai_num[2] = i
                count += 1
                is_drawn[2] = True
                self.show_ai_stats(i, 700, "Up", 2)
                
                
            if self.y[ind]+a_range == self.aiy[i] and self.x[ind] == self.aix[i] and self.is_dead(ind) == False:
                self.attack_bd.draw(self.grid.board)
                ai_num[3] = i
                count += 1  
                is_drawn[3] = True
                self.show_ai_stats(i, 750, "Down", 3)
            
            if self.x[ind]+a_range/2 == self.aix[i] and self.y[ind]+a_range/2 == self.aiy[i] and self.is_dead(ind) == False:
                self.attack_bcr.draw(self.grid.board)
                ai_num[4] = i
                count += 1
                is_drawn[4] = True
                self.show_ai_stats(i, 600, "BR CNR", 4)
                
            if self.x[ind]-a_range/2 == self.aix[i] and self.y[ind]-a_range/2 == self.aiy[i] and self.is_dead(ind) == False:
                self.attack_tl.draw(self.grid.board)
                ai_num[5] = i
                count += 1
                is_drawn[5] = True
                self.show_ai_stats(i, 650, "Top L", 5)
            
            if self.y[ind]-a_range/2 == self.aiy[i] and self.x[ind]+a_range/2 == self.aix[i] and self.is_dead(ind) == False:
                self.attack_tr.draw(self.grid.board)
                ai_num[6] = i
                count += 1
                is_drawn[6] = True
                self.show_ai_stats(i, 700, "Top R", 6)
                
                
            if self.y[ind]+a_range/2 == self.aiy[i] and self.x[ind]-a_range/2 == self.aix[i] and self.is_dead(ind) == False:
                self.attack_bcl.draw(self.grid.board)
                ai_num[7] = i
                count += 1      
                is_drawn[7] = True
                self.show_ai_stats(i, 750, "BL CNR", 7)
        if count == 0: #if there are no options to attack, exit
            return 0
        
        else:
            self.wait = Button(Rectangle(Point(0,730), Point(60, 790)) ,Text(Point(0,0), "No Attack \n (Click)"), 'white')
            self.wait.draw(self.grid.board)
            while True:
                click = self.grid.board.getMouse()
            
                if self.attack_br.wasClicked(click) and is_drawn[0] == True:
                    self.attack_process(ind, ai_num[0])
                    break
                elif self.attack_bl.wasClicked(click) and is_drawn[1] == True:
                    self.attack_process(ind, ai_num[1])
                    break
                    
                elif self.attack_bu.wasClicked(click) and is_drawn[2] == True:
                    self.attack_process(ind, ai_num[2])
                    break
                    
                elif self.attack_bd.wasClicked(click) and is_drawn[3] == True:
                    self.attack_process(ind, ai_num[3])
                    break
                if self.attack_bcr.wasClicked(click) and is_drawn[4] == True:
                    self.attack_process(ind, ai_num[4])
                    break
                
                elif self.attack_tl.wasClicked(click) and is_drawn[5] == True:
                    self.attack_process(ind, ai_num[5])
                    break
                elif self.attack_tr.wasClicked(click) and is_drawn[6] == True:
                    self.attack_process(ind, ai_num[6])
                    break
                    
                elif self.attack_bcl.wasClicked(click) and is_drawn[7] == True:
                    self.attack_process(ind, ai_num[7])
                    break
                    
                elif self.wait.wasClicked(click):
                    self.attack_bu.delete()
                    self.attack_bl.delete()
                    self.attack_br.delete()
                    self.attack_bd.delete()
                    self.attack_tl.delete()
                    self.attack_tr.delete()
                    self.attack_bcr.delete()
                    self.attack_bcl.delete()
                    self.wait.delete()
                    self.hide_ai_stats()
                    return 0
                
                
            self.attack_bu.delete()
            self.attack_bl.delete()
            self.attack_br.delete()
            self.attack_bd.delete()
            self.attack_tl.delete()
            self.attack_tr.delete()
            self.attack_bcr.delete()
            self.attack_bcl.delete()
            self.wait.delete()
            self.shp.undraw()
            self.hide_ai_stats()
            return 0
           
                
    def attack_process(self, ind, ai_num):
        """Shows battle info while battle is in progress
        Parameters:
            ind, specific index of active attacking unit
            ai_num, specific index of the ai in range to be attacked
        """
        self.show_player_info(ind, ai_num)
        time.sleep(2)
        self.change_health(ind, ai_num)
        self.hide_info()
        self.show_player_info(ind, ai_num)
        time.sleep(1)
        self.movement[ind] = 0
        self.hide_info()
        
    def ai_process(self, ind, unit_num):
        """Same as above function, but altered slightly for ai use
        """
        self.show_player_info(unit_num, ind)
        time.sleep(2)
        self.hide_info()
        self.change_aihealth(ind, unit_num)
        self.show_player_info(unit_num, ind)
        time.sleep(1)
        self.aimovement[ind] = 0
        self.hide_info()
        
    def ai_attack_command(self, ind):
        """Purpose is to have ai attack player unit as soon as player unit
        is in attack range"""
        rand_attack = []
        count = 0
        unit_num = 0
        
        for i in range(self.index):
            
            if self.aix[ind]+40 == self.x[i] and self.aiy[ind] == self.y[i] and self.is_ai_dead(ind) == False:
                rand_attack.append("Attack R")
                unit_num = i
                count += 1
                break
             
            if self.aix[ind]-40 == self.x[i] and self.aiy[ind] == self.y[i] and self.is_ai_dead(ind) == False:
                rand_attack.append("Attack L")
                unit_num = i
                count += 1
                break
                
            if self.aiy[ind]-40 == self.y[i] and self.aix[ind] == self.x[i] and self.is_ai_dead(ind) == False:
                rand_attack.append("Attack D")
                unit_num = i
                count += 1
                break
                
            if self.aiy[ind]+40 == self.y[i] and self.aix[ind] == self.x[i] and self.is_ai_dead(ind) == False:
                rand_attack.append("Attack U")
                unit_num = i
                count += 1
                break
            
        if count == 0:
            return 0
        
        else:
            choice = random.choice(rand_attack)
            if choice == "Attack R":
                self.ai_process(ind, unit_num)
            
            elif choice == "Attack L":
                self.ai_process(ind, unit_num)
                
            elif choice == "Attack D":
                self.ai_process(ind, unit_num)
                
            elif choice == "Attack U":
                self.ai_process(ind, unit_num)
        
     
    def change_health(self, index, i):
        """Changes health when attacked from the player unit perspective
        Parameters:
            index: attacking player unit's index
            i: index of ai unit getting attacked
        """
        self.aihealth[i] -= self.attack[index]
        
        if self.is_ai_dead(i) == False and self.airange[i] == self.range[index]:
            self.health[index] -= self.aiattack[i]
            
        if self.is_ai_dead(i) == True:
            self.alive_aicount -= 1
            
        if self.is_dead(index) == True:
            self.alive_count -= 1

    def change_aihealth(self, index, i):
        """Same as above except from the perspective of the ai unit
        """
        self.health[i] -= self.aiattack[index]
        
        if self.is_dead(i) == False and self.range[i] == self.airange[index]:
            self.aihealth[index] -= self.attack[i]
            
        if self.is_dead(i) == True:
            self.alive_count -= 1
            
        if self.is_ai_dead(index) == True:
            self.alive_aicount -= 1

    def is_dead(self, index):
        """Checks to see in the player unit is dead or alive"""
        if self.health[index] <= 0:
            self.unit[index].delete()
            self.x[index] = -100
            self.y[index] = -100
            self.health[index] = 0 #ensures that alive_count doesnt get subtracted every time a dead unit is indexed over
            return True
        else:
            return False
        
    def is_ai_dead(self, index):
        """Checks to see if the ai unit is dead or alive"""
        if self.aihealth[index] <= 0:
            self.ai[index].delete()
            self.aix[index] = -100
            self.aiy[index] = -100
            self.aihealth[index] = 0
            return True
        else:
            return False

    def show_unit_stats(self, index):
        """Shows stats of player unit when clicked on on player's turn"""
        self.shp = Text(Point(700, 650), ("Health: " + str(self.health[index]) + "\nAttack: " + str(self.attack[index]) + "\nMvt: " + str(self.movement[index]) + "\nRange: " + str(self.range[index]//40)))
        self.shp.draw(self.grid.board)
        
    def show_ai_stats(self, index, y, direction, num):
        """Shows stats of ai unit when player has option of attack it"""
        if self.is_ai_dead(index) == False:
            if num <= 3:
                self.ai_stats[num] = (Text(Point(630, y), (direction + " Health: " + str(self.aihealth[index]) + "\nAttack: " + str(self.aiattack[index]) + "\nMvt: " + str(self.aimovement[index]))))
                self.ai_stats[num].setFill("red")
                self.ai_stats[num].draw(self.grid.board)
            else:
                self.ai_stats[num] = (Text(Point(550, y), (direction + " Health: " + str(self.aihealth[index]) + "\nAttack: " + str(self.aiattack[index]) + "\nMvt: " + str(self.aimovement[index]))))
                self.ai_stats[num].setFill("red")
                self.ai_stats[num].draw(self.grid.board)
    
    def show_player_info(self, index, i):
        """Shows the attack, health of player unit and ai"""
        player_text = Text(Point(0,0),"Player Unit \n Health: ")
        ai_text = Text(Point(0,0),"CPU Unit \n Health: ")
    
        self.hype = Text(Point(405, 570), "Attack in Progress!")
        self.txt = Text(Point(360, 600), ("Player Unit \n Health: " + str(self.health[index])))
        self.txt2 = Text(Point(450, 600), ("CPU Unit \n Health: " + str(self.aihealth[i])))
        
        self.txt.setTextColor(self.color[index])
        self.txt2.setTextColor(self.ai_color[i])

        self.txt.draw(self.grid.board)
        self.txt2.draw(self.grid.board)
        self.hype.draw(self.grid.board)
        
    def hide_info(self):
        """hides the attack and health of ai and player units"""
        self.txt.undraw()
        self.txt2.undraw()
        self.hype.undraw()
        
    def hide_ai_stats(self):
        """Hides stats of ai from screen"""
        self.ai_stats[0].undraw()
        self.ai_stats[1].undraw()
        self.ai_stats[2].undraw()
        self.ai_stats[3].undraw()
        self.ai_stats[4].undraw()
        self.ai_stats[5].undraw()
        self.ai_stats[6].undraw()
        self.ai_stats[7].undraw()
        
    def end_turn(self, click):
        """Checks to see if the end turn button was clicked"""
        if self.end.wasClicked(click):
            return 'e'
        else:
            return False
        
    def end_button(self):
        """Necessary for some bug where redrawing button without 
        reinitializing does not redraw the text"""
        return Button(Rectangle(Point(700, 700), Point(800, 750)),Text(Point(0,0), "Click to \n end turn"), "white")
    
        
class Level():
    
    def __init__(self):
        self.easy = Button(Rectangle(Point(0, 0), Point(200, 100)),Text(Point(0,0), "Easy"), "white")
        self.normal = Button(Rectangle(Point(0, 100), Point(200, 200)), Text(Point(0,0), "Normal"), "white")
        self.difficulty = 1
        
        self.lvl1 = Button(Rectangle(Point(100, 50), Point(300, 150)),Text(Point(0,0), "Level 1"), "white")
        self.lvl2 = Button(Rectangle(Point(100, 150), Point(300, 250)), Text(Point(0,0), "Level 2"), "white")
        self.lvl3 = Button(Rectangle(Point(100, 250), Point(300, 350)),Text(Point(0,0), "Level 3"), "white")
        self.lvl4 = Button(Rectangle(Point(100, 350), Point(300, 450)),Text(Point(0,0), "Level 4"), "white")
        self.lvl5 = Button(Rectangle(Point(100, 450), Point(300, 550)),Text(Point(0,0), "BOSS LEVEL"), "red")
        self.done = Button(Rectangle(Point(300, 450), Point(500, 550)),Text(Point(0,0), "Quit"), "white")
        self.level = -1
        
        self.lvl4_extra_info = Button(Rectangle(Point(300, 350), Point(500, 450)),Text(Point(0,0), "Survive for at least 10 turns \n to win level 4!"), "orange")
    
    def get_difficulty(self):
        """Creates a menu screen for the user to select a difficulty"""
        self.win = graphics.GraphWin("Difficulty Select Menu", 200, 200)
        self.easy.draw(self.win)
        self.normal.draw(self.win)
        
        while True:
            click = self.win.getMouse()
            if self.easy.wasClicked(click):
                self.difficulty = 0
                self.win.close()
                return self.difficulty
            
            elif self.normal.wasClicked(click):
                self.difficulty = 1
                self.win.close()
                return self.difficulty
        
    def get_level(self):
        """Creates a menu screen for the user to select a level"""
        self.menu = graphics.GraphWin("Level Select Menu", 500, 550)
        self.lvl1.draw(self.menu)
        self.lvl2.draw(self.menu)
        self.lvl3.draw(self.menu)
        self.lvl4.draw(self.menu)
        self.lvl5.draw(self.menu)
        self.done.draw(self.menu)
        self.lvl4_extra_info.draw(self.menu)
        
        while True:
            click = self.menu.getMouse()
            if self.lvl1.wasClicked(click):
                self.level = 1
                self.menu.close()
                return self.level
                
            elif self.lvl2.wasClicked(click):
                self.level = 2
                self.menu.close()
                return self.level
        
            elif self.lvl3.wasClicked(click):
                self.level = 3
                self.menu.close()
                return self.level
    
            elif self.lvl4.wasClicked(click):
                self.level = 4
                self.menu.close()
                return self.level
             
            elif self.lvl5.wasClicked(click):
                self.level = 5
                self.menu.close()
                return self.level

            elif self.done.wasClicked(click):
                self.level = 0
                self.menu.close()
        return self.level
            
def main():
    lvl = 1
    while lvl > 0:
        level_select = Level()
        lvl = level_select.get_level()
        if lvl > 0:
            game = Pieces(lvl)
            game.play()
  
if __name__ == '__main__':
    main()



