

# ! sorted()
num=(1,4,2,7)

# reverse=True: Decreasing order
new=sorted(num,reverse=True)
print("Tuple sorting in Tuple")
print("Normal Function: ",new)



# list.sort()
l=[3,2,5,1]
l.sort()    #Ascending order
print("List sorting")
print(l)



# Sort in string

s=sorted("Hello I am Divya".split(),key=str.casefold)
print("String sorting")
print(s)



dict={1:'one',2:'Two'}
dict.sort()
print(dict)

