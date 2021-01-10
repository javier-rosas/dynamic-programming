# CS4102 Spring 2020 -- Homework 5
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 4 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: jr2dj
# Collaborators: None
# Sources: Introduction to Algorithms, Cormen
#################################
class RollerCoaster:
    def __init__(self):
        return

    # This method is the one you should implement.  It will be called to find the
    # the roller coaster's path.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the length of the longest drop of the coaster
    def run(self, terrain):
        size = len(terrain)
        self.terrain = terrain
        self.terrain_size = size
        self.start = None
        
        self.result = 1

        # Initialize memory of 2d array with exact dimensions as terrain. All entries are initially -10. 
        temp_terrain =[[-10 for i in range(size)]for i in range(size) ] 
        
        # Compute longest path beginning from all cells  
        self.stop_cell = (0, 0)
        
        for i in range(size): 
            for j in range(size): 
                if (temp_terrain[i][j] == -10): 
                    self.length(i, j, temp_terrain) 
                    
                # Update result if needed  
                if temp_terrain[i][j] > self.result:
                    self.result = temp_terrain[i][j]
                    self.stop_cell = (i, j)
                #self.result = max(self.result, dp[i][j])
        
        self.temp_terrain = temp_terrain
        return self.result 
    
    
    # @returns the max length from a cell 
    def length(self, i, j, temp_terrain):
        terrain = self.terrain
        size = self.terrain_size
        # In case we go out of bounds / base case
        if (i<0 or i>= size or j<0 or j>= size): 
            return 0
    
        # If the result is already in memory, return the result
        if (temp_terrain[i][j] != -10):  
            return temp_terrain[i][j] 
    
        # To store the path lengths in all the four directions 
        right = -10
        up = -10
        down = -10 
        left = -10
    
        # if the right direction is smaller than the current position 
        if (j<size-1 and (terrain[i][j] < terrain[i][j + 1])): 
            right = 1 + self.length(i, j + 1, temp_terrain) 
    
        # if the left direction is smaller than the current position 
        if (j>0 and (terrain[i][j] < terrain[i][j-1])):  
            left = 1 + self.length(i, j-1, temp_terrain) 
    
        # if the down direction is smaller than the current position 
        if (i>0 and (terrain[i][j] < terrain[i-1][j])): 
            down = 1 + self.length(i-1, j, temp_terrain) 
            
        # if the up direction is smaller than the current position 
        if (i<size-1 and (terrain[i][j] < terrain[i + 1][j])): 
            up = 1 + self.length(i + 1, j, temp_terrain) 
    
        
        # Pick the biggest decrease in the four directions
        max_down = max(down, 1)
        max_up_down = max(max_down, up)
        max_up_down_left = max(max_up_down, left)
        max_up_down_left_right = max(max_up_down_left, right)
        temp_terrain[i][j] = max_up_down_left_right
        
        return temp_terrain[i][j]
    
    

    # Get the terrain values in the coaster's main drop path, in order from highest to lowest elevation
    #
    # @return the ordered list of terrain values in the coaster's main drop
    def getCoasterPath(self):
        i, j = self.stop_cell
        temp_terrain = self.temp_terrain
        size = self.terrain_size
        
        paths = [ self.terrain[i][j] ]
        for v in range(self.result-1, 0, -1):
            
            # Right
            if (j+1) < size and temp_terrain[i][j+1] == v:
                j = j+1
            # Down
            if (i+1) < size and temp_terrain[i+1][j] == v:
                i = i+1
            # Left
            if j > 0 and temp_terrain[i][j-1] == v:
                j = j-1
            # Up
            if i > 0 and temp_terrain[i-1][j] == v:
                i = i-1
            
                
            paths.append( self.terrain[i][j] )
               
        self.start = [i, j] 
        paths.sort(reverse=True)
        
        return paths


    # Get the row,column starting point for the coaster's main drop path 
    #
    # @return an int[] with the first element being the row and the second being the column
    def getCoasterStart(self):
        if self.start is None:
            self.getCoasterPath()
        
        return self.start
