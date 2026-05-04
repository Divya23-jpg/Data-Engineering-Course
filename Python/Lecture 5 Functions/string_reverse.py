"""
str="Divya"
output:ayviD


"""
# Using String Slicing
def rev(str):
    return str[::-1]

print(rev("Divya"))


# ! WAP to calculate of Uppercase and lowercase character

def cal_up_lo(str):
    for i in range(0,len(str)+1):
        lower=0
        upper=0
        if(str.isupper()):
            lower=lower+1
        else:
            upper=upper+1

    print("Upper Case count is:"upper)
    print("Upper Case count is:"upper)
