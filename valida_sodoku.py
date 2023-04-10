import math
def is_valid_sudoku(partial_assignment) :
    # Return True if subarray
    # partiaT-assignnent Istart-row:end_row][start-col:end_coL] contains any
    # dupTicates in {1, 2, ..., 7en(partial_assignnent)}; ot}rerwjse return
    # False.
    def has_duplicate(block) :
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))
    
    n = len(partial_assignment)
    # Check row and column constraints.
    if any( has_duplicate([partial_assignment[i][j] for j in range(n)])
            or has_duplicate([partial_assignment[j][i] for j in range(n)])
            for i in range(n)):
        return False
    
    # Check region constraints.
    region_size = int(math.sqrt(n))
    return all(not has_duplicate([partial_assignment[a][b] 
                for a in range(region_size * I, region_size * (I + 1))
                for b in range(region_size * J, region_size * (J + 1))])          
                
                for I in range(region_size) for J in range(region_size))
    
sodoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
print(is_valid_sudoku(sodoku))