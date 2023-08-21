def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


#
# print(add(3, 5, 7,))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)
