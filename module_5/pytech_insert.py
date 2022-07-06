

db.movies.insertOne(
  {
    title: "The Favourite",
    genres: [ "Drama", "History" ],
    runtime: 121,
    rated: "R",
    year: 2018,
    directors: [ "Yorgos Lanthimos" ],
    cast: [ "Olivia Colman", "Emma Stone", "Rachel Weisz" ],
    type: "movie"
  }
)


fred = {
 “first_name”: “Fred”
}
 
fred_student_id = students.insert_one(fred).inserted_id
 
print(fred_student_id)
 
MongoDB: find() Example 
docs = db.collection_name.find({})
 
for doc in docs:
 print(doc)
 
MongoDB: find_one() Example 
doc = db.collection_name.find_one({“student_id”: “1007”})
 
print(doc[“student_id”])
