# Elber Funez --> Student ID #: 000958187

import csv

from Package import Package
from Graph import Graph, Vertex
from Address import Address, map
from Item import check_time_first_truck

# load packages manually
# GOING ON TRUCK ONE
package_list1 = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37,
                 40]  # packages with early deadline plus packages that need to be with these
# GOING ON TRUCK TWO
package_list2 = [3, 18, 36, 38, 2, 4, 5, 7, 8, 10, 11, 12, 17, 19, 21,
                 22]  # 3,18,36,38 can only be on truck 2. we will add some EOD's (these are low priority)
# GOING ON TRUCK THREE
package_list3 = [6, 9, 25, 28, 32, 23, 24, 26, 27, 33, 35,
                 39]  # delayed and early deadline must deliver 6 and 25 first( add nine here cause address will be corrected anyway)

# instantiate a package class so we can load data
package = Package()
# load data
package.load_csv_data(package)
# create truck lists for each truck
truck1 = []
truck2 = []
truck3 = []

# load trucks using the package lists
for package_id in package_list1:
    truck1.append(package_id)
for package_id in package_list2:
    truck2.append(package_id)
for package_id in package_list3:
    truck3.append(package_id)

# --------------------TRUCK ONE ----------------------------#
print("-----------TRUCK ONE DETAILS-------------------\n")
print("Truck one contains these package id's: ", truck1)  # print all package id's in truck one
print("--------------------------------------------")
print("truck one needs to go to these addresses:")
address_list_truck1 = []  # initialize an empty address list
# add the HUB since we always begin at the HUB ( this will be the start)
address_list_truck1.append('4001 South 700 East')

for package_id in truck1:
    # add address names to our address list for truck one
    address_list_truck1.append(package.get_address(package, package_id))

# Remove duplicate addresses from list by converting to dict and then back into list
# Trick here is that : dicts cannot have duplicate keys ;)
address_list_truck1 = list(dict.fromkeys(address_list_truck1))

# Print addresses Truck one has to take
for address in address_list_truck1:
    print(address)
print("--------------------------------------------")
print("Truck One Route")
print("********************************************")

# create address object to use Address functions
t1 = Address()

# add addresses uses address list developed by the package id's
for address in address_list_truck1:
    t1.add_address(address)  # add addresses to the truck list for truck one

i = 0  # we will use i to iterate
# set current location to the hub
for location1 in list(map.adjacency_list):
    current_address = location1
    break

# get distances between all the addresses
# nearest neighbor algorithm
# Space-time complexity is O(N)
while len(map.adjacency_list) > 1:  # only run until there is one element left in the list
    # so we always have a TO:location
    # loop through Vertex Objects (locations) in the adjacency list
    for location1 in list(map.adjacency_list):
        # set the min distance to a high number because it will check if the min distance is greater than the
        # distance between both locations. It runs a for loop and sets the min distance to the
        # distance between the two locations and continues doing that until the minimum distance is found
        min_distance = 100000000000
        min_address_name = ''  # initialize to an empty name
        if location1 == current_address:  # make sure your iteration starts at the last delivered address
            for location2 in list(map.adjacency_list):
                if map.get_address_name(location1) == map.get_address_name(location2):  # if locations are the same
                    # don't do anything
                    continue
                dist = map.get_weight(location1, location2)  # else get the distance between the last delivered
                # address and nearest neighbor
                if min_distance > float(dist):  # find smallest distance
                    min_distance = float(dist)

                    min_address_name = location2  # min address name is now the new location
                    i = i + 1  # increment
                    if i > 0:  # skip the first iteration to set last delivered Address which we call current_address
                        # this will be used to start from last stop and continue iterating
                        current_address = location2
            # delete the start location we just iterated
            del map.adjacency_list[location1]
            # print truck route
            print('from:', location1, ' To:', min_address_name, ' Distance: ', min_distance, "Time: ",
                  check_time_first_truck(min_distance))
print("********************************************")
print("-----------DONE WITH TRUCK ONE--------------")
print("--------------------------------------------\n\n")
# Clear List so we can load truck two data
map.adjacency_list.clear()

# --------------------TRUCK TWO ----------------------------#
print("-----------TRUCK TWO DETAILS-------------------\n")
print("Truck two contains these package id's: ", truck2)
print("--------------------------------------------")
print("truck two needs to go to these addresses:")
address_list_truck2 = []
# add the HUB since we always begin at the HUB
address_list_truck2.append('4001 South 700 East')

for package_id in truck2:
    address_list_truck2.append(package.get_address(package, package_id))
# Remove duplicate addresses from list by converting to dict and then back into list
# Trick here is that : dicts cannot have duplicate keys
address_list_truck2 = list(dict.fromkeys(address_list_truck2))

for address in address_list_truck2:
    print(address)
print("--------------------------------------------")
print("Truck Two Route")
print("--------------------------------------------")
# create object to add addresses
t2 = Address()
# add addresses uses address list developed by the package id's
for address in address_list_truck2:
    t2.add_address(address)

# get distances between all the addresses
# nearest neighbor algorithm
i = 0
# set current location to the hub
for location1 in list(map.adjacency_list):
    current_address = location1
    break

# next neighbor algo
print(len(address_list_truck2))
#from: index: 26, location:Wheeler Historic Farm
while len(map.adjacency_list) > 1:

    for location1 in list(map.adjacency_list):
        min_distance = 100000000000
        min_address_name = ''
        if location1 == current_address:
            for location2 in list(map.adjacency_list):
                if map.get_address_name(location1) == map.get_address_name(location2):
                    continue
                dist = map.get_weight(location1, location2)
                if min_distance > float(dist) and len(map.adjacency_list) > 1:
                    min_distance = float(dist)

                    min_address_name = location2  # min address name is now the new location
                    i = i + 1
                    if i > 0:  # skip the first iteration to set current Address
                        # this will be used to start from last stop and continue iterating
                        current_address = location2

            del map.adjacency_list[location1]
            if min_address_name.__str__() != 0:
                print('from:', location1, ' To:', min_address_name, ' Distance: ', min_distance, "Time: ",
                  check_time_first_truck(min_distance))
print("--------------------------------------------")
print("-----------DONE WITH TRUCK TWO--------------")
print("--------------------------------------------\n\n")
# Clear List so we can load truck three data
map.adjacency_list.clear()
# --------------------TRUCK THREE ----------------------------#
print("-----------TRUCK THREE DETAILS-------------------\n")
print("Truck Three contains these package id's: ", truck2)
print("--------------------------------------------")
print("truck three needs to go to these addresses:")
address_list_truck3 = []
# add the HUB since we always begin at the HUB
address_list_truck3.append('4001 South 700 East')

for package_id in truck3:
    address_list_truck3.append(package.get_address(package, package_id))
# Remove duplicate addresses from list by converting to dict and then back into list
# Trick here is that : dicts cannot have duplicate keys ;)
address_list_truck3 = list(dict.fromkeys(address_list_truck3))

for address in address_list_truck3:
    print(address)
print("--------------------------------------------")
print("Truck Three Route")
print("--------------------------------------------")
# create object to add addresses
t3 = Address()
# add addresses uses address list developed by the package id's
for address in address_list_truck3:
    t3.add_address(address)

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
print("--------------------------------------------")
print("-----------DONE WITH TRUCK THREE--------------")
print("--------------------------------------------\n\n")
# Clear List so we can load truck two data
map.adjacency_list.clear()

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
