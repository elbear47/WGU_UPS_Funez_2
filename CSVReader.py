from Graph import Vertex, Graph
import csv

location_file = open('./files/addressIndex.csv', 'r')  # open csv
reader = csv.reader(location_file)  # reader will be our csv reader
map = Graph()  # graph which we will call map to add the locations which we will call vertex's

class Address:

    def add_address(self):
        for row in reader:
            location = Vertex(int(row[0]), row[1], row[2])  # create a new location/vertex
            map.add_vertex(location)  # add that vertex to the map

    def get_weight(self):
        for location1 in map.adjacency_list:  # loop locations in the map
            for location2 in map.adjacency_list:
                # add an edge between two locations
                weight = map.get_weight(location1, location2)
                # add connection between two vertices
                map.add_undirected_edge(location1, location2, weight)

    def print_details(self):
        for location1 in map.adjacency_list:  # loop locations in the map
            for location2 in map.adjacency_list:
                print("FROM: ", location1, " TO: ", location2, " Distance: ",
                      map.get_distance(location1, location2))
                print(location1)
                print(location2)
                print(map.get_distance(location1, location2))
                break

    def return_address_key(self, address_name):
        location_file = open('./files/addressIndex.csv', 'r')  # open csv
        reader = csv.reader(location_file)  # reader will be our csv reader
        for location in map.adjacency_list:
            for row in reader:
                if row[2] == address_name:
                    return location



# test main
'''
a = Address()
a.add_address()
a.get_weight()
for location1 in map.adjacency_list:
    print(map.get_weight(location1, location1))
for location1 in map.adjacency_list:
    if a.return_address_key('4001 South 700 East').index == location1.index:
        print(location1)
        print(type(location1))
        print(a.return_address_key('4001 South 700 East'))
        print(type(a.return_address_key('4001 South 700 East')))
        print(map.get_distance(location1, location1))
        print(map.get_distance(a.return_address_key('4001 South 700 East'),
                               a.return_address_key('4001 South 700 East')))

'''
