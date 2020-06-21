from Graph import Vertex, Graph
import csv

location_file = open('./files/addressIndex.csv', 'r')  # open csv
reader = csv.reader(location_file)  # reader will be our csv reader
map = Graph()  # graph which we will call map to add the locations which we will call vertex's

for row in reader:
    location = Vertex(int(row[0]), row[1], row[2])  # create a new location/vertex
    map.add_vertex(location)  # add that vertex to the map

for location1 in map.adjacency_list:  # loop locations in the map
    for location2 in map.adjacency_list:
        # add an edge between two locations
        weight = map.get_weight(location1, location2)
        # add connection between two vertices
        map.add_undirected_edge(location1, location2, weight)

for location1 in map.adjacency_list:  # loop locations in the map
    for location2 in map.adjacency_list:
        print("FROM: ", location1, " TO: ", location2, " Distance: ", map.get_distance(location1, location2))
