def hello_folks():
    print("Hello World!")


hello_folks()


def sum(num1, num2=3):
    if (type(num1) is not int or type(num2) is not int):
        return
    return (num1+num2)


print(sum(8))


def multiple_items(*args):
    return (args)


print(multiple_items(8, 4, 5, 6, 7, 9))


def mult_named_items(**kwargs):
    print(type(kwargs))
    return kwargs


print(type([]))
