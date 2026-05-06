
# ? 1 problem
# ! create a dictionery where keys are numbers (1 to 5) and values are there square

# def dict():
#     d={x : x**2 for x in range(1,6)}
#     print(d)

# print(dict())


# ? 2 problem

# ! WAP to sort ascending or decending a dictionery by value

"""
    Dict values must be same data type dict.item() to get a list of tuple
    pairs from dict and sort it using lambda function and sorted()
"""
# ? reverse paramter can be used to sort dict in reverse order
#  using sorted method
# d={"one":1,'two':2, 'five':5, 'six':6,'three':3}
# print(sorted(d.values()))

# ? or
def sort_dict(d,reverse=False):
    return dict(sorted(d.items(),keys=lambda x: x[1],reverse=reverse))
   
d={"one":1,'two':2, 'five':5, 'six':6,'three':3}
print(d)


# ! Merge Dictionaries