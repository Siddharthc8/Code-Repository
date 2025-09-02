student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci ']}

student ["phone"] = "+987654321"                           # Updated the value here
student.update({"name" : "Jane"})                          # Also used for updating

print(student.get("phone", 965))                           # Returns if available if not prints the default "965"

del student["age"]                                         # Delete a key pair

removed_course = student.pop("courses")                                   # .pop can take "key" arguments only for dictionary
print(removed_course)
print(student)

for key in student:                                               # Loops through keys
    print(key)

for key, value in enumerate(student, start=0):                    # Loops through keys and values
    print(key,value)




