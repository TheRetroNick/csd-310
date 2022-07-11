# Assingment 6.2 - pytech_queries

import pymongo

# call the server
client = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.cbez6.mongodb.net/?retryWrites=true&w=majority')

# select the database that you want to access
db = client['pytech']

# 
db.students.update_one({'student_id': '1007'}, {'$set': {"lastName": "Smith"}})
