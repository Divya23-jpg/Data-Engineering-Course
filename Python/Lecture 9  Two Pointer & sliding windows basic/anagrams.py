"""
Input: txt = "forxxorfxdofr", pat = "for"
Output: 3
Explanation: for, orf and ofr appears in the txt, hence answer is 3.

"""

def anagrams(txt,pat):
    length1=len(txt)
    length2=len(pat)
    if(length1==length2):
        print("Anagram")
    else:
        print("Not")

    



txt="forxxorfxdofr"
pat = "for"
print(anagrams(txt,pat))