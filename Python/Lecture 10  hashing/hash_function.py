"""

Built in function
hash()
1.hash values are immutable
2.
"""


# !1.hash values are immutable
# print(hash(3.14))
# print(hash("Lorem"))
# print(hash("Lorem"))
# print(hash("divya"))
# print(hash("hello I am divya")==hash("hello I am divya"))




# ! List hashtable

# Initilize list with 10 None act as 
my_list=[None,None,None,None,None,None,None,None,None,None]

# * None means empty list []

def hash_function(value):
    sun_of_char=0
    for char in value:
        sun_of_char+=ord(char)  #ord() get ASCII value of each char and sum them
    return sun_of_char % len(my_list)  # returns the index by taking modulus with length of the list
    
print("Hash function for Divya list is : ", hash_function("Divya"))

def add(name):
    index=hash_function(name)     # get index for given name using hash()
    my_list[index]=[name]         # store the name at computed index in the list

# ! function to stop collision of names at the same index

def add1(name):
    index=hash_function(name)   # get the index for given name using hash()
    if my_list[index] is None:
        my_list[index]=[name]
    else:
        my_list[index].append(name)
        
add("Divya")
add("Rohan")
add("Sourabh")
print(my_list)

def search(name):
    index=hash_function(name)
    return my_list[index]==[name]   # returns True if given name is in list at the computated index

print(search("Divya"))
print(search("Rohan"))
print(search("Anushree"))
print(search("Sourabh"))
add("Bhumika")
print(my_list)
add("Daksh")
print(my_list)