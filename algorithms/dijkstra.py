def dijkstra(adj_matrix, weight_matrix, start_node):
        nodeNum = len(adj_matrix)
        visited = [False]*nodeNum
        distance = [(1e7, '')]*nodeNum
        distance[start_node] = (0,'')

        for i in range(nodeNum):
            min_distance = 1e7
            for j in range(nodeNum):
                if not visited[j] and distance[j][0] < min_distance:
                    min_distance = distance[j][0]
                    current_node_index = j

            visited[current_node_index] = True

            for j in range(nodeNum):
                if adj_matrix[i][j] != 0:
                    distanceWeight = distance[current_node_index][0] + weight_matrix[i][j] 
                    if distanceWeight < distance[j][0]:
                        distance[j] = (distanceWeight, distance[current_node_index][1] + str(current_node_index))

        for i in range(nodeNum):
            if distance[i] == 1e7:
                print(f"No path from node {start_node} to node {i}")
            else:
                print(f"Optimal path from node {start_node} to node {i}: {distance[i]}")