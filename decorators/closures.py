def outer_function(text):
    def inner_function():
        print(text)

    return inner_function

x = outer_function('Hey!')

x()

# The function inner_function has its scope only inside the outer_function. But with the use of closures we can easily extend its scope to invoke a function outside its scope.