case = input()

# return list of horizontal, vertical and diagonal neighbours
def neighbours(m, i, j):
    return [(x,y) for x in [i-1,i,i+1] 
                    for y in [j-1,j,j+1] 
                    if x in range(0,len(m)) and y in range(0,len(m[x])) and (x,y) != (i,j) and m[x][y]!=0]

def medicineApplied(matrix,x,y):
    if matrix[x][y] == 1:
        matrix[x][y] = (0)

for _ in range(int(case)):

    days = 0
    matrix   = []
    quantity = input().split()
    a, b = int(quantity[0]), int(quantity[1])
    
    # creating the case matrix
    for i in range(a):
        line = []
        elements = input().split()
        for j in range(b): line.append(int(elements[j]))
        matrix.append(line)
    X, Y = a, b
    # first coord where the medicine will be applied
    medicineX, medicineY = input().split()
    medicineX, medicineY = int(medicineX)-1, int(medicineY)-1
    medicineApplied(matrix,medicineX,medicineY)

    #neighbors that gonna receive the medicine on the next day
    spreadMedicine = [(medicineX,medicineY)]
    bckspreadMedicine = spreadMedicine
    list_neighbours = []
    while max([value for linha in matrix for value in linha]) == 1:
            for element in sorted(spreadMedicine):
                value = neighbours(matrix, element[0],element[1])
                for x in value: list_neighbours.append(x)
                spreadMedicine.remove(element)
            if len(list_neighbours) == 0:
                break
            for coord in sorted(list_neighbours):
                    medicineApplied(matrix,coord[0],coord[1])
                    spreadMedicine.append(coord) if coord not in bckspreadMedicine else _
                    bckspreadMedicine.append(coord) if coord not in bckspreadMedicine else _
                    list_neighbours.remove(coord)
            if len(list_neighbours) == 0 : days+=1        
    print(days)
