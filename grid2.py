def create_grid(filename):
    infile = open(filename,'r')
    content = infile.readlines()
    infile.close()
    print(content)
    rows = int(content.pop(0).strip())
    columns = int(content.pop(0).strip())
    grid = []
    print(rows)
    print(columns)
    print(content)
    for row_index in range(0,rows):
        row = []
        for col_index in range(0,columns):
            row.append(int(content[col_index+row_index*columns].strip()))
        grid.append(row)
    return grid    
def main():
    grid = create_grid('data_1.txt')
    print(grid)
            
main()            