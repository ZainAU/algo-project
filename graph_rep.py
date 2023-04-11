import dijkstra
import data_open
import matplotlib.pyplot as plt

NUMBER_OF_NODES_MAX = 3198

def analyse(fname, n):
    """
    Analyse the graph and return the graph and the airports dictionary.
    """
    # run a loop from n to 2
    # for each n, run dijkstra's algorithm
    y_cordinates = []
    x_cordinates = []
    for i in range(2,n):
        # open the data
        graph, airports_dict = data_open.open_data(fname, i)
        # find start point
        start = 0
        for j in graph:
            if len(graph[j]) > 0:
                start = j
                break

        # run dijkstra's algorithm
        distances, paths, steps = dijkstra.dijkstra_with_path(graph, str(start))
        # append the number of nodes to x_cordinates
        x_cordinates.append(len(graph))
        # append the number of steps to y_cordinates
        y_cordinates.append(steps)
        print("Number of nodes: ", len(graph), "Number of steps: ", steps)

    return x_cordinates, y_cordinates
x_ , y_ = analyse("routes.txt", NUMBER_OF_NODES_MAX)
plt.plot(x_, y_)
plt.xlabel("Number of nodes")
plt.ylabel("Number of steps")
plt.show()

GRAPH_FILES = ["s3.gr","s4.gr", "s5.gr", "s6.gr", "s7.gr", "s8.gr", "s9.gr", "s10.gr"]
# number of nodes in the graph files is 8, 16, 32, 64, 128, 256, 512, 1024
def analyse_(gfiles, n):
    """
    Analyse the graph and return the graph and the airports dictionary.
    """
    # run a loop from n to 2
    # for each n, run dijkstra's algorithm
    y_cordinates = []
    x_cordinates = []
    for i in range(n):
        # open the data
        graph = data_open.open_data_g(gfiles[i])
        # find start point
        start = 1
        for j in graph:
            if len(graph[j]) > 0:
                start = j
                break

        # run dijkstra's algorithm
        distances, paths, steps = dijkstra.dijkstra_with_path(graph, start)
        # append the number of nodes to x_cordinates
        x_cordinates.append(len(graph))
        # append the number of steps to y_cordinates
        y_cordinates.append(steps)
        print("Number of nodes: ", len(graph), "Number of steps: ", steps)

    return x_cordinates, y_cordinates

# print(analyse(GRAPH_FILES, 8))

