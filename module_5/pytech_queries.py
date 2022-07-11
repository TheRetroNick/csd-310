# Assingment 5.3 - pytech_queries

import pymongo

# call the server
client = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.cbez6.mongodb.net/?retryWrites=true&w=majority')

# select the database that you want to access
db = client['pytech']


# query all 
doc = db.students.find({})
# query which student you want to find
doc2 = db.students.find_one({'student_id': '1008'})

# output both queries
print(doc)
print(doc2)
