def get_list():
    number = []
    for i in range(10):
        number.append(i)

    return number

for number in get_list():
    print(number)


def get_generator():
    for i in range(10):
        yield i

for numbers in get_generator():
    print("{} ".format(numbers), end="")

my_generator = get_generator()

next(my_generator)