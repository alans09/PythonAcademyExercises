def positional_param(a, b):
    print(f"Positional_param: {a, b}")

def keyword_param(param1=1, param2=3):
    print(f"Keyword_param: {param1, param2}")

def args_param(*args):
    print(f"ARGS: {args}")

def kwargs_param(**kwargs):
    print(f"kwargs: {kwargs}")

positional_param(1, 2)
keyword_param()
keyword_param(20, 10)
keyword_param(param2=50, param1=30)
args_param()
args_param(1, 2, "3", 4, 5, 5)
d = {'a': 1, 'b': 'z'}
kwargs_param(argument_moj=1, **d)

