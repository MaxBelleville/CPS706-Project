def dijkstra(adj_matrix, weight_matrix, start_node, end_node):
        nodeNum = len(adj_matrix)
        visited = [False]*nodeNum
        distance = [1e7]*nodeNum
        paths = ['']*nodeNum
        distance[start_node] = 0

        for i in range(nodeNum):
            min_distance = 1e7
            for j in range(nodeNum):
                if not visited[j] and distance[j] < min_distance:
                    min_distance = distance[j]
                    current_node_index = j

            visited[current_node_index] = True

            for j in range(nodeNum):
                if adj_matrix[current_node_index][j] != 0:
                    distanceWeight = distance[current_node_index] + weight_matrix[current_node_index][j] 
                    if distanceWeight < distance[j]:
                        distance[j] = distanceWeight
                        paths[j] = paths[current_node_index] + str(current_node_index)
        
        return (distance[end_node], paths[end_node] + str(end_node))