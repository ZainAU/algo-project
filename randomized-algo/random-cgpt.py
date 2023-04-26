import random
import Graph from Graph


def random_shortest_path(graph, source, destination):
    # Create a dictionary to store the distance from the source node to each node in the graph
    distance = {}
    for node in graph:
        distance[node] = float('inf')
    distance[source] = 0

    # Explore the graph by selecting random edges until the destination node is reached
    while True:
        # Choose a random edge from the graph
        random_edge = random.choice(list(graph.keys()))
        node = random.choice(list(graph.keys()))
        neighbour = random.choice(list(graph.keys()))

        # Update the distance to the neighboring node if it is shorter
        if distance[random_edge[0]] + graph[random_edge] < distance[random_edge[1]]:
            distance[random_edge[1]] = distance[random_edge[0]] + \
                graph[random_edge]

        # If the destination node has been reached, stop exploring
        if random_edge[1] == destination:
            break

    # Return the shortest distance from the source node to the destination node
    return distance[destination]


# Driver code to test the algorithm on a sample graph
graph = {
    ('A', 'B'): 2,
    ('A', 'C'): 5,
    ('B', 'C'): 1,
    ('B', 'D'): 6,
    ('C', 'D'): 3,
    ('C', 'E'): 8,
    ('D', 'E'): 4
}

source = 'A'
destination = 'E'


def edge_list_to_adjacency_list(edge_list):
    adjacency_list = {}
    for edge in edge_list:
        vertex1, vertex2 = edge[0], edge[1]
        if vertex1 not in adjacency_list:
            adjacency_list[vertex1] = []
        if vertex2 not in adjacency_list:
            adjacency_list[vertex2] = []
        adjacency_list[vertex1].append(vertex2)
        adjacency_list[vertex2].append(vertex1)
    return adjacency_list


graph = edge_list_to_adjacency_list(graph)

shortest_distance = random_shortest_path(graph, source, destination)
print(
    f"The shortest distance from {source} to {destination} is {shortest_distance}")
