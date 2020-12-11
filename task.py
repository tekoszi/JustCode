'''
Napisać context manager, który otworzy do zapisu i udostępni plik tymczasowy oraz przechwyci
jakiekolwiek wyjątki, które wystąpiły w trakcie jego działania, nie propagując
ich dalej, a tylko zapisując traceback do ww. pliku.

Napisać dekorator, który na podstawie swojego argumentu
wykona udekorowaną funkcję n razy i zwróci wyniki wszystkich
jako listę.
'''


import unittest

def decorator_factory(n):
    def decorator_function(function):

        result_list = []

        def reverse_wrapper(*args, **kwargs):
            for x in range(n):
                make_reverse = function()+' + DECORATED STRING'
                result_list.append(make_reverse)
            return result_list
        return reverse_wrapper

    return decorator_function


@decorator_factory(5)
def function_to_decorate():
    return 'some string'

print(function_to_decorate())

class TestStringMethods(unittest.TestCase):



if __name__ == '__main__':
    unittest.main()