# import pymongo

"""
# connection with my client
myclient = pymongo.MongoClient("mongodb://localhost:27017")

# create database
# remember: In MongoDB, a database is not created until it gets content.
mydb = myclient["mydb"]

# print all databases
# print(myclient.list_database_names())

# remember: In MongoDB, a collection is not created until it gets content!
mycol = mydb["customers"]

# insert data
# "_id": 1 <-- if I use it, I can controll the _ids
my_data_list = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"}
]

# insert_many or insert_one
insert_data = mycol.insert_many(my_data_list)

# print list of the _id values of the inserted data
print(insert_data.inserted_ids)

# find_one: returns the first ocurrence
find_one = mycol.find_one()
print(find_one)

# find: returns all ocurrences
for x in mycol.find():
    print(x)

# return only some fields
for x in mycol.find({}, {"_id": 0, "name": 1}):  # return only the name, not the _ids
    print(x)

# query
myquery = {"name": "Amy"}  # return the customer data with that name

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# advanced query
myadvancedquery = {"name": {"$gt": "S"}}  # find costumers where the name starts with the letter "S" or higher.

mydoc = mycol.find(myadvancedquery)

for x in mydoc:
    print(x)

# sort the result
mydoc = mycol.find().sort("name")

for x in mydoc:
    print(x)

# delete_one or delete_many
mycol.delete_one(myquery)  # delete the customer data with that name

x = mycol.delete_many(myadvancedquery)  # delete costumers where the name starts with the letter "S" or higher.
print(x.deleted_count, " documents deleted")

# drop collection = delete table
# mycol.drop()

# update
# my_update_query = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Canyon 123" } }
# mycol.update_one(myquery, newvalues)
"""