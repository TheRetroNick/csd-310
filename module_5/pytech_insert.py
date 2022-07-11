# Assignment 5.3 - pytech_insert

import pymongo

# call the server
client = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.cbez6.mongodb.net/?retryWrites=true&w=majority')
# select the databse you want
db = client['pytech']

# mycol = db['students'] If you want to put all 3 students in at once, but not using it here 

# add each of the 3 new students to the database. Make sure you use 'students'
fred_student_id = db.students.insert_one({'student_id': '1007', 'firstName': 'Fred', 'lastName': 'Flintstone'}).inserted_id
barney_student_id = db.students.insert_one({'student_id': '1008', 'firstName': 'Farney', 'lastName': 'Rubble'}).inserted_id
dino_student_id = db.students.insert_one({'student_id': '1009', 'firstName': 'Dino', 'lastName': 'theDinosaur'}).inserted_id
