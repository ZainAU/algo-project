# dijkstra algorithm
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
# https://www.youtube.com/watch?v=gdmfOwyQlcI
# greedy algorithm

# here the graph is matrx of size n x n
# where n is the number of nodes
# graph[i][j] is the weight of edge between node i and node j
# if there is no edge between node i and node j then graph[i][j] = 0
# if there is an edge between node i and node j then graph[i][j] = weight of edge


import heapq

def dijkstra(graph, start):
    """
    Find the shortest path from a given start node to all other nodes in the graph using Dijkstra's algorithm.
    
    graph: A dictionary representing the graph, where the keys are nodes and the values are dictionaries 
           of the form {neighbor: cost}. The 'cost' represents the cost of the edge between the node and its neighbor.
    start: The node to start the search from.
    
    Returns:
    A dictionary where the keys are the nodes and the values are the shortest path to that node from the start node.
    """
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we have already visited this node with a lower distance, skip it
        if current_distance > distances[current_node]:
            continue

        #print(current_node)
        #print(graph[current_node])
        
        for neighbor, cost in graph[current_node].items():
            #print(neighbor, cost)
            distance = current_distance + cost
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


def dijkstra_with_path(graph, start):
    visited = set()
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    paths = {start: [start]}
    heap = [(0, start)]

    while heap:
        (dist, vertex) = heapq.heappop(heap)

        if vertex in visited:
            continue

        visited.add(vertex)

        for neighbor, weight in graph[vertex].items():
            if neighbor in visited:
                continue
            tentative_distance = distances[vertex] + weight
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                paths[neighbor] = paths[vertex] + [neighbor]
                heapq.heappush(heap, (tentative_distance, neighbor))

    return distances, paths


# # testing the algorithm
# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }

# start_node = 'A'

# shortest_distances = dijkstra(graph, start_node)

# print(shortest_distances)
