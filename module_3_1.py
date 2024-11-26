# cook your dish here
calls = 0


def count_calls():
    global calls
    calls = calls + 1
    return calls


def string_info(string1):
    # string1 = "qwerty"
    count_calls()  # раз счетчик
    string_ = ()
    #print(type(string_))

    string_ = (len(string1), string1.upper(), string1.lower())
    print(string_)
    return string_


def is_contains(string2, list_to_search):
    count_calls()  # раз счетчик
    #print(type(string2))
    #print(type(list_to_search))

    if string2.casefold() in (name.casefold() for name in list_to_search):
        print(string2, list_to_search, "True!")
        return True
    else:
        print(string2, list_to_search, "False!")
        return False

    #print(string2, list_to_search)
    # print(list_to_search)
    #return r1, r2

string_info("Capybara") # запуск 1 для счетцика
string_info("Armageddon") # запуск 2 для счетчика
string_info("Armata") # запуск 3 для счетчика

is_contains('urban', ['ban', 'baNan', 'TomaTe', 'UrBAn'])
is_contains('cycle', ['recycle', 'cyclic'])
print(f" Счетчик сработал : {calls} раз(а)")
