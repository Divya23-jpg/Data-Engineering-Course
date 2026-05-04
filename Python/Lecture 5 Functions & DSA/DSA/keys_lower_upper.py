
# ! WAF To convert Keys (dictionery) to upper
def con_key():
    my_dict = {
        'a': 1,
        'b': 2
    }
    new_dict = {k.upper(): v for k, v in my_dict.items()}
    print(new_dict)

# con_key()

# ! WAF To convert Keys (dictionery) to upper even dictionery in dictionery
def keys_upper(test_dict):
    # return {k.upper(): keys_upper() if isinstance (v ,dict) else v for k,v in test_dict.items()}
    return {k.upper(): keys_upper(v) if isinstance(v, dict) else v for k, v in test_dict.items()}

test_dict={
    'a':1,
    'b':{'b':2},
    'c':3
}

result=keys_upper(test_dict)
# print(result)