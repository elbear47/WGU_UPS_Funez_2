import csv

from Package import Package
from Graph import Graph, Vertex
# from CSVReader import map, Address
from test import Test, map
from Item import check_time_first_truck

# we will use the range as indexes for many functions
range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
index = 1

package_list1 = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37,
                 40]  # packages with early deadline plus packages that need to be with these
package_list2 = [3, 18, 36, 38, 2, 4, 5, 7, 8, 10, 11, 12, 17, 19, 21,
                 22]  # 3,18,36,38 can only be on truck 2. we will add some EOD's (these are low priority)
package_list3 = [6, 9, 25, 28, 32, 23, 24, 26, 27, 33, 35,
                 39]  # delayed and early deadline must deliver 6 and 25 first( add nine here cause address will be corrected anyway)

# low priority
# 2,4,5,7,8,10,11,12,17,19,21,22, # load on truck 2
# 23,24,26,27,33,35,39 # load on truck 3
# create packages
package = Package()
# load data
package.load_csv_data(package)
truck1 = []
truck2 = []
truck3 = []
# load trucks manually
for package_id in package_list1:
    truck1.append(package_id)
for package_id in package_list2:
    truck2.append(package_id)
for package_id in package_list3:
    truck3.append(package_id)
print("Truck one contains these package id's: ", truck1)
# print("Truck two contains these package id's: ", truck2)
# print("Truck three contains these package id's: ", truck3)
print("--------------------------------------------")
print("truck one needs to go to these addresses:")
address_list_truck1 = []
# add the HUB since we always begin at the HUB
address_list_truck1.append('4001 South 700 East')
index = 0
for package_id in truck1:
    address_list_truck1.append(package.get_address(package, package_id))
# Remove duplicate addresses from list by converting to dict and then back into list
# Trick here is that : dicts cannot have duplicate keys ;)
address_list_truck1 = list(dict.fromkeys(address_list_truck1))

for address in address_list_truck1:
    print(address)
print("--------------------------------------------")
print("Route")
print("--------------------------------------------")

# truck 1
# create object to add addresses
t = Test()
# add addresses uses address list developed by the package id's
for address in address_list_truck1:
    t.add_address(address)

# get distances between all the addresses
# nearest neighbor algorithm
i = 0
# set current location to the hub
for location1 in list(map.adjacency_list):
    current_address = location1
    break

# next neighbor algo
while len(map.adjacency_list) > 1:

    for location1 in list(map.adjacency_list):
        min_distance = 100000000000
        min_address_name = ''
        if location1 == current_address:
            for location2 in list(map.adjacency_list):
                if map.get_address_name(location1) == map.get_address_name(location2):
                    continue
                dist = map.get_weight(location1, location2)
                if min_distance > float(dist):
                    min_distance = float(dist)

                    min_address_name = location2  # min address name is now the new location
                    i = i + 1
                    if i > 0:  # skip the first iteration to set current Address
                        # this will be used to start from last stop and continue iterating
                        current_address = location2

            del map.adjacency_list[location1]

            print('from:', location1, ' To:', min_address_name, ' Distance: ', min_distance, "Time: ",
                  check_time_first_truck(min_distance))

# print(map.adjacency_list)
# add an address object which will implicitly add our map and will use the Graph class to do so

# map.adjacency_list
# a = Address()
# a.add_address()
# a.get_weight()
# print(map.adjacency_list.items())
# for address1 in address_list_truck1:
#   for address2 in address_list_truck1:
#        if address1 == address2:
#            0
#        else:
#            print(map.get_distance(a.return_address_key(address1),
#                                   a.return_address_key(address2)))


'''
# Create a graph object which we will call route. we will add addresses to this
location_file = open('./files/addressIndex.csv', 'r')  # open csv
reader = csv.reader(location_file)  # reader will be our csv reader
route = Graph()  # graph which we will call route to add the locations which we will call vertex's
for row in reader:
    location = Vertex(int(row[0]), row[1], row[2])  # create a new location/vertex
    route.add_vertex(location)  # add that vertex to the route
for location1 in route.adjacency_list:  # loop locations in the route
    for location2 in route.adjacency_list:
        # add an edge between two locations
        weight = route.get_weight(location1, location2)
        # add connection between two vertices
        route.add_undirected_edge(location1, location2, weight)
for location1 in route.adjacency_list:  # loop locations in the route
    for location2 in route.adjacency_list:
        print("FROM: ", location1, " TO: ", location2, " Distance: ", route.get_distance(location1, location2))'''
# print("truck one has these package details: ", package.search(package.table, int(package.table[1][0])))
# search for a package
# print(package.search(package.table, 1))

# get all package id's
# print("Package ID's: ")
# range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
# for row in range:
#    print(package.table[index][0])
#    index = index + 1

#     print(package.search(package.table, int(package.table[1][0])))
