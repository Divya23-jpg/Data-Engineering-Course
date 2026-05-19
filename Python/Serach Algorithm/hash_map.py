"""
! Before Hash Map understand dictionary

Dictionary is a key value pair data type

! Hasing
process to convert into hash table
index=keys
value=value
"""
d={"name":{"Divya","rohan"},
    "roll_no":{10,34}
  }

print(d.keys())


# ! Separate Chaining method of a hash table
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class HashTable:
    def __init__(self,size,capacity):
        self.size=size
        self.capacity=capacity  # 10%num=index
        self.table=[None]*self.capacity

def _hash(self,key):
    return hash(key) % self.capacity


def insert(self,key,value):
    index=self.hash(key)
    new_node=Node(key,value)

    if self.table[index] is None:



# if __name__=="main":
#     hash_table=