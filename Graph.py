import csv


# vertex is a location which we will add using index, location name, and address
class Vertex:
    def __init__(self, index, location_name, address):
        self.index = index
        self.location_name = location_name
        self.address = address

    # print format
    def __str__(self):
        return f"index: {self.index}, location:{self.location_name}, address: {self.address}"

    # print format
    def __repr__(self):
        return f"index: {self.index}, location:{self.location_name}, address: {self.address}"


# graph is going to be our map which we will add vertex's(locations) too
class Graph:
    def __init__(self):
        self.adjacency_list = {}  # dictionary which we will add locations
        self.edge_weights = {}  # connections between locations

    def add_vertex(self, new_vertex):  # add a location
        self.adjacency_list[new_vertex] = []  # add it to the adjacency list

    # our map will be an undirected map so we will use add_directed_edge twice each way
    def add_directed_edge(self, from_vertex, to_vertex, weight):
        self.edge_weights[(from_vertex, to_vertex)] = weight  # weight will be the distance
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight):  # add undirected edge(same as adding two directed edges)
        self.add_directed_edge(vertex_a, vertex_b, float(weight))  # from b to a
        self.add_directed_edge(vertex_b, vertex_a, float(weight))  # from a to b

    # this will give us distance between location a and b
    def get_weight(self, location_a, location_b):  # location(a or b) is a vertex object
        if location_a.index > location_b.index:  # always use the larger address index
            larger_index = location_a.index
            smaller_index = location_b.index
        else:
            larger_index = location_b.index
            smaller_index = location_a.index

        # Read distances CSV
        distances_file = open('./files/WGUDistanceData.csv', 'r')
        reader = csv.reader(distances_file)
        # create an empty list to append distances
        distances = []
        for row in reader:
            distances.append(row)
        return distances[larger_index][smaller_index]  # return the distance between two locations

    # another function to get distance between location a and location b
    def get_distance(self, a, b):
        distance = self.edge_weights[(a, b)]  # accesses my edge weights dictionary by using the
        # location of a and b as a key for the value of
        # the distance in miles
        return distance

    # need a function to get address details from just address name
    # we will extract address_name from packages csv to grab addresses details here
    def get_address_details(self, address_name):
        location_file = open('./files/addressIndex.csv', 'r')  # open csv
        reader = csv.reader(location_file)  # reader will be our csv reader
        map = Graph()

        for row in reader:
            if row[2] == address_name:
                location = Vertex(int(row[0]), row[1], row[2])  # create a new location/vertex
                # map.add_vertex(location)  # add that vertex to the map
                return location

    # a way to get the location name by using the Vertex objects stored in the adjacency list
    def get_location_name(self, Vertex):
        return Vertex.location_name

    # way to return the address
    def get_address(self, Vertex):
        return Vertex.address
