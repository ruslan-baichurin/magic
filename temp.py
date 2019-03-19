def make_multiplier_of(n):
    def multiplier(x):
        return x * n

    return multiplier


times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

# print(times3(9))
# print(times5(3))
# print(times5(times3(2)))


def my_func(n):
    funcs = []
    def printer():
        print()

    for i in range(n):
        funcs.append(printer)

    return funcs

hello = my_func(5)
for i in range(5):
    hello[i](4)

def print_msg(msg):
    def printer():
        print(msg)

    return printer


another = print_msg('Bye')
del print_msg
another()
print_msg('Hi')


def my_func(name):
    print('Hello', name)


def my_func2(name):
    print('Good bye', name)


def print_my_func(f, name, n):
    for i in range(n):
        f(name)


# print_my_func(my_func, 'Nick', 3)
# print_my_func(my_func2, 'Nick', 3)

def create_embedded_func(f, n):
    def repeater(name):
        print_my_func(f, name, n)

    return repeater

ff = create_embedded_func(my_func, 4)


ff2 = create_embedded_func(my_func2, 2)
ff2('Polina')
ff('Nick')
