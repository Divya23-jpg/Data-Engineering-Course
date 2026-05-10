
# ! Craete a variable length argument type method for calculating the avg score of a class room.Input can be of different length and individual score



class Stu_score:
    def avg(self,*args,):
           # If no args are passed, ask for input
        if not args:
            n = int(input("Enter number of students: "))
            scores = []
            for i in range(n+1):
                s = int(input(f"Enter score of student {i}: "))
                scores.append(s)
            args = tuple(scores)  # convert list to tuple for consistency

        total = sum(args)
        average = total / len(args)
        return f"The average Score of a class is: {average}"
      
   
        
cls=Stu_score()
print(cls.avg())


