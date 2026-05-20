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


def hash_function(value):
    sun_of_char=0
    for char in value:
        sun_of_char+=ord(char)
    return sun_of_char % len(my_list)
    
print("Hash function for Divya list is : ", hash_function("Divya"))

def add(name):
    index=hash_function(name)
    my_list[index]=[name]


add("Divya")
add("Rohan")
add("Sourabh")
print(my_list)

def search(name):
    index=hash_function(name)
    return my_list[index]==[name]

print(search("Divya"))
print(search("Rohan"))
print(search("Anushree"))
print(search("Sourabh"))
add("Bhumika")
print(my_list)
add("Daksh")
print(my_list)