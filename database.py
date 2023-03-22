from pymongo import MongoClient


DB = "mongodb+srv://Onkar18:Onkar@cluster0.omcwrve.mongodb.net/"
cluster = MongoClient(DB)
dbs = cluster.list_database_names()
print(dbs)

ParkApp = cluster.ParkApp  # Save Database Name

CarInfo = ParkApp.CarInfo # Save Collection Name
CarInfo2 = ParkApp.CarInfo2 # Save Collection Name
CarInfo3 = ParkApp.CarInfo3 # Save Collection Name

