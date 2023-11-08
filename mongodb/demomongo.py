import pymongo

# create database

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["mydataase"]

print()