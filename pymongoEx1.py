import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#
# mydb = myclient["mydatabase"]
#
# print(myclient.list_database_names())

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]

# mydict = { "name": "John", "address": "Highway 37" }
#
# x = mycol.insert_one(mydict)
#
# mydict = { "name": "Peter", "address": "Lowstreet 27" }
#
# x = mycol.insert_one(mydict)
#
# print(x.inserted_id)

# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]
#
# x = mycol.insert_many(mylist)
#
# print(x.inserted_ids)

# x = mycol.find_one()
#
# print(x)
# for x in mycol.find():
#   print(x)
#
# for x in mycol.find({}, {"address": 0}):
#       print(x)

# myquery = { "address": "Park Lane 38" }
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#   print(x)
#
# myquery = { "address": { "$gt": "S" } }
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#   print(x)

# mydoc = mycol.find().sort("name")
#
# for x in mydoc:
#   print(x)

mydoc = mycol.find().sort("name", -1)
for x in mydoc:
  print(x)