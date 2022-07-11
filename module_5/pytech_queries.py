# Assingment 5.3 - pytech_queries

import pymongo

# call the server
client = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.cbez6.mongodb.net/?retryWrites=true&w=majority')

# select the database that you want to access
db = client['pytech']

# query which student you want to find
doc = db.students.find_one({'student_id': '1008'})

# output the query
print(doc)
