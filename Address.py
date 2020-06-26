from Graph import Vertex, Graph
import csv

main_location_file = open('./files/addressIndex.csv', 'r')  # open csv
main_reader = csv.reader(main_location_file)  # reader will be our csv reader
# we will call location =  vertex
map = Graph()  # graph which we will call map to add the location to truck one


class Address:

    # add address to the map
    def add_address(self, a):
        location_file = open('./files/addressIndex.csv', 'r')  # open csv
        reader = csv.reader(location_file)  # reader will be our csv reader
        for row in reader:
            if row[2] == a:
                location = Vertex(int(row[0]), row[1], row[2])  # create a new location/vertex
                map.add_vertex(location)  # add that vertex to the map

            else:
                None

    # get weight will help up get the distance between two locations
    def get_weight(self):
        for location1 in map.adjacency_list:  # loop locations in the map
            for location2 in map.adjacency_list:
                # add an edge between two locations
                weight = map.get_weight(location1, location2)
                # add connection between two vertices
                map.add_undirected_edge(location1, location2, weight)

    # return address id
    def return_address_key(self, address_name):
        location_file = open('./files/addressIndex.csv', 'r')  # open csv
        reader = csv.reader(location_file)  # reader will be our csv reader
        for location in map.adjacency_list:
            for row in reader:
                if row[2] == address_name:
                    return location

    # print details of the locations looping FROM and TO plus the distances
    def print_details(self):
        for location1 in map.adjacency_list:  # loop locations in the map
            for location2 in map.adjacency_list:
                print("FROM: ", location1, " TO: ", location2, " Distance: ",  # print
                      map.get_distance(location1, location2))
                print(map.get_distance(location1, location2))
                break
