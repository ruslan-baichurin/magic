def my_func(n):
    def printer(i):
        print(i)

    for i in range(n):
        printer(i)

my_func(5)