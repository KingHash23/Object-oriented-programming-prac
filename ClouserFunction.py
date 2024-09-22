def outer_function(x):
    def inner_function(y):
        return x * y
    return inner_function

f = outer_function(5)
result = f(3)
print(result)