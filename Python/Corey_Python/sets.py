# Unordered and no duplicates

cs_courses = {"History", "Math", "Physics", "Chemistry", "Math"}       # Eliminates the second duplicate(Math) while printing and outputs differnt order everytime you print

art_courses = {"History", "Math", "Art", "Design"}

print(cs_courses.intersection(art_courses))

print(cs_courses.union(art_courses))

print(cs_courses.intersection(art_courses))

print(cs_courses.difference(art_courses))


# RULES:
# empty_list = []
# empty_list = list()

# # Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()

# # Empty Sets
# empty_set = set ()
#
# empty_set = {}         # This isn't right! It's a dict
