import csv


# create a package class which will store our package items
class Package:
    def __init__(self):
        self.package_id_list = {}
        self.package_info_list = {}

    def add_package(self, package_id):
        self.package_id_list[package_id] = []


package_file = open('./files/WGU_Package_Info.csv', 'r', encoding='utf-8-sig')
reader = csv.reader(package_file)

p = Package()  # create a package object
package_info = []  # create list to store package info
for row in reader:
    p.add_package(row[0])  # add this to the dict.keys to access list of into


print(p.package_id_list)