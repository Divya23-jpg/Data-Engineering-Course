"""
A person wants to buy a bike has X rs,he dont have total amount 
He can now pat total price for bike in monthly installment.

Equated Monthly Installment [EMI]

EMI=Principal*Monthly Interest rate(R)*(1+R)**N
divided by (1+R)**N-1
N is no. of months
R is a monthly rate 



"""
# Monthly Payment he have to pay
# Find total amount

# Function
def Emi_cal(principal,rate_years,time_period):
    N=time_period*12
    rate=(rate_years/100)/12 # for monthly
    Emi=float((principal*rate*(1+rate)**N)/((1+rate)**N-1))
    total_amount=Emi*12
    print("Monthly Interest is :",Emi)
    print("Total amount in Total::",total_amount)

# Input
principal=float(input("Enter Principle::"))
rate_years=float(input("Enter yearly Rate::"))
time_period=int(input("Enter Time period::"))


# Function Call
Emi_cal(principal,rate_years,time_period)