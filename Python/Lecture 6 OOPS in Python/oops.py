
# ! Create an "Greeter" class which greets user as Good Morning,Good Evening or Good Night by the Username

# from datetime import datetime

# class Greeter:
#     def __init__(self, name):
#         # self.name=input("Your name:")
#         self.name=name

#     def greet(self):
#         current_hour=datetime.now().hour
#         if 5<= current_hour<12:
#             greeting="Good morning"
#         elif 12<= current_hour<18:
#             greeting="Good Evening"     






# if __name__ == "__main__":
#     greeter=Greeter("Divya")
#     print(greeter.greet())

#  ! Create a  class for vehicles which shows info like vehicle_name,vehicle_type,top_speed,models etc

class Vehicle:
    def __init__(self):
        self.v_name = input("Enter Vehicle Name: ")
        self.v_type = input("Enter Vehicle Type: ")
        self.top_speed = input("Enter Vehicle Top speed: ")
        self.model = input("Enter Vehicle model: ")

# create object without arguments
v = Vehicle()
print(v.v_name, v.v_type, v.top_speed, v.model)
 
                    # ? Or
# class Vehicle:
#     def __init__(self):
#         self.v_name = name
#         self.v_type = ty_pe
#         self.top_speed =speed
#         self.model =model

# # create object without arguments
# v = Vehicle("BMW","4 Vehicle")
# print(v.v_name, v.v_type, v.top_speed, v.model)





# ! Creare a class for bank account which stores the info of bank account like 
# ! account number, acount holder name, balance and interest rate
# !Crreate few methods for deposit  , withdraw and calculate interest




class Bank_Account:
    def __init__(self):
        self.account_num=account_num
        self.account_holder=account_holder
        self.balance=balance
        self.interset=interest


    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposite amount :{amount},Total amount is :{self.balance} ")
        else:
            print("Deposite alway be in Positive")

#     def withdraw(self,amount):
#         if amount>0:
#             self.balance-=amount
#             print(f"Withdraw amount :{amount},Total amount is :{self.balance} ")
#         else:
#             print("Insufficient balance")

#     def calculate_interest(self):
#         interest=self.balance*(self.interset/100)
#         print(f"Interset for current Balance is: {interest}")
