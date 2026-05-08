
# ! Craete a variable length argument type method for calculating the avg score of a class room.Input can be of different length and individual score

# !Remaining

class Stu_score:
    def avg(self,*args,):
        self.s=int(input("Provide me individual Score:"))
        self.total=sum(args)
        self.average=self.total/100
        return f"The average Score of a class is:{self.average}"
        
cls=Stu_score()
print(cls.avg())

