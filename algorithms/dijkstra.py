def dijkstra(adj_matrix, weight_matrix, start_node, end_node):
        nodeNum = len(adj_matrix)
        visited = [False]*nodeNum
        distance = [float("inf")]*nodeNum
        paths = [[]]*nodeNum
        distance[start_node] = 0

        for i in range(nodeNum):
            min_distance = float("inf")
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
                        paths[j] = paths[current_node_index] + [current_node_index]
        
        return (distance[end_node], paths[end_node] + [end_node])