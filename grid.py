
def create_grid(filename):
        infile = open(filename,'r')
        content = infile.readlines()
        rows = int(content.pop(0))
        columns = int(content.pop(0))
        grid = []
        for row_index in range(0,rows):
            row = []
            for col_index in range(0,columns):
                row.append(int(content[col_index+row_index*columns].strip()))
            grid.append(row)
        infile.close()    
        return grid   
       
def display_grid(grid):

        for row_index in range(0,len(grid)):
                print('|',end ='') 
                for col_index in range(0,len(grid[0])):
                        price = round(grid[row_index][col_index])
                        print(price,end ='|')   
                print()

def  find_neighbors(row_index,col_index,grid):
        neighbors = []
        columns = [col_index - 1, col_index, col_index + 1]
        rows = [row_index - 1, row_index, row_index + 1]
        for r in (rows):
                for c in (columns):
                        if (r >= 0 and c >= 0) and (r < len(grid) and c < len(grid[0])) and (r != row_index or c != col_index):
                                neighbors.append(grid[r][c])
        return neighbors

def fill_gaps(grid):
        new_grid = grid
        location = []
        for row_index in range(0,len(grid)):
                for col_index in range (0,len(grid[0])):
                        value = grid[row_index][col_index]
                        if  value == 0:
                                location.append([row_index,col_index])
                                
        for item in location: 
                neighbors = find_neighbors(item[0],item[1],grid)
                ave = sum(neighbors)/len(neighbors)
                new_grid[item[0]][item[1]] = ave
        return new_grid

def find_max(grid):
        max_value = 0
        for row_index in range(0, len(grid)):
                for col_index in range(0, len(grid[0])):
                                       value = grid[row_index][col_index]
                                       if value > max_value:
                                               max_value = value
                                               
        return max_value       
                                      
def find_average(grid):
        values = []
        for row_index in range(0,len(grid)):
                for col_index in range(0,len(grid[0])):
                        values.append(grid[row_index][col_index])
        ave = round(sum(values)/len(values))
        return ave
                            
                        
        
def main():
        grid = create_grid('data_2.txt')
        print('This is our grid:')
        display_grid(grid)
        new_grid = fill_gaps(grid)
        print('\nThis is our newly calculated grid:')
        display_grid(new_grid)
        max_value = find_max(new_grid)
        average = find_average(new_grid)
        print('\nSTATS')
        print('Average housing price in this area is: '+str(average))
        print('Maximum housing price in this area is: '+str(max_value))
  
            
main()