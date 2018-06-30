//Database -> Collection -> Documents

//Will create a database mydb with below command if not exist otherwise will use the existin gone
use mydb
//db

//To shows all the available database
show dbs

//Insertion
db.mycollection.insert({'First_Name' : 'Shubham'})

// Drop a database
db.dropDatabase()

use mydb
db.createCollection("myCollection")
show collections
db.collection2.insert({'First_Name' : 'Shubham'}) 
db.myCollection.drop()


//insert documents inside collection
use school
db.students.insert(
	{'studentno':1,
	 'name':'Shubham',
	 'age' : 20,
	 'Hobby' : 'Cricket'	
	})

db.students.insert(
	[{'studentno':10,
	 'name':'pooja',
	 'age' : 29,
	 'Hobby' : 'gosssip',
	 'gender'  : 'FeMale'	
	},
	{'studentno':11,
	 'name':'Padam',
	 'age' : 29,
	 'Hobby' : 'Comics',
	 'gender'  : 'Male'		
	},
	{'studentno':12,
	 'name':'Swati',
	 'age' : 24,
	 'Hobby' : 'Cooking',
	 'gender'  : 'FeMale'		
	}
	])

show collections

//How to query document data
db.students.find().pretty()
db.students.findOne()
db.students.find({"studentno":2})
db.students.find({"age":{$ne:25}})

//$lt,lte,gt,gte,ne

//Query based on two queries
db.students.find({"name":"Swati",'age':24})

//OR Condition
db.students.find({$or:[{"name":"Swati",'age':24}]})


//And condition between first normal and second OR condition(for and dont need to use AND keyword)
db.students.find(
{
  "name":"Swati",$or:[{'age':24},{"name":"Swati"}]
  
}
)

db.students.find()

//Update the results using 'set' keyword

db.students.update(
{'name' : 'Swati'},{$set:{'name' : 'Ravi'}}
)

db.students.update({'name':'Ravi'},{$set:{'age' : 25}})

//Update multiple documents

db.students.update(
{'age' : 25},{$set:{'Hobby' : 'Hockey'}},{multi : true}
)

db.students.find()

//Another way to update (Save)
//It will update the document based on the name given below and if no document founnd , then it will insert a new collection
//with the information gievn below
db.students.save(
{'name' : 'OM','Hobby' : 'Boo Hockey','age' : 27}
)

db.students.find()

//Delete/Remove a Document from MongoDb
db.students.remove({"_id" : ObjectId("596a85c5ca53e9c9da55f80d")})

//Another way of removing the Document (Here 1 wil delete only one document even the condition matching many fields)
db.students.remove({"age" : 20},1)


db.students.find()
//MongoDb Projection (selecting only necessary data like only names of all the students only)

//1 for displaying only names and 0 for excluding that field if coming as _id will come always
db.students.find({},{'name' : 1,"_id"  :0})


//limit(will limit the no of documents to be displayed), sort and skip (will skip the documents number specified inside bracket)

use mydbs
db.students.find({},{'name' : 1,'age' : 1,'_id' :0}).limit(2)
db.students.find({},{'name' : 1,'age' : 1,'_id' :0}).skip(2)
db.students.find({},{'name' : 1,'age' : 1,'_id' :0}).skip(1).limit(2)
db.students.find({},{'name' : 1,'age' : 1,'_id' :0}).sort({'name':1}) // 1 will sort in ascending order
db.students.find({},{'name' : 1,'age' : 1,'_id' :0}).sort({'name':-1}) //-1 will sort in descending order


//MongoDb Indexes (to make searching and parsing of data easy)

use temp
for (i=0;i<10000;i++){
 db.posts.insert({'_id' : i,'name' : 'Mark', 'age' : 43}) 
  
}

db.posts.find().limit(1000)

db.posts.find({'_id' : 100}) //find will search in all document the id no is matching and then return the result
db.posts.findOne({'_id' : 100}) //findOne will check if it find the serches id then it will exist immediately , not more searching in the document (its better)

//lets create indexing

db.posts.ensureIndex({'_id' : 1})  //create index using unique key
db.posts.find({'_id' : 9999})
db.posts.dropIndex({'_id' : 1}) //Drop the index



//Aggregation(Collect and group information from variety of documents and perform various kind of operations on group data)in MongoDb

use school
db.students.find()

//will give total count of male and female
db.students.aggregate([{$group : {'_id':'$gender', MyResults : {$sum : 1}}}])

//Will give the max age male and female
db.students.aggregate([{$group : {'_id':'$gender', MaxAge : {$max : '$age'}}}]) 
//Will give the max age male and female
db.students.aggregate([{$group : {'_id':'$gender', MaxAge : {$min : '$age'}}}]) 


//How to restore and backup data in MonGoDb

