student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student.update({'name': 'Steve', 'phone': '22020-2020'})
# print(student.get('phone', 'Not Found'))
age = student.pop('courses')

print(student)
print(age)
print(len(student))
print(student.keys())
print(student.items())

# looping dictionaries
# for key in student: # only iterates through the keys, NOT items
# print(key)

for key, value in student.items():
    print(key, value)
