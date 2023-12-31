from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(
        "<h1>Hello and welcome to my first <u>Django App</u> project!</h1>"
    )


import pymongo

client = pymongo.MongoClient("YOUR_CONNECTION_STRING")

# Define Db Name
dbname = client["admin"]

# Define Collection
collection = dbname["mascot"]

mascot_1 = {"name": "Sammy", "type": "Shark"}

collection.insert_one(mascot_1)

mascot_details = collection.find({})

for r in mascot_details:
    print(r["name"])
