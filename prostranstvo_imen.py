def test_function():

    def inner_function():

        print('Я в области видимости функции test_function')

    inner_function() # вызываем inner_function

test_function() # работает - test_function видит inner_function
# inner_function() # не работает - эту функцию не видно (она в другом просстрансве имен)