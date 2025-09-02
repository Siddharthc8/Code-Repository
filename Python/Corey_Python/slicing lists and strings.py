my_list = [1,2,3,4,5,6,7,8,9,10,11]
my_list2 = [11,12,13,14,15,16,17,18,19]

print(my_list[::-1])        # Reverse the string

print(my_list[2:])          # Start from an index to the end of string

print(my_list[:5])          # Start from 0 to an index of a string

print(my_list[::1])         # Step every element

print(my_list[:] + my_list2[1:])     # To print from a value



# String Slicing

string1 = "Hi How are you doing? Let's go"
string2 = "I am doing good well"

print(string1[:-9]+" "+ string2[:-5])          # To slice a string and concatenate