"""
Encapsulation:

Bundle  data (atributes) and methods (functions) within a class
,limiting the outside interference.

It promotes data security  by using  single hyphon (-) and double (--)
for  protected and private activities respectively

"""



class User:
    def __init__(self,name):
        self.__name=name  #private attribute


    def get_name(self):
        return self.__name
    
user1=User("Divya")
print(user1.get_name())