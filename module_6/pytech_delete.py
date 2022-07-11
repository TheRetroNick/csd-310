# Assingment 6.3 - pytech_delete

import pymongo

# call the server
client = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.cbez6.mongodb.net/?retryWrites=true&w=majority')

# select the database that you want to access
db = client['pytech']

# Call the find() method and display the results to the terminal window.
doc = db.students.find({})
print(doc) 

# Call the insert_one() method and Insert a new document into the pytech collection with student_id 1010.
wilma_student_id = db.students.insert_one({'student_id': '1010', 'firstName': 'Wilma', 'lastName': 'Flintstone'}).inserted_id

# Call the find_one() method and display the results to the terminal window.
doc2 = db.students.find_one({'student_id': '1010'})
print(doc2)

# Call the delete_one() method by student_id 1010.
db.students.delete_one({'student_id': '1010'})

# Call the find() method and display the results to the terminal window.
doc = db.students.find({})
print(doc) 
