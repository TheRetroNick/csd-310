# Assignment 5.3 - pytech_insert

import pymongo

# call the server
client = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.cbez6.mongodb.net/?retryWrites=true&w=majority')
# select the databse you want
db = client['pytech']

# mycol = db['students'] If you want to put all 3 students in at once, but not using it here 

# add each of the 3 new students to the database. Make sure you use 'students'
db.students.insert_one({'student_id': '1007', 'firstName': 'fred'})
db.students.insert_one({'student_id': '1008', 'firstName': 'barney'})
db.students.insert_one({'student_id': '1009', 'firstName': 'dino'})
