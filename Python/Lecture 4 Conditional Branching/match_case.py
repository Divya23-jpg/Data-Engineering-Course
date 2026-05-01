"""
In Python, match case is part of structural pattern matching, introduced in Python 3.10.
It allows you to write cleaner conditional logic by matching values against patterns,
similar to switch statements in other languages but more powerful.



"""
# ! Example of match case
number=4
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Any other Number")

