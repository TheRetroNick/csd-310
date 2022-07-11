# Assingment 6.2 - pytech_update

import pymongo

# call the server
client = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.cbez6.mongodb.net/?retryWrites=true&w=majority')

# select the database that you want to access
db = client['pytech']

# select the student ID info you want to update. $set will add the field and value if the field is not already present to be updated.
db.students.update_one({'student_id': '1007'}, {'$set': {"lastName": "Smith"}})
