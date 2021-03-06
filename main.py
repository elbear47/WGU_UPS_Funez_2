from Package import Package
from Address import Address, map
from Times import check_time_first_truck, check_time_second_truck
from datetime import datetime

package = Package()
package.load_csv_data(package)

# GOING ON TRUCK ONE
package_list1 = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37,
                 40]
# GOING ON TRUCK TWO
package_list2 = [3, 18, 36, 38, 2, 4, 5, 7, 8, 10, 11, 12, 17, 19, 21,
                 22]  # 3,18,36,38 can only be on truck 2. we will add some EOD's (these are low priority)
# GOING ON TRUCK ONE (SECOND TRIP)
package_list3 = [6, 9, 25, 28, 32, 23, 24, 26, 27, 33, 35,
                 39]
# WE will call truck 1(second route) --> truck three
# create truck lists for each truck
truck1 = []
truck2 = []
truck3 = []
# load packages for truck one
for package_id in package_list1:
    truck1.append(package_id)
# load packages for truck two
for package_id in package_list2:
    truck2.append(package_id)
# load packages for truck three
for package_id in package_list3:
    truck3.append(package_id)
# take user input for the three choices
user_input = int(input("Press 1 to Print Truck Route Details \n"
                       "Press 2 to view delivered packages by time range/package id \n"
                       "Press 3 to view ALL Package status by time range \n"
                       ))
if user_input == 1:
    # --------------------TRUCK ONE ----------------------------#
    print("-----------TRUCK ONE DETAILS-------------------\n")
    print("Truck one contains these package id's: ", truck1)  # print all package id's in truck one
    print("--------------------------------------------")
    address_list_truck1 = []  # initialize an empty address list
    # add the HUB since we always begin at the HUB ( this will be the start)
    address_list_truck1.append('4001 South 700 East')
    for package_id in truck1:
        # add address names to our address list for truck one
        address_list_truck1.append(package.get_address(package, package_id))

    for package_id in package_list1:
        # add package_id and address to a dict, to be able to figure out which package_ids are
        # going to which address
        package.add_address_to_package_list(package.get_address(package, package_id), package_id)
    # Remove duplicate addresses from list by converting to dict and then back into list
    # Trick here is that : dicts cannot have duplicate keys ;)
    address_list_truck1 = list(dict.fromkeys(address_list_truck1))

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
    # Set total miles equal to zero and add miles each route
    total_Miles = 0
    # get distances between all the addresses
    # nearest neighbor algorithm
    # Space-time complexity is O(N)
    #
    #
    #
    #

    while len(map.adjacency_list) > 1:  # only run until there is one element left in the list
        # loop through Vertex Objects (locations) in the adjacency list
        for location1 in list(map.adjacency_list):
            # set the min distance to a high number because it will check if the min distance is greater than the
            # distance between both locations. It runs a for loop and sets the min distance to the
            # distance between the two locations and continues doing that until the minimum distance is found
            min_distance = 100000000000
            min_address_name = ''  # initialize to an empty name
            if location1 == current_address:  # make sure your iteration starts at the last delivered address
                for location2 in list(map.adjacency_list):
                    if map.get_location_name(location1) == map.get_location_name(
                            location2):  # if locations are the same
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
                print('from:', location1, ' To:', min_address_name, ' Distance: ', min_distance, "Delivered Time: ",
                      check_time_first_truck(min_distance), 'Package Ids Delivered:',
                      package.package_id_to_address_list[map.get_address(min_address_name)])
                # add miles
                total_Miles = total_Miles + min_distance
    print("********************************************")
    print("-----------DONE WITH TRUCK ONE--------------")
    print("--------------------------------------------\n\n")
    # Clear List data
    map.adjacency_list.clear()
    # clear package to address list for packages that already delivered
    package.package_id_to_address_list.clear()
    # --------------------TRUCK TWO ----------------------------#
    print("-----------TRUCK TWO DETAILS-------------------\n")
    print("Truck two contains these package id's: ", truck2)
    print("--------------------------------------------")
    address_list_truck2 = []  # initialize an empty address list
    # add the HUB since we always begin at the HUB ( this will be the start)
    address_list_truck2.append('4001 South 700 East')

    for package_id in truck2:
        # add address names to our address list for truck two
        address_list_truck2.append(package.get_address(package, package_id))

    for package_id in package_list2:
        # add package_id and address to a dict, to be able to figure out which package_ids are
        # going to which address
        package.add_address_to_package_list(package.get_address(package, package_id), package_id)
    # Remove duplicate addresses from list by converting to dict and then back into list
    # Trick here is that : dicts cannot have duplicate keys
    address_list_truck2 = list(dict.fromkeys(address_list_truck2))

    print("--------------------------------------------")
    print("Truck Two Route")
    print("--------------------------------------------")
    # create address object to use Address functions
    t2 = Address()
    # add addresses uses address list developed by the package id's
    for address in address_list_truck2:
        t2.add_address(address)  # add addresses to the truck list for truck one

    # get distances between all the addresses
    # nearest neighbor algorithm
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
                    if map.get_location_name(location1) == map.get_location_name(
                            location2):  # if locations are the same
                        # don't do anything
                        continue
                    dist = map.get_weight(location1, location2)
                    if min_distance > float(dist) and len(map.adjacency_list) > 1:
                        min_distance = float(dist)

                        min_address_name = location2  # min address name is now the new location
                        i = i + 1
                        if i > 0:  # skip the first iteration to set current Address
                            # this will be used to start from last stop and continue iterating
                            current_address = location2
                # delete the start location we just iterated
                del map.adjacency_list[location1]
                # print truck route
                if bool(min_address_name):  # check if TO location is empty

                    print('from:', location1, ' To:', min_address_name, ' Distance: ', min_distance, "Delivered Time: ",
                          check_time_second_truck(min_distance), 'Package Ids Delivered:',
                          package.package_id_to_address_list[map.get_address(min_address_name)])
                    # add miles
                    total_Miles = total_Miles + min_distance

    print("--------------------------------------------")
    print("-----------DONE WITH TRUCK TWO--------------")
    print("--------------------------------------------\n\n")
    # Clear List so we can load truck three data
    map.adjacency_list.clear()
    # clear package to address list for packages that already delivered
    package.package_id_to_address_list.clear()
    # --------------------TRUCK ONE SECOND TRIP ----------------------------#
    print("-----------TRUCK ONE SECOND TRIP------------------------------------------------\n")
    print("-----------Driver Returns to Hub to deliver the rest of these-------------------\n")
    print("Truck One Starts second Trip and now contains these package id's: ", truck2)
    print("--------------------------------------------------------------------------------")
    address_list_truck3 = []  # initialize an empty address list
    # add the HUB since we always begin at the HUB ( this will be the start)
    address_list_truck3.append('4001 South 700 East')

    for package_id in truck3:
        # add address names to our address list for truck two
        address_list_truck3.append(package.get_address(package, package_id))
    for package_id in package_list3:
        # add package_id and address to a dict, to be able to figure out which package_ids are
        # going to which address
        package.add_address_to_package_list(package.get_address(package, package_id), package_id)
    # Remove duplicate addresses from list by converting to dict and then back into list
    # Trick here is that : dicts cannot have duplicate keys ;)
    address_list_truck3 = list(dict.fromkeys(address_list_truck3))

    print("--------------------------------------------")
    print("Truck One Route Part 2")
    print("--------------------------------------------")
    # create address object to use Address functions
    t3 = Address()
    # add addresses uses address list developed by the package id's
    for address in address_list_truck3:
        t3.add_address(address)

    # get distances between all the addresses
    # nearest neighbor algorithm
    # Space-time complexity is O(N)
    i = 0  # we will use i to iterate
    # set current location to the hub
    for location1 in list(map.adjacency_list):
        current_address = location1
        break

    # next neighbor algo
    while len(map.adjacency_list) > 1:  # only run until there is one element left in the list
        # so we always have a TO:location
        # loop through Vertex Objects (locations) in the adjacency list
        for location1 in list(map.adjacency_list):
            # set the min distance to a high number because it will check if the min distance is greater than the
            # distance between both locations. It runs a for loop and sets the min distance to the
            # distance between the two locations and continues doing that until the minimum distance is found
            min_distance = 100000000000
            min_address_name = ''  # initialize to an empty name
            if location1 == current_address:
                for location2 in list(
                        map.adjacency_list):  # make sure your iteration starts at the last delivered address
                    if map.get_location_name(location1) == map.get_location_name(
                            location2):  # if locations are the same
                        # don't do anything
                        continue
                    dist = map.get_weight(location1, location2)
                    if min_distance > float(dist):
                        min_distance = float(dist)

                        min_address_name = location2  # min address name is now the new location
                        i = i + 1
                        if i > 0:  # skip the first iteration to set current Address
                            # this will be used to start from last stop and continue iterating
                            current_address = location2
                # delete the start location we just iterated
                del map.adjacency_list[location1]
                if bool(min_address_name):  # check if TO location is empty
                    #  print truck route
                    #  use the check_time_first_truck method because its going to be on truck one again
                    print('from:', location1, ' To:', min_address_name, ' Distance: ', min_distance, "Delivered Time: ",
                          check_time_first_truck(min_distance), 'Package Ids Delivered:',
                          package.package_id_to_address_list[map.get_address(min_address_name)])
                    # add miles
                    total_Miles = total_Miles + min_distance
    print("----------------------------------------------------------")
    print("-----------DONE WITH TRUCK ONE (Second Trip)--------------")
    print("----------------------------------------------------------\n\n")
    # print total miles
    print("Route Completed in :", total_Miles, " Total miles")
    # Clear List
    map.adjacency_list.clear()
    # clear package to address list for packages that already delivered
    package.package_id_to_address_list.clear()

elif user_input == 2:
    decision = int(input("Press 1 to search by Package ID \n"
                         "Press 2 to view delivered packages by a set Time Range\n"))
    # Do Package ID Decision
    if decision == 1:
        user_package_id = int(input("Enter a Package ID (1-40):"))
        # we will store package details in this dict
        dict = {}
        # take user input for the start time
        st_time_str = input("Enter Starting Time in the format (HH:MM:SS): ")
        # convert to a datetime object
        st_time_DT = datetime.strptime(st_time_str, '%H:%M:%S').time()
        # take user input for the end time
        end_time_str = input("Enter Ending Time in the format (HH:MM:SS): ")
        # convert user input into DT
        end_time_DT = datetime.strptime(end_time_str, '%H:%M:%S').time()
        print("**********************************************************************")
        print('Delivery Details for Package ID:', user_package_id, ' between ', st_time_str, ' and ', end_time_str)
        print("-------------------------------------------------------------")
        # --------------------TRUCK ONE ----------------------------#
        address_list_truck1 = []  # initialize an empty address list
        # add the HUB since we always begin at the HUB ( this will be the start)
        address_list_truck1.append('4001 South 700 East')
        for package_id in truck1:
            # add address names to our address list for truck one
            address_list_truck1.append(package.get_address(package, package_id))

        for package_id in package_list1:
            # add package_id and address to a dict, to be able to figure out which package_ids are
            # going to which address
            package.add_address_to_package_list(package.get_address(package, package_id), package_id)
        # Remove duplicate addresses from list by converting to dict and then back into list
        # Trick here is that : dicts cannot have duplicate keys ;)
        address_list_truck1 = list(dict.fromkeys(address_list_truck1))

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
            first_time_list = ['8:00:00']
            # loop through Vertex Objects (locations) in the adjacency list
            for location1 in list(map.adjacency_list):
                # set the min distance to a high number because it will check if the min distance is greater than the
                # distance between both locations. It runs a for loop and sets the min distance to the
                # distance between the two locations and continues doing that until the minimum distance is found
                min_distance = 100000000000
                min_address_name = ''  # initialize to an empty name
                if location1 == current_address:  # make sure your iteration starts at the last delivered address
                    for location2 in list(map.adjacency_list):
                        if map.get_location_name(location1) == map.get_location_name(
                                location2):  # if locations are the same
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
                    current_package_id = int(package.package_id_to_address_list[map.get_address(min_address_name)][0])
                    address_ = package.search(package, current_package_id)[1]
                    city = package.search(package, current_package_id)[2]
                    state = package.search(package, current_package_id)[3]
                    zip = package.search(package, current_package_id)[4]
                    deadline = package.search(package, current_package_id)[5]
                    mass = package.search(package, current_package_id)[6]

                    # this case will be appended to the dict as a list under the values
                    case = {
                        'Package Ids:': package.package_id_to_address_list[map.get_address(min_address_name)],
                        'Delivery Address': min_address_name,
                        'City': city,
                        'State': state,
                        'Zip': zip,
                        'Deadline Time:': deadline,
                        'Mass': mass
                    }
                    # our delivery timestamp will be the key to the dict
                    entryname = datetime.strptime(str(check_time_first_truck(min_distance)), '%H:%M:%S').time()
                    # add the list to the dictionary
                    dict[entryname] = case
        # update the package status
        for d in dict:
            for pack_id in dict[d]['Package Ids:']:
                if datetime.strptime('08:00:00',
                                     '%H:%M:%S').time() <= d <= end_time_DT:  # if the delivered time is in between the start/end parameter then it was delivered
                    package.update_status(package, int(pack_id), 'Delivered')
                elif d > end_time_DT:  # if delivered time is greater than the end parameter, then its still in route
                    package.update_status(package, int(pack_id), 'In route')
                else:
                    package.update_status(package, int(pack_id), 'At the hub')  # else its at the hub

        # clear the list so that the next addresses can be loaded w the according package id's
        package.package_id_to_address_list.clear()
        dict.clear()
        # Clear List so we can load truck two data
        map.adjacency_list.clear()
        # --------------------TRUCK TWO ----------------------------#
        address_list_truck2 = []  # initialize an empty address list
        # add the HUB since we always begin at the HUB ( this will be the start)
        address_list_truck2.append('4001 South 700 East')

        for package_id in truck2:
            # add address names to our address list for truck two
            address_list_truck2.append(package.get_address(package, package_id))

        for package_id in package_list2:
            # add package_id and address to a dict, to be able to figure out which package_ids are
            # going to which address
            package.add_address_to_package_list(package.get_address(package, package_id), package_id)
        # Remove duplicate addresses from list by converting to dict and then back into list
        # Trick here is that : dicts cannot have duplicate keys
        address_list_truck2 = list(dict.fromkeys(address_list_truck2))

        # create address object to use Address functions
        t2 = Address()
        # add addresses uses address list developed by the package id's
        for address in address_list_truck2:
            t2.add_address(address)  # add addresses to the truck list for truck one

        # get distances between all the addresses
        # nearest neighbor algorithm
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
                        if map.get_location_name(location1) == map.get_location_name(
                                location2):  # if locations are the same
                            # don't do anything
                            continue
                        dist = map.get_weight(location1, location2)
                        if min_distance > float(dist) and len(map.adjacency_list) > 1:
                            min_distance = float(dist)

                            min_address_name1 = location2  # min address name is now the new location
                            i = i + 1
                            if i > 0:  # skip the first iteration to set current Address
                                # this will be used to start from last stop and continue iterating
                                current_address = location2
                    # delete the start location we just iterated
                    del map.adjacency_list[location1]
                    current_package_id = int(package.package_id_to_address_list[map.get_address(min_address_name1)][0])
                    address_ = package.search(package, current_package_id)[1]
                    city = package.search(package, current_package_id)[2]
                    state = package.search(package, current_package_id)[3]
                    zip = package.search(package, current_package_id)[4]
                    deadline = package.search(package, current_package_id)[5]
                    mass = package.search(package, current_package_id)[6]

                    # this case will be appended to the dict as a list under the values
                    case = {
                        'Package Ids:': package.package_id_to_address_list[map.get_address(min_address_name1)],
                        'Delivery Address': min_address_name1,
                        'City': city,
                        'State': state,
                        'Zip': zip,
                        'Deadline Time:': deadline,
                        'Mass': mass
                    }

                    # print truck route
                    if bool(min_address_name1):  # check if TO location is empty
                        if location1 == min_address_name1:
                            pass
                        else:
                            # our delivery timestamp will be the key to the dict
                            entryname1 = datetime.strptime(str(check_time_second_truck(min_distance)),
                                                           '%H:%M:%S').time()
                            # add the list to the dictionary
                            dict[entryname1] = case

        # update the package status
        for d in dict:
            for pack_id in dict[d]['Package Ids:']:
                if datetime.strptime('08:00:00',
                                     '%H:%M:%S').time() <= d <= end_time_DT:  # if the delivered time is in between the start/end parameter then it was delivered
                    package.update_status(package, int(pack_id), 'Delivered')
                elif d > end_time_DT:  # if delivered time is greater than the end parameter, then its still in route
                    package.update_status(package, int(pack_id), 'In route')
                elif datetime.strptime('08:00:00', '%H:%M:%S').time() == d:
                    package.update_status(package, int(pack_id), 'At the hub')  # else its at the hub

        package.package_id_to_address_list.clear()
        dict.clear()
        # Clear List so we can load truck three data
        map.adjacency_list.clear()

        # --------------------TRUCK ONE SECOND TRIP ----------------------------#
        address_list_truck3 = []  # initialize an empty address list
        # add the HUB since we always begin at the HUB ( this will be the start)
        address_list_truck3.append('4001 South 700 East')

        for package_id in truck3:
            # add address names to our address list for truck two
            address_list_truck3.append(package.get_address(package, package_id))
        for package_id in package_list3:
            # add package_id and address to a dict, to be able to figure out which package_ids are
            # going to which address
            package.add_address_to_package_list(package.get_address(package, package_id), package_id)
        # Remove duplicate addresses from list by converting to dict and then back into list
        # Trick here is that : dicts cannot have duplicate keys ;)
        address_list_truck3 = list(dict.fromkeys(address_list_truck3))
        # create address object to use Address functions
        t3 = Address()
        # add addresses uses address list developed by the package id's
        for address in address_list_truck3:
            t3.add_address(address)

        # get distances between all the addresses
        # nearest neighbor algorithm
        # Space-time complexity is O(N)
        i = 0  # we will use i to iterate
        # set current location to the hub
        for location1 in list(map.adjacency_list):
            current_address = location1
            break

        # next neighbor algo
        while len(map.adjacency_list) > 1:  # only run until there is one element left in the list
            # so we always have a TO:location
            # loop through Vertex Objects (locations) in the adjacency list

            for location1 in list(map.adjacency_list):
                # set the min distance to a high number because it will check if the min distance is greater than the
                # distance between both locations. It runs a for loop and sets the min distance to the
                # distance between the two locations and continues doing that until the minimum distance is found
                min_distance = 100000000000
                min_address_name = ''  # initialize to an empty name
                if location1 == current_address:
                    for location2 in list(
                            map.adjacency_list):  # make sure your iteration starts at the last delivered address
                        if map.get_location_name(location1) == map.get_location_name(
                                location2):  # if locations are the same
                            # don't do anything
                            continue
                        dist = map.get_weight(location1, location2)
                        if min_distance > float(dist):
                            min_distance = float(dist)

                            min_address_name2 = location2  # min address name is now the new location
                            i = i + 1
                            if i > 0:  # skip the first iteration to set current Address
                                # this will be used to start from last stop and continue iterating
                                current_address = location2
                    # delete the start location we just iterated
                    del map.adjacency_list[location1]
                    current_package_id = int(package.package_id_to_address_list[map.get_address(min_address_name2)][0])
                    address_ = package.search(package, current_package_id)[1]
                    city = package.search(package, current_package_id)[2]
                    state = package.search(package, current_package_id)[3]
                    zip = package.search(package, current_package_id)[4]
                    deadline = package.search(package, current_package_id)[5]
                    mass = package.search(package, current_package_id)[6]

                    # this case will be appended to the dict as a list under the values
                    case = {
                        'Package Ids:': package.package_id_to_address_list[map.get_address(min_address_name2)],
                        'Delivery Address': min_address_name2,
                        'City': city,
                        'State': state,
                        'Zip': zip,
                        'Deadline Time:': deadline,
                        'Mass': mass
                    }

                    # print truck route
                    if bool(min_address_name2):  # check if TO location is empty
                        if location1 == min_address_name2:
                            pass
                        else:
                            # our delivery timestamp will be the key to the dict
                            entryname1 = datetime.strptime(str(check_time_first_truck(min_distance)),
                                                           '%H:%M:%S').time()
                            # add the list to the dictionary
                            dict[entryname1] = case

        # update the package status
        for d in dict:
            for pack_id in dict[d]['Package Ids:']:
                if datetime.strptime('08:00:00',
                                     '%H:%M:%S').time() <= d <= end_time_DT:  # if the delivered time is in between the start/end parameter then it was delivered
                    package.update_status(package, int(pack_id), 'Delivered')
                elif d > end_time_DT:  # if delivered time is greater than the end parameter, then its still in route
                    package.update_status(package, int(pack_id), 'In route')
                elif datetime.strptime('08:00:00', '%H:%M:%S').time() == d:
                    package.update_status(package, int(pack_id), 'At the hub')  # else its at the hub

        print('Delivery status:', package.check_status(package, user_package_id))
        package.package_id_to_address_list.clear()
        dict.clear()
        # Clear List
        map.adjacency_list.clear()
    # do datetime range
    elif decision == 2:
        dict = {}
        # take user input for the start time
        st_time_str = input("Enter Starting Time in the format (HH:MM:SS): ")
        # convert to a datetime object
        st_time_DT = datetime.strptime(st_time_str, '%H:%M:%S').time()
        # take user input for the end time
        end_time_str = input("Enter Ending Time in the format (HH:MM:SS): ")
        # convert user input into DT
        end_time_DT = datetime.strptime(end_time_str, '%H:%M:%S').time()
        print("**********************************************************************")
        print('Delivery Details between', st_time_str, ' and ', end_time_str)
        print("**********************************************************************")
        # --------------------TRUCK ONE ----------------------------#
        address_list_truck1 = []  # initialize an empty address list
        # add the HUB since we always begin at the HUB ( this will be the start)
        address_list_truck1.append('4001 South 700 East')
        for package_id in truck1:
            # add address names to our address list for truck one
            address_list_truck1.append(package.get_address(package, package_id))

        for package_id in package_list1:
            # add package_id and address to a dict, to be able to figure out which package_ids are
            # going to which address
            package.add_address_to_package_list(package.get_address(package, package_id), package_id)
        # Remove duplicate addresses from list by converting to dict and then back into list
        # Trick here is that : dicts cannot have duplicate keys ;)
        address_list_truck1 = list(dict.fromkeys(address_list_truck1))

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
            first_time_list = ['8:00:00']
            # loop through Vertex Objects (locations) in the adjacency list
            for location1 in list(map.adjacency_list):
                # set the min distance to a high number because it will check if the min distance is greater than the
                # distance between both locations. It runs a for loop and sets the min distance to the
                # distance between the two locations and continues doing that until the minimum distance is found
                min_distance = 100000000000
                min_address_name = ''  # initialize to an empty name
                if location1 == current_address:  # make sure your iteration starts at the last delivered address
                    for location2 in list(map.adjacency_list):
                        if map.get_location_name(location1) == map.get_location_name(
                                location2):  # if locations are the same
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
                    current_package_id = int(package.package_id_to_address_list[map.get_address(min_address_name)][0])
                    address_ = package.search(package, current_package_id)[1]
                    city = package.search(package, current_package_id)[2]
                    state = package.search(package, current_package_id)[3]
                    zip = package.search(package, current_package_id)[4]
                    deadline = package.search(package, current_package_id)[5]
                    mass = package.search(package, current_package_id)[6]

                    # this case will be appended to the dict as a list under the values
                    case = {
                        'Package Ids:': package.package_id_to_address_list[map.get_address(min_address_name)],
                        'Delivery Address': min_address_name,
                        'City': city,
                        'State': state,
                        'Zip': zip,
                        'Deadline Time:': deadline,
                        'Mass': mass
                    }
                    # our delivery timestamp will be the key to the dict
                    entryname = datetime.strptime(str(check_time_first_truck(min_distance)), '%H:%M:%S').time()
                    # add the list to the dictionary
                    dict[entryname] = case
        # update the package status
        for d in dict:
            for pack_id in dict[d]['Package Ids:']:
                if datetime.strptime('08:00:00',
                                     '%H:%M:%S').time() <= d <= end_time_DT:  # if the delivered time is in between the start/end parameter then it was delivered
                    package.update_status(package, int(pack_id), 'Delivered')
                elif d > end_time_DT:  # if delivered time is greater than the end parameter, then its still in route
                    package.update_status(package, int(pack_id), 'In route')
                else:
                    package.update_status(package, int(pack_id), 'At the hub')  # else its at the hub
        # print packages delivered within the start and end times defined by the user
        for d in dict:
            if st_time_DT <= d <= end_time_DT:
                print(dict[d], 'Delivered Time: ', d)
                print("---------------------------------------")
        # clear the list so that the next addresses can be loaded w the according package id's
        package.package_id_to_address_list.clear()
        dict.clear()
        # Clear List so we can load truck two data
        map.adjacency_list.clear()

        # --------------------TRUCK TWO ----------------------------#
        address_list_truck2 = []  # initialize an empty address list
        # add the HUB since we always begin at the HUB ( this will be the start)
        address_list_truck2.append('4001 South 700 East')

        for package_id in truck2:
            # add address names to our address list for truck two
            address_list_truck2.append(package.get_address(package, package_id))

        for package_id in package_list2:
            # add package_id and address to a dict, to be able to figure out which package_ids are
            # going to which address
            package.add_address_to_package_list(package.get_address(package, package_id), package_id)
        # Remove duplicate addresses from list by converting to dict and then back into list
        # Trick here is that : dicts cannot have duplicate keys
        address_list_truck2 = list(dict.fromkeys(address_list_truck2))

        # create address object to use Address functions
        t2 = Address()
        # add addresses uses address list developed by the package id's
        for address in address_list_truck2:
            t2.add_address(address)  # add addresses to the truck list for truck one

        # get distances between all the addresses
        # nearest neighbor algorithm
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
                        if map.get_location_name(location1) == map.get_location_name(
                                location2):  # if locations are the same
                            # don't do anything
                            continue
                        dist = map.get_weight(location1, location2)
                        if min_distance > float(dist) and len(map.adjacency_list) > 1:
                            min_distance = float(dist)

                            min_address_name1 = location2  # min address name is now the new location
                            i = i + 1
                            if i > 0:  # skip the first iteration to set current Address
                                # this will be used to start from last stop and continue iterating
                                current_address = location2
                    # delete the start location we just iterated
                    del map.adjacency_list[location1]
                    current_package_id = int(package.package_id_to_address_list[map.get_address(min_address_name1)][0])
                    address_ = package.search(package, current_package_id)[1]
                    city = package.search(package, current_package_id)[2]
                    state = package.search(package, current_package_id)[3]
                    zip = package.search(package, current_package_id)[4]
                    deadline = package.search(package, current_package_id)[5]
                    mass = package.search(package, current_package_id)[6]

                    # this case will be appended to the dict as a list under the values
                    case = {
                        'Package Ids:': package.package_id_to_address_list[map.get_address(min_address_name1)],
                        'Delivery Address': min_address_name1,
                        'City': city,
                        'State': state,
                        'Zip': zip,
                        'Deadline Time:': deadline,
                        'Mass': mass
                    }

                    # print truck route
                    if bool(min_address_name1):  # check if TO location is empty
                        if location1 == min_address_name1:
                            pass
                        else:
                            # our delivery timestamp will be the key to the dict
                            entryname1 = datetime.strptime(str(check_time_second_truck(min_distance)),
                                                           '%H:%M:%S').time()
                            # add the list to the dictionary
                            dict[entryname1] = case

        # update the package status
        for d in dict:
            for pack_id in dict[d]['Package Ids:']:
                if datetime.strptime('08:00:00',
                                     '%H:%M:%S').time() <= d <= end_time_DT:  # if the delivered time is in between the start/end parameter then it was delivered
                    package.update_status(package, int(pack_id), 'Delivered')
                elif d > end_time_DT:  # if delivered time is greater than the end parameter, then its still in route
                    package.update_status(package, int(pack_id), 'In route')
                elif datetime.strptime('08:00:00', '%H:%M:%S').time() == d:
                    package.update_status(package, int(pack_id), 'At the hub')  # else its at the hub
        # print packages delivered within the start and end times defined by the user
        for d in dict:
            if st_time_DT <= d <= end_time_DT:
                print(dict[d], 'Delivered Time: ', d)
                print("---------------------------------------")

        package.package_id_to_address_list.clear()
        dict.clear()
        # Clear List so we can load truck three data
        map.adjacency_list.clear()

        # --------------------TRUCK ONE SECOND TRIP ----------------------------#
        address_list_truck3 = []  # initialize an empty address list
        # add the HUB since we always begin at the HUB ( this will be the start)
        address_list_truck3.append('4001 South 700 East')

        for package_id in truck3:
            # add address names to our address list for truck two
            address_list_truck3.append(package.get_address(package, package_id))
        for package_id in package_list3:
            # add package_id and address to a dict, to be able to figure out which package_ids are
            # going to which address
            package.add_address_to_package_list(package.get_address(package, package_id), package_id)
        # Remove duplicate addresses from list by converting to dict and then back into list
        # Trick here is that : dicts cannot have duplicate keys ;)
        address_list_truck3 = list(dict.fromkeys(address_list_truck3))
        # create address object to use Address functions
        t3 = Address()
        # add addresses uses address list developed by the package id's
        for address in address_list_truck3:
            t3.add_address(address)

        # get distances between all the addresses
        # nearest neighbor algorithm
        # Space-time complexity is O(N)
        i = 0  # we will use i to iterate
        # set current location to the hub
        for location1 in list(map.adjacency_list):
            current_address = location1
            break

        # next neighbor algo
        while len(map.adjacency_list) > 1:  # only run until there is one element left in the list
            # so we always have a TO:location
            # loop through Vertex Objects (locations) in the adjacency list

            for location1 in list(map.adjacency_list):
                # set the min distance to a high number because it will check if the min distance is greater than the
                # distance between both locations. It runs a for loop and sets the min distance to the
                # distance between the two locations and continues doing that until the minimum distance is found
                min_distance = 100000000000
                min_address_name = ''  # initialize to an empty name
                if location1 == current_address:
                    for location2 in list(
                            map.adjacency_list):  # make sure your iteration starts at the last delivered address
                        if map.get_location_name(location1) == map.get_location_name(
                                location2):  # if locations are the same
                            # don't do anything
                            continue
                        dist = map.get_weight(location1, location2)
                        if min_distance > float(dist):
                            min_distance = float(dist)

                            min_address_name2 = location2  # min address name is now the new location
                            i = i + 1
                            if i > 0:  # skip the first iteration to set current Address
                                # this will be used to start from last stop and continue iterating
                                current_address = location2
                    # delete the start location we just iterated
                    del map.adjacency_list[location1]
                    current_package_id = int(package.package_id_to_address_list[map.get_address(min_address_name2)][0])
                    address_ = package.search(package, current_package_id)[1]
                    city = package.search(package, current_package_id)[2]
                    state = package.search(package, current_package_id)[3]
                    zip = package.search(package, current_package_id)[4]
                    deadline = package.search(package, current_package_id)[5]
                    mass = package.search(package, current_package_id)[6]

                    # this case will be appended to the dict as a list under the values
                    case = {
                        'Package Ids:': package.package_id_to_address_list[map.get_address(min_address_name2)],
                        'Delivery Address': min_address_name2,
                        'City': city,
                        'State': state,
                        'Zip': zip,
                        'Deadline Time:': deadline,
                        'Mass': mass
                    }

                    # print truck route
                    if bool(min_address_name2):  # check if TO location is empty
                        if location1 == min_address_name2:
                            pass
                        else:
                            # our delivery timestamp will be the key to the dict
                            entryname1 = datetime.strptime(str(check_time_first_truck(min_distance)),
                                                           '%H:%M:%S').time()
                            # add the list to the dictionary
                            dict[entryname1] = case
        # print packages delivered within the start and end times defined by the user
        for d in dict:
            if st_time_DT <= d <= end_time_DT:
                print(dict[d], 'Delivered Time: ', d)
                print("---------------------------------------")
elif user_input == 3:
    dict = {}
    # take user input for the start time
    st_time_str = input("Enter Starting Time in the format (HH:MM:SS): ")
    # convert to a datetime object
    st_time_DT = datetime.strptime(st_time_str, '%H:%M:%S').time()
    # take user input for the end time
    end_time_str = input("Enter Ending Time in the format (HH:MM:SS): ")
    # convert user input into DT
    end_time_DT = datetime.strptime(end_time_str, '%H:%M:%S').time()
    print("**********************************************************************")
    print('Delivery Details for all Package IDs between ', st_time_str, ' and ', end_time_str)
    print("-------------------------------------------------------------")
    # --------------------TRUCK ONE ----------------------------#
    address_list_truck1 = []  # initialize an empty address list
    # add the HUB since we always begin at the HUB ( this will be the start)
    address_list_truck1.append('4001 South 700 East')
    for package_id in truck1:
        # add address names to our address list for truck one
        address_list_truck1.append(package.get_address(package, package_id))
    for package_id in package_list1:
        # add package_id and address to a dict, to be able to figure out which package_ids are
        # going to which address
        package.add_address_to_package_list(package.get_address(package, package_id), package_id)
    # Remove duplicate addresses from list by converting to dict and then back into list
    # Trick here is that : dicts cannot have duplicate keys ;)
    address_list_truck1 = list(dict.fromkeys(address_list_truck1))
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
    # Set total miles equal to zero and add miles each route
    total_Miles = 0
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
                    if map.get_location_name(location1) == map.get_location_name(
                            location2):  # if locations are the same
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
                current_package_id = int(package.package_id_to_address_list[map.get_address(min_address_name)][0])
                address_ = package.search(package, current_package_id)[1]
                city = package.search(package, current_package_id)[2]
                state = package.search(package, current_package_id)[3]
                zip = package.search(package, current_package_id)[4]
                deadline = package.search(package, current_package_id)[5]
                mass = package.search(package, current_package_id)[6]

                # this case will be appended to the dict as a list under the values
                case = {
                    'Package Ids:': package.package_id_to_address_list[map.get_address(min_address_name)],
                    'Delivery Address': min_address_name,
                    'City': city,
                    'State': state,
                    'Zip': zip,
                    'Deadline Time:': deadline,
                    'Mass': mass
                }
                # our delivery timestamp will be the key to the dict
                entryname = datetime.strptime(str(check_time_first_truck(min_distance)), '%H:%M:%S').time()
                # add the list to the dictionary
                dict[entryname] = case
    # update the package status
    for d in dict:
        for pack_id in dict[d]['Package Ids:']:
            if datetime.strptime('08:00:00',
                                 '%H:%M:%S').time() <= d <= end_time_DT:  # if the delivered time is in between the start/end parameter then it was delivered
                package.update_status(package, int(pack_id), 'Delivered')
            elif d > end_time_DT:  # if delivered time is greater than the end parameter, then its still in route
                package.update_status(package, int(pack_id), 'In route')
            elif datetime.strptime('08:00:00', '%H:%M:%S').time() == d:
                package.update_status(package, int(pack_id), 'At the hub')  # else its at the hub

            print('Package IDs: ', pack_id, '-->Status:', package.check_status(package, pack_id),
                  '-->Time Package will be/is delivered:', d)

    # Clear List data
    map.adjacency_list.clear()
    # clear package to address list for packages that already delivered
    package.package_id_to_address_list.clear()
    # clear package dict
    dict.clear()
    # --------------------TRUCK TWO ----------------------------#
    address_list_truck2 = []  # initialize an empty address list
    # add the HUB since we always begin at the HUB ( this will be the start)
    address_list_truck2.append('4001 South 700 East')

    for package_id in truck2:
        # add address names to our address list for truck two
        address_list_truck2.append(package.get_address(package, package_id))

    for package_id in package_list2:
        # add package_id and address to a dict, to be able to figure out which package_ids are
        # going to which address
        package.add_address_to_package_list(package.get_address(package, package_id), package_id)
    # Remove duplicate addresses from list by converting to dict and then back into list
    # Trick here is that : dicts cannot have duplicate keys
    address_list_truck2 = list(dict.fromkeys(address_list_truck2))

    # create address object to use Address functions
    t2 = Address()
    # add addresses uses address list developed by the package id's
    for address in address_list_truck2:
        t2.add_address(address)  # add addresses to the truck list for truck one

    # get distances between all the addresses
    # nearest neighbor algorithm
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
            # min_address_name1 = Vertex(8, 'Salt Lake City Ottinger Hall', '233 Canyon Rd')
            min_address_name = ''  # initialize to an empty name
            if location1 == current_address:  # make sure your iteration starts at the last delivered address
                for location2 in list(map.adjacency_list):
                    if map.get_location_name(location1) == map.get_location_name(
                            location2):  # if locations are the same
                        # don't do anything
                        continue
                    dist = map.get_weight(location1, location2)
                    if min_distance > float(dist) and len(map.adjacency_list) > 1:
                        min_distance = float(dist)

                        min_address_name1 = location2  # min address name is now the new location
                        i = i + 1
                        if i > 0:  # skip the first iteration to set current Address
                            # this will be used to start from last stop and continue iterating
                            current_address = location2
                # delete the start location we just iterated
                del map.adjacency_list[location1]
                current_package_id = int(package.package_id_to_address_list[map.get_address(min_address_name1)][0])
                address_ = package.search(package, current_package_id)[1]
                city = package.search(package, current_package_id)[2]
                state = package.search(package, current_package_id)[3]
                zip = package.search(package, current_package_id)[4]
                deadline = package.search(package, current_package_id)[5]
                mass = package.search(package, current_package_id)[6]

                # this case will be appended to the dict as a list under the values
                case = {
                    'Package Ids:': package.package_id_to_address_list[map.get_address(min_address_name1)],
                    'Delivery Address': min_address_name1,
                    'City': city,
                    'State': state,
                    'Zip': zip,
                    'Deadline Time:': deadline,
                    'Mass': mass
                }

                # print truck route
                if bool(min_address_name1):  # check if TO location is empty
                    if location1 == min_address_name1:
                        pass
                    else:
                        # our delivery timestamp will be the key to the dict
                        entryname1 = datetime.strptime(str(check_time_second_truck(min_distance)), '%H:%M:%S').time()
                        # add the list to the dictionary
                        dict[entryname1] = case

    # update the package status
    for d in dict:
        for pack_id in dict[d]['Package Ids:']:
            if datetime.strptime('08:00:00',
                                 '%H:%M:%S').time() <= d <= end_time_DT:  # if the delivered time is in between the start/end parameter then it was delivered
                package.update_status(package, int(pack_id), 'Delivered')
            elif d > end_time_DT:  # if delivered time is greater than the end parameter, then its still in route
                package.update_status(package, int(pack_id), 'In route')
            elif datetime.strptime('08:00:00', '%H:%M:%S').time() == d:
                package.update_status(package, int(pack_id), 'At the hub')  # else its at the hub

            print('Package IDs: ', pack_id, '-->Status:', package.check_status(package, pack_id),
                  '-->Time Package will be/is delivered:', d)

    package.package_id_to_address_list.clear()
    dict.clear()
    # Clear List so we can load truck three data
    map.adjacency_list.clear()

    # --------------------TRUCK ONE SECOND TRIP ----------------------------#
    address_list_truck3 = []  # initialize an empty address list
    # add the HUB since we always begin at the HUB ( this will be the start)
    address_list_truck3.append('4001 South 700 East')

    for package_id in truck3:
        # add address names to our address list for truck two
        address_list_truck3.append(package.get_address(package, package_id))
    for package_id in package_list3:
        # add package_id and address to a dict, to be able to figure out which package_ids are
        # going to which address
        package.add_address_to_package_list(package.get_address(package, package_id), package_id)
    # Remove duplicate addresses from list by converting to dict and then back into list
    # Trick here is that : dicts cannot have duplicate keys ;)
    address_list_truck3 = list(dict.fromkeys(address_list_truck3))
    # create address object to use Address functions
    t3 = Address()
    # add addresses uses address list developed by the package id's
    for address in address_list_truck3:
        t3.add_address(address)

    # get distances between all the addresses
    # nearest neighbor algorithm
    # Space-time complexity is O(N)
    i = 0  # we will use i to iterate
    # set current location to the hub
    for location1 in list(map.adjacency_list):
        current_address = location1
        break

    # next neighbor algo
    while len(map.adjacency_list) > 1:  # only run until there is one element left in the list
        # so we always have a TO:location
        # loop through Vertex Objects (locations) in the adjacency list

        for location1 in list(map.adjacency_list):
            # set the min distance to a high number because it will check if the min distance is greater than the
            # distance between both locations. It runs a for loop and sets the min distance to the
            # distance between the two locations and continues doing that until the minimum distance is found
            min_distance = 100000000000
            min_address_name = ''  # initialize to an empty name
            if location1 == current_address:
                for location2 in list(
                        map.adjacency_list):  # make sure your iteration starts at the last delivered address
                    if map.get_location_name(location1) == map.get_location_name(
                            location2):  # if locations are the same
                        # don't do anything
                        continue
                    dist = map.get_weight(location1, location2)
                    if min_distance > float(dist):
                        min_distance = float(dist)

                        min_address_name2 = location2  # min address name is now the new location
                        i = i + 1
                        if i > 0:  # skip the first iteration to set current Address
                            # this will be used to start from last stop and continue iterating
                            current_address = location2

                # delete the start location we just iterated
                del map.adjacency_list[location1]
                current_package_id = int(package.package_id_to_address_list[map.get_address(min_address_name2)][0])
                address_ = package.search(package, current_package_id)[1]
                city = package.search(package, current_package_id)[2]
                state = package.search(package, current_package_id)[3]
                zip = package.search(package, current_package_id)[4]
                deadline = package.search(package, current_package_id)[5]
                mass = package.search(package, current_package_id)[6]

                # this case will be appended to the dict as a list under the values
                case = {
                    'Package Ids:': package.package_id_to_address_list[map.get_address(min_address_name2)],
                    'Delivery Address': min_address_name2,
                    'City': city,
                    'State': state,
                    'Zip': zip,
                    'Deadline Time:': deadline,
                    'Mass': mass
                }
                if location1 != min_address_name2:
                    entryname1 = datetime.strptime(str(check_time_first_truck(min_distance)), '%H:%M:%S').time()
                    dict[entryname1] = case

    # print packages delivered within the start and end times defined by the user
    # update the package status

    for d in dict:
        for pack_id in dict[d]['Package Ids:']:
            if datetime.strptime('08:00:00',
                                 '%H:%M:%S').time() <= d <= end_time_DT:  # if the delivered time is in between the start/end parameter then it was delivered
                package.update_status(package, int(pack_id), 'Delivered')
            elif d > end_time_DT:  # if delivered time is greater than the end parameter, then its still in route
                package.update_status(package, int(pack_id), 'In route')
            elif datetime.strptime('08:00:00', '%H:%M:%S').time() == d:
                package.update_status(package, int(pack_id), 'At the hub')  # else its at the hub
            print('Package IDs: ', pack_id, '-->Status:', package.check_status(package, pack_id),
                  '-->Time Package will be/is delivered:', d)
    map.adjacency_list.clear()
