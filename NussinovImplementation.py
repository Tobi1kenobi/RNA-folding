import numpy as np

x = "AAACUUUCCCAGGG"
xlist = list(x)

def complimentarity(base_tuple):
    comp_pairs = (("A","U"),
                  ("U","A"),
                  ("G", "U"),
                  ("U", "G"),
                  ("C", "G"),
                  ("G", "C"))
    if base_tuple in comp_pairs:
        return 1
    else:
        return 0

numenov_matrix = []*len(x)

for i in range(len(x)):
    numenov_matrix.append([0]*len(x))

print(np.array(numenov_matrix))

def M_function(matrix):
    stack = []
    for start_col in range(1, len(matrix)):
        for column in range(start_col, len(matrix)):
            row = column - start_col
            print(column,row)
            max_bifurc = 0
            if row+1<column-1:
                for k in range(row+1, column-1):
                    cur_bifurc = matrix[row][k]+matrix[k+1][column]
                    max_bifurc = max((cur_bifurc,max_bifurc))
            max_val = max((matrix[row][column-1],
                           matrix[row+1][column],
                           matrix[row+1][column-1]+complimentarity((xlist[row],xlist[column])),
                           max_bifurc))
            matrix[row][column] = max_val
    return matrix

print(np.array(M_function(numenov_matrix)))

stacklist = []
recorded_bases =[]
length_matrix = len(numenov_matrix)
stacklist.append((0,length_matrix-1))

def traceback(matrix,stack):
    if stack == []:
        return None
    i,j = stack.pop()
    print(i,j)
    if i >= j:
        traceback(matrix, stack)
    elif matrix[i+1][j] == matrix[i][j]:
        stack.append((i+1,j))
    elif matrix[i][j-1] == matrix[i][j]:
        stack.append((i,j-1))
    elif matrix[i+1][j-1] + complimentarity((xlist[i],xlist[j])) == matrix[i][j]:
        recorded_bases.append((i,j))
        stack.append((i+1,j-1))
    else:
        for k in range(i+1,j-1):
            if matrix[i][k] + matrix[k+1][j] == matrix[i][j]:
                stack.append((k+1,j))
                stack.append((i,k))
    traceback(matrix,stack)

traceback(numenov_matrix,stacklist)