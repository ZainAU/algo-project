
import dijkstra
AIRPORTS_FILE = "airports.txt"
# Airline	2-letter (IATA) or 3-letter (ICAO) code of the airline.
# Airline ID	Unique OpenFlights identifier for airline (see Airline).
# Source airport	3-letter (IATA) or 4-letter (ICAO) code of the source airport.
# Source airport ID	Unique OpenFlights identifier for source airport (see Airport)
# Destination airport	3-letter (IATA) or 4-letter (ICAO) code of the destination airport.
# Destination airport ID	Unique OpenFlights identifier for destination airport (see Airport)
# Codeshare	"Y" if this flight is a codeshare (that is, not operated by Airline, but another carrier), empty otherwise.
# Stops	Number of stops on this flight ("0" for direct)
# Equipment	3-letter codes for plane type(s) generally used on this flight, separated by space

# source: https://openflights.org/data.html

# read the data


def open_data(filename, n):
    # reads the data from the file
    # returns a graph of the form: {node: {neighbor: cost}}
    # where node is a string of the form "airport_id:airport_name"
    # and neighbor is a string of the form "airport_id:airport_name"
    # and cost is the distance between the two airports
    # the graph is directed and weighted since an edge does not always exist between two airports

    # open the file
    replace_Count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(AIRPORTS_FILE, 'r', encoding='utf-8') as f:
        airports = f.readlines()
    airports_dict = {}
    # has a list of coordinates for each airport
    # plus the name of the airport
    # and the code of the airport
    for airport in airports:
        airport = airport.split(",")
        airports_dict[airport[0]] = [airport[1],
                                     float(airport[-8]), float(airport[-7])]
    # print("Number of airports: ", len(airports_dict))
    # print("Number of lines in the file: ", len(lines))
    graph = {}
    condition = True
    for line in lines:
        line = line.split(",")
        if (line[7] not in graph or line[5] not in graph) and len(graph) >= n:
            condition = False
        else:
            condition = True
        if condition:
            pass
        else:
            continue
        if line[7] == "0" and line[5] in airports_dict and line[3] in airports_dict:
            # if the flight is direct
            # add the edge to the graph
            # the cost is the distance between the airports
            # print(line[3], line[5])
            if line[5] == "\\N":
                continue
            if line[3] not in graph:
                weight = ((float(airports_dict[line[3]][1]) - float(airports_dict[line[5]][1])) ** 2 + (
                    float(airports_dict[line[3]][2]) - float(airports_dict[line[5]][2])) ** 2) ** 0.5
                graph[line[3]] = {line[5]: weight}
            else:
                if line[5] not in graph[line[3]]:
                    weight = ((float(airports_dict[line[3]][1]) - float(airports_dict[line[5]][1])) ** 2 + (
                        float(airports_dict[line[3]][2]) - float(airports_dict[line[5]][2])) ** 2) ** 0.5
                    graph[line[3]][line[5]] = weight
                else:
                    weight = ((float(airports_dict[line[3]][1]) - float(airports_dict[line[5]][1])) ** 2 + (
                        float(airports_dict[line[3]][2]) - float(airports_dict[line[3]][2])) ** 2) ** 0.5
                    if graph[line[3]][line[5]] > weight:
                        graph[line[3]][line[5]] = weight
                        replace_Count = replace_Count + 1
            if line[5] not in graph:
                graph[line[5]] = {}
    # print("Number of nodes in the graph: ", len(graph))
    # print("replace_Count: ", replace_Count)
    # print(graph)
    return graph, airports_dict


def open_data_g(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()
    graph = {}
    for line in lines:
        line = line.split(",")
        if line[1] not in graph:
            graph[line[1]] = {line[2]: float(line[3])}
        else:
            graph[line[1]][line[2]] = float(line[3])
        if line[2] not in graph:
            graph[line[2]] = {}
    return graph


test_graph, test_airports = open_data("routes.txt", 300000)

# run dijkstra's algorithm
# print the path from the source to the destination
# print(test_graph["1"])
# distances = dijkstra.dijkstra(test_graph, "1")
# #print(distances)
# path = dijkstra.get_shortest_paths(test_graph, distances, "1")

# print the path from the source to the destination
distances, paths, steps = dijkstra.dijkstra_with_path(test_graph, "1")
# print(paths)
# print("Distance from 1 to 675: ", distances["675"])
# print(steps)
