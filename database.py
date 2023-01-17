from pymongo import MongoClient


DB = "mongodb+srv://Onkar18:Onkar@cluster0.omcwrve.mongodb.net/"
cluster = MongoClient(DB)
dbs = cluster.list_database_names()
print(dbs)
ParkApp = cluster.ParkApp

CarInfo = ParkApp.CarInfo

# CarInfo.insert_one({"Name": "Omkar"})
# coll = ParkApp.list_collection_names()
# CarInfo.drop()
# print(coll)
# CarInfo.drop()

# a = set()
# a = {1, 2, 3, 4}
# ax=[]
# print(a)
# for  i in range(len(a)):
#     ax.append(True)
# az = dict(zip(a, ax))
# print(az)
