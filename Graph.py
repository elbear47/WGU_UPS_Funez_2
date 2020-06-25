import csv


class Vertex:
    def __init__(self, index, location_name, address):
        self.index = index
        self.location_name = location_name
        self.address = address

    def __str__(self):
        return f"index: {self.index}, location:{self.location_name}, address: {self.address}"

    def __repr__(self):
        return f"index: {self.index}, location:{self.location_name}, address: {self.address}"


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight):
        self.add_directed_edge(vertex_a, vertex_b, float(weight))
        self.add_directed_edge(vertex_b, vertex_a, float(weight))

    def get_weight(self, location_a, location_b):  # location(a or b) is a vertex object
        if location_a.index > location_b.index:
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
        return distances[larger_index][smaller_index]

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
                #map.add_vertex(location)  # add that vertex to the map
                return location
    def get_address_name(self, Vertex):
        return Vertex.location_name



