
# ! Create tuple eith empty typle
# tup=()
# print(tup)
# # ! With variable
# tup_val=("Divya")
# print(tup_val)


# ! String to tuple
# str="Divya"
# print(tuple(str))

# # !Print Tuple
# tup=tuple("Divya")
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])
# print(tup[4])

#? OR
# !Using Slicing
# print(tup[1:4])  # 4 will not included
# !count number of specific String
# print(tup.count('i'))

# ! Concatenation

# tup1=tuple([1,2,3,4])
# tup2=tuple(["ABC","DEF"])
# print(tup1+tup2)


# !String slicing in Tuple
# tup=tuple("Divya")
# print("Starts with 1st and end with 4th:",tup[1:5])
# print("Reversed:",tup[::-1])
# print("Start with 1st Index:",tup[1:])
# del tup  # for delete 

# ! Tuple with different Data type
# tup=tuple([5,'welcome',7.5,True])
# print(type(tup))




# !Reversed Tuple
# tup=tuple([1,2,3,4,5])
# print(tup[::-1])

#  bDictionary in Tuple
tup=tuple([5,'welcome',7.5,True,{3:"Divya"}])
print(type(tup))
