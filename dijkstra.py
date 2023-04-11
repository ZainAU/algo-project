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
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'

shortest_distances = dijkstra(graph, start_node)

print(shortest_distances)
