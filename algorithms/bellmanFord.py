def bellmanFord(adj_matrix, weight_matrix, start, end):
    maxVal = float("inf")
    numNodes = len(adj_matrix)
    edges = []

    # ---START OF BUILDING EDGES---
    # The format of an edge is as follows: (NodeA, NodeB, Weight)

    for i in range(numNodes):   # First, add edges connected to starting vertex
        if adj_matrix[i][start] == 1 and (start, i, weight_matrix[i][start]) not in edges:
            edges.append((start, i, weight_matrix[i][start]))
    for i in range(numNodes):
        for j in range(numNodes):
            if i != end and j != end:   # Second, add edges not connected to start, nor ending vertex
                if adj_matrix[i][j] == 1 and (j, i, weight_matrix[i][j]) not in edges:
                    edges.append((i, j, weight_matrix[i][j]))
    for i in range(numNodes):   # Third, add edges connected to ending vertex
        if adj_matrix[i][end] == 1 and (end, i, weight_matrix[i][end]) not in edges:
            edges.append((end, i, weight_matrix[i][end]))

    # Removes duplicate entries in edge list
    tempEdges = list()
    for item in edges:
        if item not in tempEdges:
            tempEdges.append(item)
    edges = tempEdges

    # print('Edges:', edges)

    # ---END OF BUILDING EDGES---

    # ---START OF INITIALIZING TABLES---

    bellmanFordTable = {}   # Table of
    propagationTable = {}   # Updates 1 step ahead of bellmanFordTable

    for i in range(numNodes):
        temp = {}
        for j in range(numNodes):
            if i == j:
                temp[j] = [0, str(j)]
            else:
                temp[j] = [maxVal, '']
        bellmanFordTable[i] = temp.copy()
        propagationTable[i] = temp.copy()

    # print('Initial bellmanFordTable:\n', bellmanFordTable)
    # print('Initial propagationTable:\n', propagationTable)

    # ---END OF INITIALIZING TABLES---

    # ---START OF MAIN ALGORITHM---

    costAtEachIter = []
    for n in range(numNodes - 1):   # Bellman-Ford algorithm loops numNodes - 1 times; n is not used
        # Loop through number of nodes (length of matrix)
        for i in range(numNodes):
            # Loop through number of edges (Get into form shown at top)
            # NOTE: e[0] and e[1] are adjacent nodes, while e[2] is the associated weight
            for e in edges:
                if e[0] == i or e[1] == i:
                    if e[0] == i:
                        other = e[1]
                    else:
                        other = e[0]
                    for j in range(numNodes):
                        if bellmanFordTable[other][j][0] + e[2] < propagationTable[i][j][0]:
                            propagationTable[i][j] = [
                                bellmanFordTable[other][j][0] + e[2], str(i) + str(bellmanFordTable[other][j][1])]
        for i in range(numNodes):
            temp = {}
            for j in range(numNodes):
                temp[j] = [propagationTable[i][j][0],
                           str(propagationTable[i][j][1])]
            bellmanFordTable[i] = temp.copy()
        #print('ITERATION ' + str(n) + ':\n' + str(bellmanFordTable) + '\n')

        costAtEachIter.append([])
        for x in range(numNodes):
            costAtEachIter[n].append(bellmanFordTable[start][x][0])

    # ---END OF MAIN ALGORITHM---
    #print('COSTS:\n', costAtEachIter)
    return bellmanFordTable[start][end], costAtEachIter
