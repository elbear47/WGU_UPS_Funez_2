import csv

package_file = open('./files/WGU_Package_Info.csv', 'r', encoding='utf-8-sig')
reader = csv.reader(package_file)


# HashTable class using chaining.
class Package:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=41):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(0, initial_capacity):
            self.table.append([])

    def search(self, bucket, key):
        bucket = self.table
        if len(bucket[key]) != 0:
            return bucket[key]
        else:
            return None

    # Inserts a new item into the hashtable.
    def insert(self, bucket, item):
        # get the bucket list where this item will go.
        # bucket = hash(item) % len(self.table)
        bucket = self.table
        # bucket = int(item[0])
        # bucket_list = self.table[bucket]
        bucket[int(item[0])] = item

        # insert the item to the end of the bucket list.
        bucket.append(item)

    # this will update the package status
    def update_status(self, key, index, newvalue):
        # index 7 is the status in the csv file
        self.table[key][7] = newvalue

    def load_csv_data(self, c):
        for row in reader:
            c.insert(c.table, row)

    def get_address(self, c, key):
        return c.table[key][1]

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

#test main
#c = Package()

#for row in reader:
#    c.insert(c.table, row)

# print(package_id_list[0])
# print(range(len(package_id_list)))
# we can access information in the hash table by referencing the index
#print(c.table[1])
#print(c.table[1][7])
#c.update_status(1, 0, 'getting delivered')
#print(c.table[1][7])
#print(c.search(c.table, 1))
# print(id)
