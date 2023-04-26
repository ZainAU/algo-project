# dijkstra algorithm
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
# https://www.youtube.com/watch?v=gdmfOwyQlcI
# greedy algorithm

# here the graph is matrx of size n x n
# where n is the number of nodes
# graph[i][j] is the weight of edge between node i and node j
# if there is no edge between node i and node j then graph[i][j] = 0
# if there is an edge between node i and node j then graph[i][j] = weight of edge


# import heapq


# def dijkstra_with_path(graph, start):
#     visited = set()
#     distances = {v: float('inf') for v in graph}
#     distances[start] = 0
#     paths = {start: [start]}
#     heap = [(0, start)]
#     steps = 0

#     while heap:
#         (dist, vertex) = heapq.heappop(heap)

#         if vertex in visited:
#             continue

#         visited.add(vertex)

#         for neighbor, weight in graph[vertex].items():
#             if neighbor in visited:
#                 continue
#             tentative_distance = distances[vertex] + weight
#             if tentative_distance < distances[neighbor]:
#                 distances[neighbor] = tentative_distance
#                 paths[neighbor] = paths[vertex] + [neighbor]
#                 heapq.heappush(heap, (tentative_distance, neighbor))
#             steps += 1

#     return distances, paths, steps


import random


def monte_carlo_shortest_path(graph, start, end, iterations):
    shortest_path = None
    shortest_distance = float('inf')

    for i in range(iterations):
        current_node = start
        current_path = [start]
        current_distance = 0

        while current_node != end:
            neighbor_nodes = graph[current_node].keys()
            neighbor_node = random.choice(list(neighbor_nodes))

            new_distance = current_distance + \
                graph[current_node][neighbor_node]
            if new_distance < shortest_distance:
                current_path.append(neighbor_node)
                current_node = neighbor_node
                current_distance = new_distance

            elif new_distance == shortest_distance:
                if random.random() < shortest_distance / new_distance:
                    current_path.append(neighbor_node)
                    current_node = neighbor_node
                    current_distance = new_distance
        print(f'i, current_distance: {i, current_distance}')
        if current_distance < shortest_distance:
            shortest_path = current_path
            shortest_distance = current_distance
        print(f'i, shortest_distance: {i, shortest_distance}')

    return shortest_path, shortest_distance


if __name__ == "__main__":
    # # testing the algorithm
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_node = 'A'

    shortest_distances = monte_carlo_shortest_path(graph, start_node, "D", 10)

    print(shortest_distances)
