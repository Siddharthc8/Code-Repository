customer = {                  # "customer" is the dictionary
    "name": "John Smith",     # a dictionary cannot have two key value pairs of the same name
    "age": 30,                # numbers need not be enclosed in ""
    "is_verified" : True

}

print (customer["name"])
#print (customer["wrong value"])               Returns an error if you try to search something that is not present
print (customer.get("job"))
#print (customer.get("wrong value"))    Does not throw an error if you try to search something that is not present

# Updating key pairs
customer ["name"] = "New Name"
print (customer ["name"])
customer ["birthdate"] = "Jan 1 1980"     # Inserted new value birthdate
print (customer.get ("age", "123"))
print (customer.get ("address"))
#
customer ["address"] = "2740"
customer = dict(customer, money = 100)
del customer["money"]
customer.pop("is_verified" )
                                        # Use .keys to loop through keys and .values to loop through values
for key, value in customer.items():     # To print both the keys and values
    print(key, value)

print(customer)