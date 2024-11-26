# cook your dish here
calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls
    
def string_info(string1):
    #string1 = "qwerty"
    count_calls() #раз счетчик
    count_calls() #два счетчик
    count_calls() #три счетчик
    string_ = ()
    print(type(string_))
   
    string_ = (len(string1),string1.upper(), string1.lower())
    print(string_)
    return string_

def  is_contains(string2, list_to_search):
    count_calls() # раз счетчик
    print(type(string2))
    print(type(list_to_search))
    unique_names = list(name.casefold() for name in list_to_search)
    print(f"без регистров :{unique_names}")
    r1 = string2
    r2 = list_to_search
    if r1 in r2:
        True
    else:
        False
        
    print(string2, list_to_search)
    #print(list_to_search)
    return r1, r2

string_info("asdfghj")

is_contains('Urban', ['ban', 'baNan', 'TomaTe', 'UrBAn'])
print(count_calls())