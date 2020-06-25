from Graph import Vertex, Graph
import csv

main_location_file = open('./files/addressIndex.csv', 'r')  # open csv
main_reader = csv.reader(main_location_file)  # reader will be our csv reader
map = Graph()  # graph which we will call map to add the locations which we will call vertex's

class Test:

    def add_address(self, a):
        location_file = open('./files/addressIndex.csv', 'r')  # open csv
        reader = csv.reader(location_file)  # reader will be our csv reader
        for row in reader:
            if row[2] == a:
                location = Vertex(int(row[0]), row[1], row[2])  # create a new location/vertex
                map.add_vertex(location)  # add that vertex to the map
            else:
                None



