courses = ["History",   "Math", "Science", "CompSci"]
courses2 = ["Art", "Education"]
list1 = [ 78, 5, 6, 7, 8,8,8,8,8, 9,9,9,9,9,9]

courses.append("Art")
courses.insert(0,"Art") # Insert at a particular index

courses = courses + courses2 # Add 2 lists            OR
courses.extend(courses2)

courses.remove("Art")
popped = courses.pop()                                # Can only take index as argument in lists

courses.reverse()

courses.sort()                           # Sorts the original list
courses.sort(reverse=True)               # Reverse sort
courses2.reverse()
sorted_list = sorted(courses, reverse = True)         # Returns the sorted list to a new variable   NOTE: Does not alter the original string

courses.index("Art")
# courses.remove("Art")
print("Art" in courses)

for i in range(len(list1)):
    if 9 in list1:
        list1.remove(9)

print(list1)

print(courses, "\n", popped)

for index,item in enumerate(courses, start =0):           # Enumerate function to return the index value, also mentioned the start value only for index
    print(index, item)

courses_string = ",".join(courses)
courses_string = courses_string.split(",")
print(courses_string)

# Example:
#
# list = [1,2,3,4,5,6,6,7,7,8,9,10]
# index_list = []
# for index in range(0, len(list)):
#     if (list[index]>5 and list[index]<10):
#         index_list.append(index)
#
# index_list.reverse()
# for j in index_list:
#     list.remove(list[j])
#
# print(list)

#           OR
#
# list = [1,2,3,4,5,6,6,7,7,8,9,10]
# index_list = []
# for index,item in enumerate(list):
#     if (item>5 and item<10):
#         index_list.append(index)
#
# index_list.reverse()
# for j in index_list:
#     list.remove(list[j])
#
# print(list)