"""
str="Divya"
output:ayviD


"""
# Using String Slicing
def rev(str):
    return str[::-1]

# print(rev("Divya"))


# ! WAP to calculate of Uppercase and lowercase character

def cal_up_lo(str):
    for i in range(0,len(str)+1):
        lower=0
        upper=0
        if(str.isupper()):
            lower=lower+1
        else:
            upper=upper+1

    # print("Upper Case count is:",upper)
    # print("Lower Case count is:",lower)

# cal_up_lo("Hyy")

# str = "Hello World"
# upperCase = 0
# lowerCase = 0
# def checkChar(str):
#     global upperCase, lowerCase   
    
#     for i in str:
#         if i.isupper():
#             upperCase += 1
#         elif i.islower():
#             lowerCase += 1
# checkChar(str)
# print(f"UpperCase characters: {upperCase}")
# print(f"LowerCase characters: {lowerCase}")

# ? using Dictionery
sentence="The quick Brown Fpx Jums over the Lazy Dog"
counts={'upper':0,'lower':0}
for i in sentence:
    if i.isupper():
        counts['upper']+=1
    elif i.islower():
        counts['lower']+=1

# print("Upper case:",counts['upper'])
# print("Lower case:",counts['lower'])


# ! WAF To convert Keys (dictionery) to upper
def con_key():
    dict={
    'a':1,
    'b':2
    }
    new_dict={k.upper():v for k,vin dict.item()}

con_key()

