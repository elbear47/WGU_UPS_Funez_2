import csv

package_file = open('./files/WGU_Package_Info.csv', 'r', encoding='utf-8-sig')  # open csv
reader = csv.reader(package_file)  # reader will be our csv reader


# HashTable class called Package
class Package:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=41):  # 40 distinct package id's so make the capacity 0-40
        self.package_id_to_address_list = {}
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(0, initial_capacity):
            # append to the table
            self.table.append([])

    # lookup for all package hashtable details by package id
    def search(self, bucket, key):
        bucket = self.table
        if len(bucket[key]) != 0:
            return bucket[key]
        else:
            return None

    # Inserts a new item into the direct access hashtable.
    def insert(self, bucket, item):
        # get the bucket list where this item will go.
        bucket = self.table
        bucket[int(item[0])] = item

        # insert the item to the end of the bucket list.
        bucket.append(item)

    # this will update the package status
    def update_status(self, bucket, package_id, status_to_update):
        # index 7 is the status in the csv file
        bucket.table[package_id][7] = str(status_to_update)

    # this will check if the status is at the hub, in route, or delivered
    def check_status(self, bucket, package_id):
        return bucket.table[package_id][7]

    # this function automatically loads the package data into the hashtable
    def load_csv_data(self, c):
        for row in reader:
            c.insert(c.table, row)

    # get address name by the package id
    def get_address(self, c, key):
        # address name is index 1
        return c.table[key][1]  # return address name from hashtable

    # get package_id by the address name
    def get_package_id(self, package_to_address_dict, address):
        return package_to_address_dict[str(address)]

    # we will use this function to create a package_id to address dictionary
    def add_address_to_package_list(self, address, package_id):
        # if there is already package id for that address, append it, don't replace it
        if address in self.package_id_to_address_list.keys():
            self.package_id_to_address_list[address].append(int(package_id))
        # else, create a list item for it and append the package id to the dict
        else:
            self.package_id_to_address_list[address] = list()
            self.package_id_to_address_list[address].append(int(package_id))

    # Overloaded string conversion method to create a string
    # representation of the entire hash table. Each bucket is shown
    # as a pointer to a list object.
    def __str__(self):
        index = 0
        s = "   --------\n"
        for bucket in self.table:
            print(index, bucket)
            index += 1
        s += "   --------"
        return s
