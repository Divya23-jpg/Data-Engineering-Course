# user={

#     "name":["Divya","Anu","Khushi"],
#     "ID":[123,124,125],
#     "age":[18,16,20]
# }

# data=dict([('name','Divya'),('id',123),('age',20)])
# print(type(data))



# ?Basic Operation

# ! 1.Create
# my_dict={'name':'Divya','age':23}
# ! 2 . Access

# print(my_dict["name"])


# ! 3. Add/Update

# ! 4.Remove


# # ! check
# print("name" in my_dict)

# ? Dictionary Method

# .get(key,defauly): Safely retrieve a value if a key not present then return none
#  .key(): Returns a view object of all keys in the 
#  .values() :Returns a view object of all values in the dict
# .items(): Returns key value pair as a list of tuple which is most efficient way to loop through both
#  .clear(): clear a dict.


my_dict={'name':'Divya','age':23}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.get("name"))
