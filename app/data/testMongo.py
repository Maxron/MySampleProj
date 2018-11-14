from pymongo import MongoClient

DB_HOST = 'localhost'
DB_PORT = 27017

client = MongoClient(
    host=DB_HOST,
    port=DB_PORT
)

if __name__ == '__main__':
    student = {
        'id':'00001',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male'
    }

    students = [student]

    db = client.test
    collection = db.students
    result = collection.insert(students)
    print(result)
