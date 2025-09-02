'''Dictionary is used to store and retrieve key value pairs or jjust a bunch of related stuff in a class type environment'''


Phone_num = input("Phone: ")
print(Phone_num)
dictionary = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}

output = " "
for key in Phone_num:
    # print(dictionary.get (key))      #    OR
    # print(dictionary[key])                OR
    output += (dictionary.get(key, "Null")) + " "    #String appending
    #   print(dictionary.get(key, "Default value if key not available"))

print(output)


