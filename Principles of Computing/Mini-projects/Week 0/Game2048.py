"""
Clone of 2048 game.
"""

import poc_2048_gui      
import random
#import user34_cMJVLVBRqj_5

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    number = 0;
    newline = []
    for index in range(len(line)):
        if (line[index] != 0):
            if (number == 0):
                number = line[index]
                if (index == len(line)-1 and number != 0):
                    newline.append(number) 
                    number = 0
            else:
                if(number == line[index]):
                    number += line[index]
                    newline.append(number)
                    number = 0                
                else:
                    newline.append(number)
                    number = line[index]
        else:
            if (index == len(line)-1 and number != 0):
                newline.append(number)
                number = 0
                
    if (number != 0):
        newline.append(number)
    for dummy_index in range(len(line)-len(newline)):
        newline.append(0)
    return newline

def matrixes_are_equal(matrix_one, matrix_two):
    """
    Checks does two matrixes are equal/same
    """    
    for row in range(len(matrix_one)):
        for col in range(len(matrix_one[0])):
            if (matrix_one[row][col] != matrix_two[row][col]):
                return False
    return True

def clone_matrix(source):
    """
    Create a copy of an existing matrix
    """
    target = []
    for row in range(len(source)):
        line = []
        for col in range(len(source[0])):
            line.append(source[row][col])
        target.append(line)
    return target
        
class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.grid = []
        self.reset()
        self.positions = []        
        up_indexes = []
        down_indexes = []
        up_counter = -1        
        down_counter = self.grid_height
        for dummy_row in range(self.grid_height):
            up_indexes.append([up_counter + OFFSETS[UP][0], OFFSETS[UP][1]])
            up_counter += 1
            down_indexes.append([down_counter + OFFSETS[DOWN][0], OFFSETS[DOWN][1]])
            down_counter -= 1
        self.positions.append(up_indexes)
        self.positions.append(down_indexes) 
        left_indexes = []
        right_indexes = []
        left_counter = -1
        right_counter = self.grid_width
        for dummy_row in range(self.grid_width):
            left_indexes.append([OFFSETS[LEFT][0], left_counter + OFFSETS[LEFT][1]])
            left_counter += 1
            right_indexes.append([OFFSETS[RIGHT][0], right_counter + OFFSETS[RIGHT][1]])
            right_counter -= 1 
        self.positions.append(left_indexes)        
        self.positions.append(right_indexes) 
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.grid = []
        for dummy_row in range(self.grid_height):
            row_line = []
            for dummy_col in range(self.grid_width):
                row_line.append(0)
            self.grid.append(row_line)    
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        output = ""
        for row in range(self.grid_height):
            output += str(self.grid[row]) + "\n"            
        return output    

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        initial_grid = clone_matrix(self.grid)
        if (direction == LEFT or direction == RIGHT):
            new_matrix = []
            for row in range(self.grid_height):
                merged_line = []
                line_to_merge = []
                for col in range(self.grid_width):
                    y_pos = self.positions[direction-1][col][1]
                    line_to_merge.append(self.grid[row][y_pos])   
                merged_line = merge(line_to_merge)
                if(direction == RIGHT):
                    merged_line.reverse()
                new_matrix.append(merged_line)
            self.grid = new_matrix    
        else:
            for col in range(self.grid_width):
                merged_line = []
                line_to_merge = []
                for row in range(self.grid_height):
                    x_pos = self.positions[direction-1][row][0]
                    line_to_merge.append(self.grid[x_pos][col])
                merged_line = merge(line_to_merge)
                if (direction == DOWN):
                    merged_line.reverse()
                for row in range(self.grid_height):
                    self.grid[row][col] = merged_line[row]
        if (not matrixes_are_equal(initial_grid, self.grid)):
            self.new_tile()
                    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        tile_value = 2 if (random.random() < 0.9) else 4
        x_pos = 0
        y_pos = 0
        while True:
            x_pos = random.randrange( self.grid_height)
            y_pos = random.randrange( self.grid_width)
            if self.get_tile(x_pos, y_pos) == 0:
                break
        self.set_tile(x_pos, y_pos, tile_value)        
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self.grid[row][col]
 
    
poc_2048_gui.run_gui(TwentyFortyEight(3, 3))
##user34_cMJVLVBRqj_5.run_test(merge) # merge test
#my_board = TwentyFortyEight(4,5)
#my_board.grid = []
#my_board.grid.insert(0, [8, 16, 8, 16, 8])
#my_board.grid.insert(1, [16, 8, 16, 8, 16])
#my_board.grid.insert(2, [8, 16, 8, 16, 8])
#my_board.grid.insert(3, [16, 8, 16, 8, 16])
##my_board.grid.insert(0, [2,2,2,2])
##my_board.grid.insert(1, [2,0,2,2])
##my_board.grid.insert(2, [2,4,4,2])
##my_board.grid.insert(0, [0,0,2,2])
#print my_board
#my_board.move(LEFT)
#print my_board
