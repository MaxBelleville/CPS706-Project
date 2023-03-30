def printMatrix(M):
    print('[')
    for row in M:
        print(' ' + str(row))
    print(']')

adjMatrix = []

with open('matrixInput.txt') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i][:-1]    #Removes \n character

    #Create matrix    

    for line in lines:
        lineData = line.split(',')
        for i in range(0, len(lineData)):
            lineData[i] = int(lineData[i])
        adjMatrix.append(lineData)

printMatrix(adjMatrix)
