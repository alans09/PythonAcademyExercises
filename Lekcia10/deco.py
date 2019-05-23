#### Vytvorte dekorator, ktory overi, ci vstupne parametre pre:
## def sum_numbers(a, b):
##    return a+b
# su cisla, ak nie vyhodte TypeError (raise TypeError)


## Decorator -> funkcia, ktora vracia upravenu funkciu
# priklad, dekorator, ktory kontroluje, ci vstupne parametre funkcie su cisla
def deco_validate_inputs(func):
    def inner(*args, **kwargs):
        if not isinstance(args[0], int):
            raise TypeError("First argument have to be integer")
        if not isinstance(args[1], int):
            raise TypeError("Second argument have to be integer")
        result = func(args[0], args[1])
        return result
    return inner


# @deco_validate_inputs
def sum_numbers(a, b):
    return a+b


print(sum_numbers("a",2))
