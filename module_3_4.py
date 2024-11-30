# Задача "Однокоренные"
def single_root_words(root_word, *other_words):
    same_words= []

    #for i in other_words:
    #if root_word.casefold() in (name.casefold() for name in other_words): # не работает далее
    list_ = [i.lower() for i in other_words] # преобразуем в нижний списком
    # преобразоване выше работает, но в результат выйдут все в нижнем регистре
    # поэтому не будем использовать

    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
        # if root_word.lower() in i: # если слово содержится в списке
        #     same_words.append(i)
        #
        # elif i in root_word.lower(): # если из списка содержатся в слове
        #     same_words.append(i)
        else:
            continue
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)