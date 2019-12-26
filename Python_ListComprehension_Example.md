# Python List Comprehension Example

```python
__author__ = 'deepakmane'

import pymongo
uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

# This can be written as below
# students = collection.find({})
# student_list = []
#
# for student in students:
#     student_list.append(student)
# print(student_list)

# List comprehension
students = [student for student in collection.find({})]
print(students)

students = [student['mark'] for student in collection.find({}) if student['mark'] == 100]
print(students)
```
