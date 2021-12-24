# represent a matrix using a list of lists

#def print_matrix(matrix):
    #for row in matrix:
        #for number in row:
            #print(number,'\t',end ='')
        #print()

def print_matrix(matrix):
    # print the matrix using its row_index and col_index
    for row_index in range(0,len(matrix)):
        for col_index in range(0,len(matrix[0])):
            number = matrix[row_index][col_index]
            print(number,'\t',end ='')
        print() 
def transpose(matrix):
    # transpose the matrix
    matrix_t = []
    for col_index in range(0,len(matrix[0])):
        new_row = []
        for row_index in range(0,len(matrix)):
            number = matrix[row_index][col_index]
            new_row.append(number)
        matrix_t.append(new_row)
    return matrix_t


def main():
    A = [[2,4,1,1],[7,0,1,5],[3,6,4,5]]
    print_matrix(A)
    print('Transpose of A')
    A_t = transpose(A)
    print_matrix(A_t)
main()