
# ! Set Print

# a={0,1,2,3,4,5}
# for i in range(0,len(a)):
#     print(i)

# # ?Or

# a={0,1,2,3,4,5}
# for i in a:
#     print(i)

# ! string to set
# a="Divya"
# new=set(a)
# print(type(new))
    # ? Or
# set1=set("Divya")
# print(type(set1))
# print(set1)

# ! List to set

# list=[1,2,1,3,4]
# new=set(list)
# print(new)  #! If we print in a new line than loop use


# ! String to set

# s=set("Hy I Am  Divya")
# print(s)

# ! string  set to list
# s=(1,1,2,3,4)
# print(list(s))


# ! Iterate another method
# num_set={1,2,3,4,5}
# # ? value is index and value is value
# for value , char in enumerate(num_set):
#     print(char, end=" ")


# ! Adding single and multiple element
# a=set()
# print(a)
# a.add("Divya")  #Adding single element in a set
# print(a)

# a.update(["Anushree","Gourav","Manju"])  #Adding multiple element in a set
# print(a)


# ! Remove element

# b=set([0,1,2,3,4,5])
# print(" original value:", b)
# b.pop()  #Removing Random element
# print(b)

# b.remove(1)  #Removing specific element
# print(b)

# b.discard(1) #Removing specific element if not present gives error
# print(b)

# ! Remove  all element in a set

s=set([0,1,2,3,4,5])
for i in range(len(s)):
    s.remove(i)

print(s)

