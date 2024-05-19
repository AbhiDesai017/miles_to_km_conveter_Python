def add(*args):
    total = 0
    for i in args:
        total += i
    return total

# print(add(2, 3, 4, 7, 9))


def calculate(n, **kwargs):      # **kwargs is dictionary
    print(kwargs)                # op = {'add': 3, 'multiply': 5}
   # for key, value in kwargs.items():
   #    print(key)
   #    print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)                      #op = 25

calculate(2, add=3, multiply=5)
