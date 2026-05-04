"Using Loops"
# ! WAP to calculate of Uppercase and lowercase character
def cal_up_lo(str):
    for i in range(0,len(str)+1):
        lower=0
        upper=0
        if(str.isupper()):
            lower=lower+1
        else:
            upper=upper+1

    print("Upper Case count is:",upper)
    print("Lower Case count is:",lower)


cal_up_lo("Hyy")


# ! using Dictionery
sentence="The quick Brown Fpx Jums over the Lazy Dog"
counts={'upper':0,'lower':0}
for i in sentence:
    if i.isupper():
        counts['upper']+=1
    elif i.islower():
        counts['lower']+=1

print("Upper case:",counts['upper'])
print("Lower case:",counts['lower'])